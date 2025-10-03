import numpy as np

def rgb_to_average(pixel):
    return (pixel[0] + pixel[1] + pixel[2]) / 3

# lightness: [max(R, G, B) + min(R, G, B)] / 2
def rgb_to_lightness(pixel):
    return (max(pixel[0], pixel[1], pixel[2]) -
            min(pixel[0], pixel[1], pixel[2])) / 2

# luminosity: weighted average of RGB
def rgb_to_luminosity(pixel):
    return 0.21 * pixel[0] + 0.72 * pixel[1] + 0.07 * pixel[2]

def rgb_matrix_to_brightness_matrix(matrix, algorithm):
    h, w = matrix.shape[:2]

    # print(matrix.shape[:2])
    brightness_matrix = np.empty((h, w), dtype=np.float64)

    for i in range(h):
        for j in range(w):
            pixel = matrix[i, j]
            match algorithm:
                case "average":
                    brightness_matrix[i, j] = rgb_to_average(pixel)
                case "lightness":
                    brightness_matrix[i, j] = rgb_to_lightness(pixel)
                case "luminosity":
                    brightness_matrix[i, j] = rgb_to_luminosity(pixel)

    return brightness_matrix
