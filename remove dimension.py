from numpy import squeeze
from numpy import array
from numpy import random


def remove_dimensional(mat: array) -> array:
    """
    The function returns mat parameter's removed single-dimensional entries from a specified shape.
    :param mat: The entries matrix.
    :return: The mat parameter's removed single-dimensional entries from a specified shape.
    """
    return squeeze(mat).shape


if __name__ == "__main__":
    matrix = random.randint(100, size=3)
    print("base matrix:\n", matrix)
    print("squeezed matrix:\n", remove_dimensional(matrix))
