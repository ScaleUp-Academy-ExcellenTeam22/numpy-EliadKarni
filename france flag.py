from numpy import array
from numpy import ones
from matplotlib.pyplot import imsave


def get_france_flag_matrix() -> array:
    """
    The function returns a 3-D matrix (600, 900, 3) shape, which contains 600x900 pixels array that draws
    France flag.
    :return: A 3-D matrix that draws a France flag.
    """
    img = ones((600, 900, 3))
    img[:, 600:] = [1, 0, 0]
    img[:, :300] = [0, 0, 1]
    return img


if __name__ == "__main__":
    imsave("france flag.png", get_france_flag_matrix())
