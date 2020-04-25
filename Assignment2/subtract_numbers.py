"""
File: subtract_numbers.py
-------------------------
This program gets two real-values from the user and prints
the first number minus the second number.
"""


def main():
    """
    The program receive 2 variables from the user, num1 and num2.
    Then it will prints the first number minus the second number.
    """
    print('This program subtracts one number from another')

    # Using float() to convert the string to a float number
    num1 = float(input('Enter first number: '))
    num2 = float(input('Enter second number: '))
    result = num1 - num2

    # Using str() to convert the result to a string
    print('The result is ' + str(result))


# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()
