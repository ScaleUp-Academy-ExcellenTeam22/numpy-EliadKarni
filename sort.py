from numpy import array
from numpy import sort
from numpy import random


def array_sort(matrix: array, axis: int) -> array:
    """
    The function sorts an along the received axis of an array
    :param matrix: The array wanted to be sorted.
    :param axis: The axis wanted to be sorted along.
    :return: An array sorted along the received axis.
    """
    return sort(matrix, axis)


if __name__ == "__main__":
    example_matrix = array([random.randint(100, size=10) for x in range(10)])
    print("original matrix:\n", example_matrix)
    print("the matrix sorted by 1st axis:\n", array_sort(example_matrix, 0))
    print("the matrix sorted by 2nd axis:\n", array_sort(example_matrix, 1))
