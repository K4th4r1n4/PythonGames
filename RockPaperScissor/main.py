#!/usr/bin/env python

import random

def IsInt(x):
    try:
        int(x)
        return True
    except ValueError:
        return False

def main():
    # dict of possible options
    options = {1:"Rock", 2:"Paper", 3:"Scissor"}

    # 1: win, 0: draw, -1: loose
    rules = {1:{1: 0, 2:-1, 3: 1},
             2:{1: 1, 2: 0, 3:-1},
             3:{1:-1, 2: 1, 3: 0}}

    user = 0

    while True:
        # get user input
        user = input("Rock(1), Paper(2) or Scissor(3)?\n")
        # check if input represents integer
        if IsInt(user):
            user = int(user)
            # check if input is in valid range [1-3]
            if user >= 1 and user <=3:
                break
        print("Input not valid. Try again.")

    # random choice of opponent
    opponent = random.randint(1,3)

    print("You chose {0}.".format(options[user]))
    print("CPU chose {0}.".format(options[opponent]))

    outcome = rules[user][opponent]

    if   outcome ==  1:
        print("You won! :)")
    elif outcome ==  0:
        print("It's a draw. :/")
    elif outcome == -1:
        print("You lost. :(")

if __name__ == "__main__":
    main()