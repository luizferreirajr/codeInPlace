"""
This program generates the Warhol effect based on the original image.
"""
import random
from simpleimage import SimpleImage

N_ROWS = 2
N_COLS = 3
PATCH_SIZE = 222
WIDTH = N_COLS * PATCH_SIZE
HEIGHT = N_ROWS * PATCH_SIZE
PATCH_NAME = 'images/simba-sq.jpg'


def main():
    final_image = SimpleImage.blank(WIDTH, HEIGHT)
    # This is an example which should generate a pinkish patch
    # patch = make_recolored_patch(random.uniform(0.0, 2.0), random.uniform(0.0, 2.0), random.uniform(0.0, 2.0))

    # The first for loop will run trough the cols and rows
    for col in range(N_COLS):
        for row in range(N_ROWS):
            # The make_recolored_patch inside this for loop will automatically generate awesome colors (sometimes)
            patch = make_recolored_patch(random.uniform(0.0, 2.0), random.uniform(0.0, 2.0),
                                         random.uniform(0.0, 2.0))

            # The second for loop will run trough the x, y inside each patch
            for y in range(PATCH_SIZE):
                for x in range(PATCH_SIZE):

                    pixel_to_copy = patch.get_pixel(x, y)

                    # Creating the first row
                    for i in range(N_ROWS):
                        final_image.set_pixel(x + col * PATCH_SIZE, y + row * PATCH_SIZE, pixel_to_copy)

    final_image.show()


def make_recolored_patch(red_scale, green_scale, blue_scale):
    '''
    Implement this function to make a patch for the Warhol Filter. It
    loads the patch image and recolors it.
    :param red_scale: A number to multiply each pixels' red component by
    :param green_scale: A number to multiply each pixels' green component by
    :param blue_scale: A number to multiply each pixels' blue component by
    :return: the newly generated patch
    '''
    patch = SimpleImage(PATCH_NAME)
    # Adding the scale for each pixel
    for pixel in patch:
        pixel.red *= red_scale
        pixel.green *= green_scale
        pixel.blue *= blue_scale
    return patch


if __name__ == '__main__':
    main()