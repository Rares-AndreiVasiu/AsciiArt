import argparse
import sys

def get_args(argv=None):
    parser = argparse.ArgumentParser(
        prog="main",
        description="An image to ascii art convertor",
        usage="%(prog)s [options]",
        allow_abbrev=True,
        epilog="And that is how ascii art was done a long time ago",
        add_help=True)

    """
        input picture path
    """
    parser.add_argument("image_path",
                        nargs=1,
                        type=str,
                        help='path to the image to be converted, e.g. "bear.png"',
                        metavar="")

    """
        option for rgb conversion to brightness
    """
    parser.add_argument("--filter",
                        nargs="?",
                        const="luminosity",
                        default="luminosity",
                        choices=["average", "lightness", "luminosity"],
                        type=str,
                        help="choose the rgb conversion algorithm to brightness")

    """
        option for background color ascii printing
    """
    parser.add_argument("--bgcolor",
                        nargs="?",
                        const="#000000",
                        default="#000000",
                        type=str,
                        help='Introduce a str hex html color code, e.g. "#FFFFFF"',
                        metavar="")

    """
                   option for foreground color ascii printing
    """
    parser.add_argument("--fgcolor",
                        nargs="?",
                        const="#FFFFFF",
                        default="#FFFFFF",
                        type=str,
                        help='Introduce a str hex html color code, e.g. "#FFFFFF"',
                        metavar="")

    """
        option for style
    """
    parser.add_argument("--style",
                        nargs="?",
                        const="bold",
                        default="bold",
                        choices=["bold", "italic", "underline"],
                        type=str,
                        help='Introduce a str style from the choices, e.g. "bold"')

    """
        option for output file
    """
    parser.add_argument("--outfile", "-o",
                        type=argparse.FileType("w"),
                        default=sys.stdout,
                        metavar="")

    """
        option for DEBUG
    """
    parser.add_argument("--debug",
                        help="Debug",
                        nargs='?',
                        type=int,
                        const=1,
                        default=0)

    return parser.parse_args(argv)

