from karel.stanfordkarel import * 

"""
File: MidpointKarel.py
----------------------
When you finish writing it, MidpointKarel should
leave a beeper on the corner closest to the center of 1st Street
(or either of the two central corners if 1st Street has an even
number of corners).  Karel can put down additional beepers as it
looks for the midpoint, but must pick them up again before it
stops.  The world may be of any size, but you are allowed to
assume that it is at least as tall as it is wide.
"""

# Check if the front is blocked because the first World 1x1
def main():
    if front_is_blocked():
        put_beeper()
    else:
        add_beepers()
        second_step()


# Add the first line of beepers to check
def add_beepers():
    move()
    while front_is_clear():
        put_beeper()
        move()
    turn_around()
    move()


# Check the edges and, at the end add the final beeper to conclude the exercise
def second_step():
    while beepers_present():
        move()
    while no_beepers_present():
        check_edges()
        if beepers_present():
            catch_beepers()
        else:
            put_beeper()


# Check the no beepers edges to start the cleaning of beepers
def check_edges():
    if no_beepers_present():
        turn_around()
        move()


# Catch the beepers and move Karel to the next square
def catch_beepers():
    pick_beeper()
    move()
    while beepers_present():
        move()


# Turn Karel around
def turn_around():
    turn_left()
    turn_left()


# Turn Karel 180 degrees
def turn_right():
    turn_left()
    turn_left()
    turn_left()

# There is no need to edit code beyond this point

if __name__ == "__main__":
    run_karel_program()
