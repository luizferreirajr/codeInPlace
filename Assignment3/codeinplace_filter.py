"""
File: codeinplace_filter.py
----------------
This program implements a rad image filter.
"""

from simpleimage import SimpleImage

DEFAULT_FILE = 'images/quad.jpg'

def main():
    # Get file and load image
    filename = get_file()
    image = SimpleImage(filename)

    # Show the image before the transform
    image.show()

    # Apply the filter
    # The pixel.color will receive himself times the value necessary to do the CodeInPlace filter.
    codeinplace_filter(image)

    # Show the image after the transform
    image.show()
    

def get_file():
    # Read image file path from user, or use the default file
    filename = input('Enter image file (or press enter for default): ')
    if filename == '':
        filename = DEFAULT_FILE
    return filename


def codeinplace_filter(image):
    for pixel in image:
        pixel.red *= 1.5
        pixel.green *= 0.7
        pixel.blue *= 1.5


if __name__ == '__main__':
    main()