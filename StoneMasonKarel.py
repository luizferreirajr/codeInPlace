from karel.stanfordkarel import *

"""
File: StoneMasonKarel.py
------------------------
When you finish writing code in this file, StoneMasonKarel should 
solve the "repair the quad" problem from Assignment 1. You
should make sure that your program works for all of the 
sample worlds supplied in the starter folder.
"""


def main():
    repair_column()


#Do the repair in the column if Karel is facing east
#After the repair she go back to her initial position
def repair_column():
    while facing_east():
        turn_left()
        while front_is_clear():
            if beepers_present():
                move()
            else:
                put_beeper()
        going_back()


# Going back to her initial position
# If she encounter a wall in front of her, she will turn left to don't face east
# I need to improve that but was a solution that I've found.
def going_back():
    if no_beepers_present():
        put_beeper()
    turn_around()
    while front_is_clear():
        move()
    turn_left()
    if front_is_clear():
        next_column()
    else:
        turn_left()


def turn_around():
    turn_left()
    turn_left()


# Go to the next column
def next_column():
    for i in range(4):
        move()

# There is no need to edit code beyond this point

if __name__ == "__main__":
    run_karel_program()
