"""
**Name:** While loop calculator
**Author:** Christoffer Thorske Johnsen
**Created:** 04.01.2019
"""

import time
from sense_hat import SenseHat

sense = SenseHat()


def tic_tac():

    X = [255, 0, 0]  # Red
    O = [0, 0, 255]  # Blue
    B = [0, 0, 0]  #Black
    W = [255, 255, 255] #White

    brett = [
    W, W, B, W, W, B, W, W,
    W, W, B, W, W, B, W, W,
    B, B, B, B, B, B, B, B,
    W, W, B, W, W, B, W, W,
    W, W, B, W, W, B, W, W,
    B, B, B, B, B, B, B, B,
    W, W, B, W, W, B, W, W,
    W, W, B, W, W, B, W, W
    ]


    opp_del = ([6, 7, 14, 15], [3, 4, 11, 12], [0, 1, 8, 9],
               [30, 31, 38, 39], [27, 28, 35, 36],  [24, 25, 32, 33],
               [54, 55, 62, 63], [51, 52, 59, 60], [48, 49, 56, 57])



    win_pos = ((0, 3, 6), (24, 27, 30), (48, 51, 54), (0, 3, 6), (3, 27, 51),
               (6, 30, 54), (0, 27, 54), (6, 27, 48))
    end = False

    def draw_brett():
        sense.set_pixels(brett)

    def pl_1():
        n = choose_numb()
        for i in opp_del[n]:
            if brett[i] == [255, 0, 0] or brett[i] == [0, 0, 255]:
                print('The place is not free!')
                pl_1()
            else:
                brett[i] = [255, 0, 0]

    def pl_2():
        n = choose_numb()
        for i in opp_del[n]:
            if brett[i] == [255, 0, 0] or brett[i] == [0, 0, 255]:
                print('The place is not free!')
                pl_2()
            else:
                brett[i] = [0, 0, 255]

    def choose_numb():
        while True:
            try:
                a = int(input('\n Choose a number: '))
                if a in range(1,10):
                    a -= 1
                    return a
                else:
                    print('Not on the board')
            except ValueError:
                print('Not a number')

    def win():
        for a, b, c in win_pos:
            if brett[a] == [0, 0, 255] and brett[b] == [0, 0, 255] and brett[c] == [0, 0, 255] or brett[a] == [255, 0, 0] and brett[b] == [255, 0, 0] and brett[c] == [255, 0, 0]:
                print('Congratulations!\n')
                return True
        if 36 == sum((pos == [0, 0, 255] or pos == [255, 0, 0]) for pos in brett):  #Need to change
            print("The game ends in a tie\n")
            sense.set_rotation(180)
            sense.show_message("Tie")
            return True

    while not end:
        draw_brett()
        end = win()
        if end == True:
            print('Player 2 won!!')
            sense.set_rotation(180)
            sense.show_letter("2")
            time.sleep(1)
            sense.clear()
            break
        print("Player 1 choose where to place red marke")
        pl_1()
        print()
        draw_brett()
        end = win()
        if end == True:
            print('Player 1 won!!')
            sense.set_rotation(180)
            sense.show_letter("1")
            time.sleep(3)
            sense.clear()
            break
        print("Player 2 choose where to place blue marke")
        pl_2()
        print()

tic_tac()
