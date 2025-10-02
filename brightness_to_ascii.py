import sys

import numpy as np
BRIGHTNESS_TO_ASCII_MAPPER = ("`^\",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvcz"
                              "XYUJCLQ0OZmwqpdbkhao*#MW&8%B@$")

# BRIGHTNESS_TO_ASCII_MAPPER = " .-:*^x%X$"

# we have 65 characters which need to map 256 brightness levels
# brightness of 255 -> 65th character
# brigthness of 0 -> 0 character
# 255..................65
# rounded_val...........x
# x = rounded_val * 65 / 255
def brightness_to_ascii_pixel(brightness_pixel):
    try:
        val = float(brightness_pixel)
    except (TypeError, ValueError):
        raise TypeError("brightness_pixel must be a number")

    if not (0.0 <= val <= 255.0):
        raise ValueError("brightness_pixel must be included in range [0,255]")

    rounded_val = round(val)

    index = rounded_val * len(BRIGHTNESS_TO_ASCII_MAPPER) // 255
    if index:
        index -= 1

    index = max(0, min(index, len(BRIGHTNESS_TO_ASCII_MAPPER) - 1))

    return BRIGHTNESS_TO_ASCII_MAPPER[index]


def brightness_matrix_to_ascii_matrix(brightness_matrix):
    h, w = brightness_matrix.shape[:2]

    ascii_matrix = np.empty((h, w), dtype=np.dtype("<U1"))

    for i in range(len(brightness_matrix)):
        for j in range(len(brightness_matrix[i])):
            ascii_matrix[i][j] = brightness_to_ascii_pixel(brightness_matrix[i][j])
    return ascii_matrix


def main():
    print(brightness_to_ascii_pixel(255))
    print(brightness_to_ascii_pixel(0))
    print(brightness_to_ascii_pixel(180.9))

if __name__ == "__main__":
    main()