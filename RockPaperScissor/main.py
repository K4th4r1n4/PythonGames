#!/usr/bin/env python3

import tkinter as tk
import random

# dict of possible options
options = {1:"Rock", 2:"Paper", 3:"Scissor"}

# 1: win, 0: draw, -1: loose
rules = {1:{1: 0, 2:-1, 3: 1},
         2:{1: 1, 2: 0, 3:-1},
         3:{1:-1, 2: 1, 3: 0}}

def battle(user):
    '''ToDo.'''

    # random choice of opponent
    opponent = random.randint(1,3)

    overview = "You chose {0}.\nCPU chose {1}.\n".format(options[user],
                                                       options[opponent])

    # determine winner
    outcome = rules[user][opponent]

    result = ""
    if outcome ==  1:
        result = "You won! :)\n"
    elif outcome ==  0:
        result = "It's a draw. :/\n"
    elif outcome == -1:
        result = "You lost. :(\n"

    label_result.config(text=overview+result)


root = tk.Tk()
# set title
root.title("RockPaperScissor")

# rock button
btn_rock= tk.Button(root, text ="Rock", height=7, width=20,
                    command=lambda:battle(1))
btn_rock.grid(row=3,column=0)

# paper button
btn_paper = tk.Button(root, text="Paper", height=7, width=20,
                      command=lambda:battle(2))
btn_paper.grid(row=3,column=1)

# scissor button
btn_scissor = tk.Button(root, text="Scissor", height=7, width=20,
                        command=lambda:battle(3))
btn_scissor.grid(row=3,column=2)

message = ""
label_result = tk.Label(root, text=message)
label_result.grid()

root.mainloop()