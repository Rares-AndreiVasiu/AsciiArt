import numpy as np
brightness_to_ascii_mapper = ("`^\",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvcz"
                              "XYUJCLQ0OZmwqpdbkhao*#MW&8%B@$")

# we have 65 characters which need to map 256 brightness levels
# brightness of 255 -> 65th character
# brigthness of 0 -> 0 character
# 255..................65
# rounded_val...........x
# x = rounded_val * 65 / 255
def brightness_to_ascii_pixel(brightness_pixel):
    rounded_val = round(brightness_pixel)

    index = rounded_val * 65 // 255

    if index:
        index -= 1

    return brightness_to_ascii_mapper[index]


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