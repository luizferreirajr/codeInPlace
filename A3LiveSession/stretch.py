"""
File: stretch.py
----------------
Take an image and stretch it by some factor.
Written collaboratively during the Live Assignment Help Session for A3!
"""
from simpleimage import SimpleImage


def make_stretched(filename):
    """
    This function returns a stretched version of the original
    image (the image in the filename) by stretching the input
    image by a factor of 2 in the width.
    """
    image = SimpleImage(filename)
    # Create a stretched image and return it
    return image



def main():
    filename = 'images/simba-sq.jpg'

    original = SimpleImage(filename)
    original.show()

    stretched = make_stretched(filename)
    stretched.show()


if __name__ == '__main__':
    main()