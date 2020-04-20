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
# After the first validation she will starts sow beepers to keep her track
# Then Karel will turn around to start the harvest of beepers, checking the edges to control her position
# The harvest_beepers method is responsible for positioning Karel with a beeper in the middle of any map
def main():
    if front_is_blocked():
        put_beeper()
    else:
        sow_beepers()
        go_back()
        harvest_beepers()


# Add the first line of beepers to check, I call that "Sow beepers"
def sow_beepers():
    move()
    while front_is_clear():
        put_beeper()
        move()


# When Karel face a wall she will go back to start the harvest
def go_back():
    turn_around()
    move()


# Check the edges and, at the end add the final beeper to conclude the exercise
# I call that "harvest beepers"
def harvest_beepers():
    while beepers_present():
        move()
    clean_edges()


# clean all the edges that have at least one beeper
# at the end, if Karel cannot find a beeper, she needs to place one.
def clean_edges():
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
    for i in range(2):
        turn_left()


# Turn Karel 180 degrees
def turn_right():
    for i in range(3):
        turn_left()


# There is no need to edit code beyond this point

if __name__ == "__main__":
    run_karel_program()
