"""
File: liftoff.py
----------------------
This program writes out the calls for a spaceship that is about to launch.
It counts down the numbers from 10 to 1 and then writes “Liftoff!”
"""
START_COUNT = 10
END_COUNT = 0
STEP_COUNT = -1

def main():
    """
    This program use a structure range(start, end, step) using the START_COUNT as a constant to start,
    the end I configured with a END_COUNT constant and the step, responsible to minus a value in the for loop.

    My idea was to creat an open program wich anyone can use to countdown anything.
    """
    for i in range(START_COUNT, END_COUNT, STEP_COUNT):
        print(i)
    print('Liftoff!')


# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == "__main__":
    main()
