"""
Your task is to write a simple number guessing game. The program's specifications are as follows:

The program should ask the user for their name and refer to the user by name for the duration of the session.
The user should be prompted for a guess in a predefined interval that is provided to the user.
The user should be continuously prompted for guesses until they guess the correct answer.
The user should be provided with feedback about the guess (whether it's too high or low).
The user should also be notified if the guess is outside the allowable range.
Once the correct number is guessed, a new game should be started.

"""

import random

SECRET_NUMBER_MIN = 0
SECRET_NUMBER_MAX = 100


def main():
    print("Hello! Let's play a number guessing game.")
    print("Press ctrl+c to quit.")
    name = input("Please enter your name: ")

    while True:
        secret_number = random.randint(0, 100)
        print(str(name) + ", I'm thinking of an integer between " + str(SECRET_NUMBER_MIN) + " and "
              + str(SECRET_NUMBER_MAX))

        answer = int(input("Please enter your guess: "))
        while answer != secret_number:

            while answer < SECRET_NUMBER_MIN or answer > SECRET_NUMBER_MAX:
                print(str(name) + ", the guess is outside the allowable range, try again!")
                answer = int(input("Please enter your guess: "))

            if answer > secret_number:
                print(str(name) + ", your guess was too high!\n")
            elif answer < secret_number:
                print(str(name) + ", your guess was too low!\n")

            answer = int(input("Please enter your guess: "))

        print("Congratulations " + str(name) + ", you got it!\n")


if __name__ == '__main__':
    main()