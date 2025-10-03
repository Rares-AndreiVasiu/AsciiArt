import sys
import numpy as np

from utils import check_color, open_image, resize_image
from brightness_to_ascii import brightness_matrix_to_ascii_matrix
from parser import get_args
from printing import print_matrix
from rgb_to_brightness import rgb_matrix_to_brightness_matrix

def ascii_art():
    args = get_args()

    if args.debug != 0:
        print(f"Command line arguments: {args}")

    if not check_color(args.bgcolor):
        sys.exit("Invalid background color format")

    if not check_color(args.fgcolor):
        sys.exit("Invalid foreground color format")

    pil_image = open_image(args.image_path[0])

    pil_image_resized = resize_image(pil_image)

    np_array = np.asarray(pil_image_resized).astype(np.float64)

    brightness_matrix = rgb_matrix_to_brightness_matrix(np_array, args.filter)

    ascii_matrix = brightness_matrix_to_ascii_matrix(brightness_matrix)

    if args.debug != 0:
        print(ascii_matrix, end="\n\n\n\n")

    print_matrix(ascii_matrix, args.fgcolor, args.bgcolor, args.style, args.outfile)
