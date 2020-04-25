"""
Write a program to prompt the user for a weight on earth and print
the equivalent weight on the moon
"""

def main():
    earth_weight = int(input('Enter a weight on earth: '))
    moon_weight = ((earth_weight/9.81)*1.622)
    print('Equivalent weight on the moon: ' + str(round(moon_weight, 1)))

if __name__ == '__main__':
    main()