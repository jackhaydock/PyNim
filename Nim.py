from __future__ import print_function
from random import randint
import re

#-------------------------------------------------------------------------------
# Functions
#-------------------------------------------------------------------------------

def show_pieces():
    #global pieces
    j = 0
    print("|", end='')
    while j < pieces:
        print("-|", end='')
        j += 1
    print("")
    print(str(pieces) + " Pieces Left")

def nim_choose():
    a = randint(1, max_num)

    if (pieces % (max_num + 1) == 0): # pieces is multiple of 4
        x = randint(1, max_num)
    else:
        i = pieces - 1
        while (i % (max_num + 1) != 0):
            i -= 1
        b = pieces - i

    if (pieces < max_num):
        x = pieces
    else:
        if randint(0, difficulty) == 0: #eg. if difficulty = 0, nim will always play b
            x = b
        else:
            x = a

    return x

def human_choose():
    x = -1
    while x == -1:
        try:
            y = int(raw_input("How many pieces will you take: "))
        except:
            print("Please enter a number")
            continue

        if (y <= 0):
            print("Please enter a number greater than 0")
        elif (y > max_num):
            print("Please enter a number less than " + str(max_num + 1))
        elif (y > pieces):
            print("Please enter a number less than " + str(pieces + 1))
        else:
            x = y
    return x

def move(player):
    global pieces
    print("")
    show_pieces()
    print(player + "'s turn:")
    if player == "Nim":
        x = nim_choose()
    else:
        x = human_choose()
    print(player + " removes " + str(x) + " pieces")
    pieces -= x
    if pieces == 0:
        print("")
        print("No Pieces Left!")
        print(player + " Wins!")
        exit()

#-------------------------------------------------------------------------------
# Runtime
#-------------------------------------------------------------------------------
pieces = 12
max_num = 3
difficulty = 3


print("     __ _            ")
print("  /\ \ (_)_ __ ___   ")
print(" /  \/ / | '_ ` _ \  ")
print("/ /\  /| | | | | | | ")
print("\_\ \/ |_|_| |_| |_| ")
print("-------------------- ")
print("Difficulty: " + str(difficulty))
print("Starting Pieces: " + str(pieces))
print("Max Pieces Per Turn: " + str(max_num))

while pieces > 0:
    move("Human")
    move("Nim")
