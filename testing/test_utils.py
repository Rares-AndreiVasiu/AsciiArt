import pytest
from src.utils import check_color
from src.utils import open_image
from src.utils import resize_image

from PIL import Image

def test_check_color():
    assert check_color("hey") == None
    assert check_color("#HAHAHA") == None
    assert check_color("#FFFFF") == None


def test_check_color_invalid_type():
    with pytest.raises(TypeError):
        check_color(29)


def test_open_image():
    img = open_image("testing/tree.png")

    assert isinstance(img, Image.Image)

    assert img.mode == "RGB"


def test_open_image_invalid():
    with pytest.raises(FileNotFoundError):
        open_image("Romania.jpg")


@pytest.mark.parametrize("size", [
    (240, 120),
    (300, 300),
    (600, 100),
])

def test_resize_image(size):
    img = Image.new("RGB", size, (255, 255, 255))

    resized = resize_image(img)

    # i've set a fixed width
    assert resized.width == 120

    assert int(120 * size[1] / size[0] *0.55) == resized.height

