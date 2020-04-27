"""
File: hailstones.py
-------------------
This is a file for the optional Hailstones problem, if
you'd like to try solving it.
"""


def main():

    # Pick some positive integer and call it n.
    num1 = int(input('Enter a positive number: '))
    while num1 <= 0:
        num1 = int(input('Invalid number, please enter a positive number: '))

    # Continue this process until n is equal to one.
    while num1 != 1:
        # I used this base variable to store the original value of num1 each loop.
        base = num1

        # If n is even, divide it by two.
        if (num1 % 2) == 0:
            num1 = int((num1 / 2))
            print(str(base) + ' is even, so I take half: ' + str(num1))

        # If n is odd, multiply it by three and add one.
        elif (num1 % 2) != 0:
            num1 = int((num1 * 3) + 1)
            print(str(base) + ' is odd, so I make 3n + 1: ' + str(num1))


# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()
