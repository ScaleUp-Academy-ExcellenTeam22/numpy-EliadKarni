from numpy import random
from numpy import array


def rand_array(size: int, max_value: int = 100) -> array:
    """
    The function generate a random array with size parameter's value rows and columns.
    :param size: The wanted array size.
    :param max_value: The array's max values.
    :return: Array with size parameter's rows and columns, that its values is no higher then max_value parameter's
             value.
    """
    return array([random.randint(max_value, size=size) for x in range(size)])


def swap_first_and_last_row(mat: array) -> array:
    """
    The function returns the received array's copy, with the first and the last rows swapped.
    :param mat: The copied array.
    :return: Mat parameter's copy with the first and last row copied.
    """
    temp = mat
    temp[[0, -1]] = temp[[-1, 0]]
    return temp


if __name__ == "__main__":
    matrix = rand_array(4)
    print("origin array:\n", matrix, "\n")
    print("array with first and last rows swapped:\n", swap_first_and_last_row(matrix), "\n")
