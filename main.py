import os
import sys
import numpy as np
import pillow_heif
from pillow_heif import register_heif_opener
from PIL import Image
import argparse

from rgb_to_brightness import rgb_matrix_to_brightness_matrix
from brightness_to_ascii import brightness_matrix_to_ascii_matrix

register_heif_opener()

RESAMPLE = Image.Resampling.LANCZOS

def print_matrix(matrix, outfile=sys.stdout):
    for row in matrix:
        # scale horizontally by repeating chars
        line = [l + l + l for l in row]
        outfile.writelines("".join(line) + "\n")

    if outfile is not sys.stdout:
        outfile.flush()


def open_image(path: str) -> Image.Image:
    ext = os.path.splitext(path)[1].lower()

    try:
        img = Image.open(path)
        return img.convert("RGB")

    except Exception:
        if ext in [".heic", ".heif"]:
            if pillow_heif.is_supported(path):
                im = pillow_heif.open_heif(path, convert_hdr_to_8bit=False)

                return im.to_pillow().convert("RGB")
            else:
                raise ValueError("Unsupported HEIF format: " + path)
        else:
            raise


def get_args():
    parser = argparse.ArgumentParser(
        prog="main",
        description="An image to ascii art convertor",
        usage="%(prog)s [options]",
        epilog="And that is how ascii art was a long time ago",
        add_help=True
    )

    """
        input picture path
    """
    parser.add_argument("image_path",
                        nargs=1,
                        type=str,
                        help='path to the image to be converted (e.g. "bear.png")')

    """
        option for rgb conversion to brightness
    """
    parser.add_argument("--filter", "-f",
                        nargs="?",
                        default="average",
                        choices=["average", "lightness", "luminosity"],
                        type=str,
                        help="choose the rgb conversion algorithm to brightness")
    """
        option for output file
    """
    parser.add_argument("--outfile", "-o",
                        type=argparse.FileType("w"),
                        default=sys.stdout)

    return parser.parse_args()


def main():
    args = get_args()

    pil_image = open_image(args.image_path[0])

    max_width = 120

    aspect_ratio = 0.55

    new_height = int(max_width * pil_image.height / pil_image.width * aspect_ratio)

    pil_image = pil_image.resize((max_width, new_height), RESAMPLE)

    np_array = np.asarray(pil_image).astype(np.float64)

    brightness_matrix = rgb_matrix_to_brightness_matrix(np_array, args.filter)

    ascii_matrix = brightness_matrix_to_ascii_matrix(brightness_matrix)

    print_matrix(ascii_matrix, args.outfile)


if __name__ == "__main__":
    main()
