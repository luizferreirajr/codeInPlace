from karel.stanfordkarel import *

"""
File: TripleKarel.py
--------------------
When you finish writing this file, TripleKarel should be
able to paint the exterior of three buildings in a given
world, as described in the Assignment 1 handout. You
should make sure that your program works for all of the 
Triple sample worlds supplied in the starter folder.
"""


# Paint all the buildings
def main():
    paint_buildings()


# Paint the buildings around, using the left side test
# Turning right to be in position to go to another building
def paint_buildings():
    for i in range(2):
        paint_building_around()
        turn_right()
    paint_building_around()


# Paint the buildings around, using the left side test
# Turning Karel without painting the corners
def paint_building_around():
    for i in range(2):
        paint()
        turn_karel_corner()
    paint()


# Checking if the left side has a wall to be able to paint
# Moving to the next square
def paint():
    while left_is_blocked():
        put_beeper()
        move()


# Turning Karel to go to another wall
def turn_karel_corner():
    turn_left()
    move()


# Turning Karel around 180 degrees
def turn_right():
    for i in range(3):
        turn_left()


# There is no need to edit code beyond this point

if __name__ == "__main__":
    run_karel_program()
