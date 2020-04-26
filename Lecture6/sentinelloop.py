"""
File: sentinelloop.py
------------------
A program that prompts the user for numbers until the user types -1, then output the total
of the numbers.
"""
SENTINEL = -1


def main():
    total = 0
    number = int(input('Type a number: '))

    # The while loop is responsible for compare the variable number with de constant SENTINEL
    # post condition: The program needs to keep making the same question until the user types the SENTINEL value.
    while number != SENTINEL:
        total += number
        number = int(input('Type a number: '))
    print('The total is ' + str(total))


# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()