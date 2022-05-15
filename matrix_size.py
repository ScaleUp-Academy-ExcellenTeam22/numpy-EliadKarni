from numpy import shape
from numpy import array
from numpy import arange


def get_size(matrix: array) -> tuple:
    """
    The function finds the number of rows and columns of the given matrix.
    :param matrix: The matrix which wanted to find its number of rows and columns.
    :return: The number of rows and columns of the given matrix.
    """
    return shape(matrix)


if __name__ == "__main__":
    print(get_size(arange(0, 100).reshape(5, 20)))
