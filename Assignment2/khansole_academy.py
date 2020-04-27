"""
File: khansole_academy.py
-------------------------
This program generates simple addition problems that
involve adding two 2-digit integers (i.e., the numbers 10 through 99). The user asks
for an answer to each problem. This program determines if the answer is
correct or not and give the user a message.
This program keeps giving the user problems until the user reach 3 problems correct in a row.
"""

import random

CORRECT_ROW = 3
MIN_RANDOM = 10
MAX_RANDOM = 99


def main():
    answer = int(input('WELCOME TO KHANSOLE ACADEMY\n1- Addition\n2- Subtraction\n3- Division\n4- Multiplication\n'
                       'What do you want to practice?: '))

    # While the user does not select a valid answer the program will ask a new question
    while answer < 0 or answer > 4:
        print('Invalid option\n')
        answer = int(input('WELCOME TO KHANSOLE ACADEMY\n1- Addition\n2- Subtraction\n3- Division\n4- Multiplication\n'
                           'What do you want to practice?: '))
    if answer == 1:
        addition()
    elif answer == 2:
        subtraction()
    elif answer == 3:
        division()
    elif answer == 4:
        multiplication()


# Addition function
def addition():
    # I started with a variable to count the correct answers the user gave to the program
    correct_answers = 0
    # Then I used a while loop to compare the correct answers with the row that the user needs to master the subject
    while correct_answers != CORRECT_ROW:
        # I created two variables to generate the random numbers, it's important to put the variables inside the loop
        # If they are outside the program will use the same numbers
        num1 = int(random.randint(MIN_RANDOM, MAX_RANDOM))
        num2 = int(random.randint(MIN_RANDOM, MAX_RANDOM))
        addition = (num1 + num2)

        # Print a question with two random numbers between MIN_RANDOM and MAX_RANDOM
        answer = int((input('What is ' + str(num1) + '+' + str(num2) + ' ?: ')))

        # Check if the answer is correct or not and print the result
        if answer == addition:
            # If the answer is correct the program will add 1 unit into the correct_answers variable
            correct_answers += 1
            print("Correct! You've gotten " + str(correct_answers) + " correct in a row")
        else:
            # If the answer is incorrect, the program will print a message and will define the value of 0
            # The program needs to do that to start the count again if the user can't reach 3 corrects answers in a row
            print("Incorrect. The expected answer is " + str(addition))
            correct_answers = 0

    # When the user gives 3 corrects answers in a row, finish the program and congrats the user
    if correct_answers == CORRECT_ROW:
        print('Congratulations! You mastered addition!')


# Subtraction function
def subtraction():
    # I started with a variable to count the correct answers the user gave to the program
    correct_answers = 0
    # Then I used a while loop to compare the correct answers with the row that the user needs to master the subject
    while correct_answers != CORRECT_ROW:
        # I created two variables to generate the random numbers, it's important to put the variables inside the loop
        # If they are outside the program will use the same numbers
        num1 = int(random.randint(MIN_RANDOM, MAX_RANDOM))
        num2 = int(random.randint(MIN_RANDOM, MAX_RANDOM))
        subtraction = (num1 - num2)

        # Print a question with two random numbers between MIN_RANDOM and MAX_RANDOM
        answer = int((input('What is ' + str(num1) + '-' + str(num2) + ' ?: ')))

        # Check if the answer is correct or not and print the result
        if answer == subtraction:
            # If the answer is correct the program will add 1 unit into the correct_answers variable
            correct_answers += 1
            print("Correct! You've gotten " + str(correct_answers) + " correct in a row")
        else:
            # If the answer is incorrect, the program will print a message and will define the value of 0
            # The program needs to do that to start the count again if the user can't reach 3 corrects answers in a row
            print("Incorrect. The expected answer is " + str(subtraction))
            correct_answers = 0

    # When the user gives 3 corrects answers in a row, finish the program and congrats the user
    if correct_answers == CORRECT_ROW:
        print('Congratulations! You mastered addition!')


# Division function
def division():
    # I started with a variable to count the correct answers the user gave to the program
    correct_answers = 0
    # Then I used a while loop to compare the correct answers with the row that the user needs to master the subject
    while correct_answers != CORRECT_ROW:
        # I created two variables to generate the random numbers, it's important to put the variables inside the loop
        # If they are outside the program will use the same numbers
        num1 = int(random.randint(MIN_RANDOM, MAX_RANDOM))
        num2 = int(random.randint(MIN_RANDOM, MAX_RANDOM))
        division = (num1 / num2)

        # Print a question with two random numbers between MIN_RANDOM and MAX_RANDOM
        answer = int((input('What is ' + str(num1) + '/' + str(num2) + ' ?: ')))

        # Check if the answer is correct or not and print the result
        if answer == division:
            # If the answer is correct the program will add 1 unit into the correct_answers variable
            correct_answers += 1
            print("Correct! You've gotten " + str(correct_answers) + " correct in a row")
        else:
            # If the answer is incorrect, the program will print a message and will define the value of 0
            # The program needs to do that to start the count again if the user can't reach 3 corrects answers in a row
            print("Incorrect. The expected answer is " + str(division))
            correct_answers = 0

    # When the user gives 3 corrects answers in a row, finish the program and congrats the user
    if correct_answers == CORRECT_ROW:
        print('Congratulations! You mastered addition!')


# Multiplication function
def multiplication():
    # I started with a variable to count the correct answers the user gave to the program
    correct_answers = 0
    # Then I used a while loop to compare the correct answers with the row that the user needs to master the subject
    while correct_answers != CORRECT_ROW:
        # I created two variables to generate the random numbers, it's important to put the variables inside the loop
        # If they are outside the program will use the same numbers
        num1 = int(random.randint(MIN_RANDOM, MAX_RANDOM))
        num2 = int(random.randint(MIN_RANDOM, MAX_RANDOM))
        multiplication = (num1 * num2)

        # Print a question with two random numbers between MIN_RANDOM and MAX_RANDOM
        answer = int((input('What is ' + str(num1) + '*' + str(num2) + ' ?: ')))

        # Check if the answer is correct or not and print the result
        if answer == multiplication:
            # If the answer is correct the program will add 1 unit into the correct_answers variable
            correct_answers += 1
            print("Correct! You've gotten " + str(correct_answers) + " correct in a row")
        else:
            # If the answer is incorrect, the program will print a message and will define the value of 0
            # The program needs to do that to start the count again if the user can't reach 3 corrects answers in a row
            print("Incorrect. The expected answer is " + str(multiplication))
            correct_answers = 0

    # When the user gives 3 corrects answers in a row, finish the program and congrats the user
    if correct_answers == CORRECT_ROW:
        print('Congratulations! You mastered addition!')


# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()
