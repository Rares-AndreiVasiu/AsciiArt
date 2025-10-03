import numpy as np
import pytest

from brightness_to_ascii import brightness_to_ascii_pixel
from brightness_to_ascii import BRIGHTNESS_TO_ASCII_MAPPER
from brightness_to_ascii import brightness_matrix_to_ascii_matrix

def test_returns_single_character_for_valid_float_pixel():
    assert isinstance(brightness_to_ascii_pixel(255.0), str)

    assert len(brightness_to_ascii_pixel(255.0)) == 1

    assert brightness_to_ascii_pixel(255.0) in BRIGHTNESS_TO_ASCII_MAPPER


@pytest.mark.parametrize("val", [0.0, 1.0, 249.9, 255.0])
def test_bounds_pixel(val):
    assert isinstance(brightness_to_ascii_pixel(val), str)

    assert len(brightness_to_ascii_pixel(val)) == 1

    assert brightness_to_ascii_pixel(val) in BRIGHTNESS_TO_ASCII_MAPPER


@pytest.mark.parametrize("tmp", [None, ["banana"], {"monkey": 1}, ])
def test_invalid_input_pixel(tmp):
    with pytest.raises(TypeError):
        brightness_to_ascii_pixel(tmp)

def test_rounding_pixe_pixell():
    assert brightness_to_ascii_pixel(29.4) == brightness_to_ascii_pixel(round(29.4))
    assert brightness_to_ascii_pixel(49.9) == brightness_to_ascii_pixel(round(49.9))

def test_single_pixel_matrix():
    np.testing.assert_array_equal(brightness_matrix_to_ascii_matrix(np.array([ [0.0] ])), np.array([ ["`"] ]))

def test_full_matrix():
    np.testing.assert_array_equal(brightness_matrix_to_ascii_matrix(np.full((10, 10), 255)), np.full((10, 10), "$"))

    np.testing.assert_array_equal(brightness_matrix_to_ascii_matrix(np.full((10, 10), 255)), np.full((10, 10), "$"))
