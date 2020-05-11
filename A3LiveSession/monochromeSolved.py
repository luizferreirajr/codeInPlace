from simpleimage import SimpleImage


def main():
    """
    This program applies a monochrome filter to an image by
    making all the pixels that are dark enough into full black
    pixels (red=255, green=255, blue=255) and all the others
    to full white pixels (red=0, blue=0, green=0).
    """
    image = SimpleImage('images/girl.jpeg')

    for pixel in image:
        if should_be_black(pixel):
            pixel.red = 255
            pixel.green = 255
            pixel.blue = 255
        else:
            pixel.red = 0
            pixel.green = 0
            pixel.blue = 0

    image.show()


def should_be_black(px):
    px_avg = get_pixel_average(px)
    return px_avg > 255/2


def get_pixel_average(px):
    return (px.red + px.green + px.blue) // 3


if __name__ == '__main__':
    main()