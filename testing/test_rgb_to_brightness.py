import numpy as np
import pytest

from src.rgb_to_brightness import rgb_to_average
from src.rgb_to_brightness import rgb_to_lightness
from src.rgb_to_brightness import rgb_to_luminosity
from src.rgb_to_brightness import rgb_matrix_to_brightness_matrix

@pytest.fixture
def sample_pixels():
    return {
        "black": np.array([0, 0, 0]),

        "white": np.array([255, 255, 255]),

        "red": np.array([255, 0, 0]),

        "green": np.array([0, 255, 0]),

        "blue": np.array([0, 0, 255]),

        "gray": np.array([128, 128, 128]),

        "mixed": np.array([100, 150, 200]),
    }


def test_rgb_to_average(sample_pixels):
    assert rgb_to_average(sample_pixels["black"]) == 0

    assert rgb_to_average(sample_pixels["white"]) == 255

    assert rgb_to_average(sample_pixels["gray"]) == 128

    assert rgb_to_average(sample_pixels["red"]) == pytest.approx(85.0, rel=1e-2)

    assert rgb_to_average(sample_pixels["mixed"]) == pytest.approx((100 + 150 + 200) / 3)


def test_rgb_to_lightness(sample_pixels):
    assert rgb_to_lightness(sample_pixels["black"]) == 0

    assert rgb_to_lightness(sample_pixels["white"]) == 0

    assert rgb_to_lightness(sample_pixels["red"]) == pytest.approx(127.5)

    assert rgb_to_lightness(sample_pixels["gray"]) == 0

    assert rgb_to_lightness(sample_pixels["mixed"]) == pytest.approx((200 - 100) / 2)


def test_rgb_to_luminosity(sample_pixels):
    assert rgb_to_luminosity(sample_pixels["black"]) == 0

    assert rgb_to_luminosity(sample_pixels["white"]) == pytest.approx(0.21 * 255 + 0.72 * 255 + 0.07 * 255)

    lum_red = rgb_to_luminosity(sample_pixels["red"])

    lum_green = rgb_to_luminosity(sample_pixels["green"])

    lum_blue = rgb_to_luminosity(sample_pixels["blue"])

    assert lum_green > lum_red > lum_blue

    assert (rgb_to_luminosity(sample_pixels["mixed"]) ==
            pytest.approx(0.21 * sample_pixels["mixed"][0] + 0.72 * sample_pixels["mixed"][1] + 0.07 * sample_pixels["mixed"][2]))

def test_rgb_matrix_to_brightness_matrix_average():
    # Use small, exact integer values that divide cleanly by 3
    mat = np.array([
        [[0, 0, 0], [30, 60, 90]],
        [[100, 200, 250], [10, 40, 70]]
    ], dtype=np.float64)

    result = rgb_matrix_to_brightness_matrix(mat, "average")

    expected = np.array([
        [(0 + 0 + 0) / 3, (30 + 60 + 90) / 3],
        [(100 + 200 + 250) / 3, (10 + 40 + 70) / 3]
    ], dtype=float)

    np.testing.assert_allclose(result, expected, rtol=1e-5)


def test_rgb_matrix_to_brightness_matrix_lightness():
    mat = np.array([
        [[10, 20, 30], [100, 50, 200]],
        [[255, 255, 255], [0, 0, 0]]
    ], dtype=np.uint8)

    result = rgb_matrix_to_brightness_matrix(mat, "lightness")

    expected = np.array([
        [(30 - 10) / 2, (200 - 50) / 2],
        [(255 - 255) / 2, (0 - 0) / 2]
    ])
    np.testing.assert_allclose(result, expected, rtol=1e-5)


def test_rgb_matrix_to_brightness_matrix_luminosity():
    mat = np.array([
        [[100, 150, 200]],
        [[50, 100, 150]]
    ], dtype=np.uint8)

    result = rgb_matrix_to_brightness_matrix(mat, "luminosity")

    expected = np.array([
        [0.21 * 100 + 0.72 * 150 + 0.07 * 200],
        [0.21 * 50 + 0.72 * 100 + 0.07 * 150]
    ])
    np.testing.assert_allclose(result, expected, rtol=1e-5)


def test_matrix_shape_and_dtype():
    mat = np.random.randint(0, 256, (5, 5, 3), dtype=np.uint8)
    for algo in ["average", "lightness", "luminosity"]:
        result = rgb_matrix_to_brightness_matrix(mat, algo)
        assert result.shape == (5, 5)

        assert result.dtype == np.float64


def test_random_matrix_consistency():
    np.random.seed(0)

    mat = np.random.randint(0, 256, (10, 10, 3), dtype=np.uint8)

    result_avg = rgb_matrix_to_brightness_matrix(mat, "average")

    result_light = rgb_matrix_to_brightness_matrix(mat, "lightness")

    result_lum = rgb_matrix_to_brightness_matrix(mat, "luminosity")

    assert not np.allclose(result_avg, result_light)

    assert not np.allclose(result_avg, result_lum)

    assert not np.allclose(result_light, result_lum)


def test_invalid_algorithm():
    mat = np.zeros((2, 2, 3), dtype=np.uint8)

    with pytest.raises(ValueError):
        rgb_matrix_to_brightness_matrix(mat, "excalibur")