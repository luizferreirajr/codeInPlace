"""
File: stretch.py
----------------
Take an image and stretch it by some factor.
Written collaboratively during the Live Assignment Help Session for A3!
"""

# The line below imports SimpleImage for use here
# Its depends on the Pillow package being installed
from simpleimage import SimpleImage


def make_stretched(filename, scale):
    image = SimpleImage(filename)
    # Make a new image of the appropriate size
    result_image = SimpleImage.blank(scale*image.width, image.height) # width, height

    # Loop over every pixel in the original image
    for y in range(image.height):
        for x in range(image.width):
            # Grab the pixel we want to copy
            pixel_to_copy = image.get_pixel(x, y)

            # Copy over that pixel scale times, shifting over by 1 each time
            for i in range(scale):
                result_image.set_pixel(scale * x + i, y, pixel_to_copy)

    return result_image



def main():
    filename = 'images\simba-sq.jpg'

    original = SimpleImage(filename)
    original.show()

    # scale by 2
    stretched = make_stretched(filename, 2)
    stretched.show()

    # scale by 3
    stretched = make_stretched(filename, 3)
    stretched.show()


if __name__ == '__main__':
    main()