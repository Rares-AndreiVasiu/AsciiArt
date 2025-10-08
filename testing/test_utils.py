import pytest
from src.utils import check_color

def test_check_color():
    assert check_color("hey") == None
    assert check_color("#HAHAHA") == None
    assert check_color("#FFFFF") == None


def test_check_color_invalid_type():
    with pytest.raises(TypeError):
        check_color(29)

