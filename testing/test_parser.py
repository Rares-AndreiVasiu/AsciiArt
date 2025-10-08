import sys
import pytest

from src.parser import get_args

def test_positional_argument():
    args = get_args(["woods.jpg"])

    assert args.image_path == ["woods.jpg"]

    assert args.filter == "luminosity"

    assert args.bgcolor == "#000000"

    assert args.fgcolor == "#FFFFFF"

    assert args.style == "bold"

    assert args.debug == 0

    assert args.outfile == sys.stdout


def test_filter_average_argument():
    args = get_args(["woods.jpg", "--filter", "average"])

    assert args.filter == "average"


def test_filter_lightness_argument():
    args = get_args(["woods.jpg", "--filter", "lightness"])

    assert args.filter == "lightness"


def test_filter_luminosity_argument():
    args = get_args(["woods.jpg", "--filter", "luminosity"])

    assert args.filter == "luminosity"

def test_fg_and_bg_colors_arguments():
    args = get_args(["woods.jpg", "--bgcolor", "#FFD44C", "--fgcolor", "#FFD44C"])

    assert args.bgcolor == "#FFD44C"

    assert args.fgcolor == "#FFD44C"


def test_debug_flag_default_and_const_argument():
    args = get_args(["woods.png"])

    assert args.debug == 0

    args = get_args(["img.png", "--debug"])

    assert args.debug == 1

    args = get_args(["img.png", "--debug", "2"])

    assert args.debug == 2


def test_invalid_filter_argument():
    with pytest.raises(SystemExit):
        get_args(["woods.jpg", "--filter", "big_man"])

def test_style_argument():
    args = get_args(["woods.jpg", "--style", "bold"])

    assert args.style == "bold"

    args = get_args(["woods.jpg", "--style", "italic"])

    assert args.style == "italic"

    args = get_args(["woods.jpg", "--style", "underline"])

    assert args.style == "underline"

def test_invalid_style_argument():
    with pytest.raises(SystemExit):
        get_args(["woods.jpg", "--style", "mici"])