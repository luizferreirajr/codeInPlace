from simpleimage import SimpleImage

DARK_THRESHOLD = 128


def main():
    """
    This program applies a monochrome filter to an image by
    making all the pixels that are dark enough into full black
    pixels (red=0, green=0, blue=0) and all the others
    to full white pixels (red=255, blue=255, green=255).

    Here, a pixel is dark enough if its average value is
    less than 128
    """
    # load image
    image = SimpleImage('images/joker.jpg')
    # TODO: apply monochrome filter
    for pixel in image:
        average = (pixel.red + pixel.green + pixel.blue) // 3
        # See if this pixel is "sufficiently" black
        if average < 128:
            pixel.red = 0
            pixel.green = 0
            pixel.blue = 0
        else:
            pixel.red = 255
            pixel.green = 255
            pixel.blue = 255

    image.show()


if __name__ == '__main__':
    main()