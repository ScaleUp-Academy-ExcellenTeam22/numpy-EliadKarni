from numpy import array
from numpy import multiply
from numpy import random


def multiply_matrix(left_matrix: array, right_matrix: array) -> array:
    """
    The function returns an array which is a multiplication between left_matrix and right_matrix parameters.
    :param left_matrix: The matrix which is the left matrix at the multiplication.
    :param right_matrix: The matrix which is the right matrix at the multiplication.
    :return: An array that is the multiplication of the left_matrix and right_matrix parameters.
    """
    return multiply(left_matrix, right_matrix)


if __name__ == "__main__":
    matrix1 = array([random.randint(10, size=10) for x in range(10)])
    matrix2 = array([random.randint(10, size=10) for x in range(10)])
    print("left matrix:\n", matrix1, "\nright matrix:\n", matrix2, "\nmultiplied matrix:\n",
          multiply_matrix(matrix1, matrix2))
