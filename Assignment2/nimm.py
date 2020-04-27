"""
File: nimm.py
-------------------------
This game is based in the ancient game of Nimm, a game of strategy that is named after the old German word for "take."
It is also called Tiouk Tiouk in West Africa and Tsynshidzi in China. Players alternate
taking stones until there are zero left.
"""


def main():
    # Stones quantity starts at 20
    stones = 20
    # I defined this variable to control the Player, it will be improve.
    player = 1
    print('There are ' + str(stones) + ' left.')
    # While the stones quantity is bigger than 0 the game keeps going
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
