"""
This program asks for the user the 3 coefficients of a quadratic equation and outputs the roots.
"""

from math import sqrt


def main():
    print("Welcome to Quadratic Equation Solver!")
    print("This program solves equations of the form Ax^2 + Bx + C = 0.")

    while True:
        # Read the polynomial coefficients from the user.
        # We cast to float before assigning to variables.
        a = float(input("Enter the coefficient A: "))
        b = float(input("Enter the coefficient B: "))
        c = float(input("Enter the coefficient C: "))

        discriminant = b * b - 4 * a * c

        # Recall that sqrt(-4) = i * sqrt(4) = i * 2.
        # Since Python can't directly handle imaginary numbers, we will manually
        # track whether the discriminant was negative and then do the
        # calculations always using a positive discriminant. We can then prepend
        # the imaginary number "i" in the printed output if the discriminant was
        # negative.
        discriminant_is_negative = False
        if discriminant < 0:
            discriminant_is_negative = True
            discriminant = -1 * discriminant

        # We keep the first and second parts of the formula separate
        # here because the second term might be imaginary.
        first_term = -b / (2 * a)
        second_term = sqrt(discriminant) / (2 * a)

        # Display the results to the user.
        equation_str = str(a) + " x^2 + " + str(b) + " x + " + str(c) + " = 0"
        print("The roots of " + equation_str + " are:")
        if discriminant_is_negative:
            # Need to print real and imaginary parts separately.
            print("x1 = " + str(first_term) + " + i" + str(second_term))
            print("x2 = " + str(first_term) + " - i" + str(second_term))
        else:
            # Here we just add/subtract the terms since they are real numbers.
            print("x1 = " + str(first_term + second_term))
            print("x2 = " + str(first_term - second_term))
        print("")


if __name__ == '__main__':
    main()