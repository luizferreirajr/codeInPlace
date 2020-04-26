"""
File: nimm.py
-------------------------
Add your comments here.
"""


def main():
    stones = 20
    player = 1
    print('There are ' + str(stones) + ' left.')
    while stones > 0:
        answer = int(input('Player ' + str(player) + ' would you like to remove 1 or 2 stones?: '))

        # While the answer is not 1 or 2 the program will keep asking a input from the user
        while answer != 1 and answer != 2:
            answer = int(input('Please enter 1 or 2:'))
        stones -= answer

        # I need to improve that...The program checks if the player at the moment is 1 or 2, then he changes the value.
        if player == 1:
            player = 2
        elif player == 2:
            player = 1

        """
            The program checks how many stones left to avoid printing negative numbers and to decide de winner
            The last player to remove the stone loses.
        """
        if stones > 0:
            print('There are ' + str(stones) + ' left.')
        else:
            print('Player ' + str(player) + ' wins.')


# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()
