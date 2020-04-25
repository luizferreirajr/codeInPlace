import random

"""
This program simulates an Eight Ball game, basically it is a random answer game.
First the user needs to give a question then the Eight Ball program will find a random answer and will
print it in the prompt.
"""


def main():
        question = input("Ask a yes or no question: ")

        # Print the answer
        while question != "":

                answer = random.randint(1, 6)
                first_answer = "As i see it, yes."
                second_answer = "Ask again later."
                third_answer = "Better not tell you now."
                forth_answer = "Cannot predict now."
                fifth_answer = "Concentrate and ask again."
                sixth_answer = "Don't count on it."

                if answer == 1:
                        print(first_answer)
                if answer == 2:
                        print(second_answer)
                if answer == 3:
                        print(third_answer)
                if answer == 4:
                        print(forth_answer)
                if answer == 5:
                        print(fifth_answer)
                if answer == 6:
                        print(sixth_answer)

                question = input("Ask a yes or no question: ")

if __name__ == '__main__':
        main()