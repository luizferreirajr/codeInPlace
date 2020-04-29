"""
File: examplefor.py
------------------
Print a string adding spaces each line.
"""
import math

MAX_SPACES = 20


def main():
    for j in range(MAX_SPACES):
        print_n_spaces(j)
        print(print_io(0,0))

# print_io
# prints shift_i spaces,
# then it prints "i"
# then it prints shift_o spaces
# then it prints "o"
def print_io(shift_i, shift_o):
    print_n_spaces(shift_i)
    print_no_new_line("i")
    print_n_spaces(shift_o)
    print_no_new_line("o")
    print("")


def print_n_spaces(n):
    for i in range(n):
        print_no_new_line(' ')


# takes in a string, and prints without the enter
def print_no_new_line(to_print):
    print(to_print, end="")


# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()