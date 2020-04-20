from karel.stanfordkarel import *

"""
File: StoneMasonKarel.py
------------------------
When you finish writing code in this file, StoneMasonKarel should 
solve the "repair the quad" problem from Assignment 1. You
should make sure that your program works for all of the 
sample worlds supplied in the starter folder.
"""


# Do the repair in the column if Karel is facing east
# After the repair she go back to her initial position
# pre condition: Karel facing east
# post condition: Karel facing east
def main():
    while facing_east():
        climb_column()
        going_back()
        go_to_next_column()


# Karel will climb the column adding beepers when she can't find beepers
def climb_column():
    turn_left()
    while front_is_clear():
        if beepers_present():
            move()
        else:
            put_beeper()


# Going back to her initial position
# If she encounter a wall in front of her, she will turn left to don't face east
# I need to improve that but was a solution that I've found.
def going_back():
    check_the_top()
    turn_around()
    go_down()
    turn_left()


# Verify the top of the column to check if there is a no beepers
# If is that true, Karel will put the last beeper
def check_the_top():
    if no_beepers_present():
        put_beeper()


# Karel will go down to the base
def go_down():
    while front_is_clear():
        move()


# Karel will check if there is a wall in front of her
# If is that true she will stop, if is not, she will move to the next column
def go_to_next_column():
    if front_is_clear():
        next_column()
    else:
        turn_left()


# Turn Karel around
def turn_around():
    for i in range(2):
        turn_left()


# Go to the next column
def next_column():
    for i in range(4):
        move()


# There is no need to edit code beyond this point

if __name__ == "__main__":
    run_karel_program()
