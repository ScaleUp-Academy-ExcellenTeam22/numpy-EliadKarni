from numpy import array
from numpy import where
from numpy import random


def replace_equal(mat: array, compared_num: int, replacement: int) -> array:
    """
    The function returns an array's copy of the received mat parameter, which all its values that are equals to
    the received compared_num parameter, replaced by the received replacement parameter value.
    :param mat: The copied matrix.
    :param compared_num: The value compared to.
    :param replacement: The value replaced with.
    :return: A copy of the mat parameter which all its values that are equals to the compared parameter replaced by
             the received replacement value.
    """
    return where(mat == compared_num, replacement, mat)


def replace_lower(mat: array, compared_num: int, replacement: int) -> array:
    """
    The function returns an array's copy of the received mat parameter, which all its values that are lower then
    the received compared_num parameter, replaced by the received replacement parameter value.
    :param mat: The copied matrix.
    :param compared_num: The value compared to.
    :param replacement: The value replaced with.
    :return: A copy of the mat parameter which all its values that are lower then the compared parameter replaced by
             the received replacement value.
    """
    return where(mat < compared_num, replacement, mat)


def replace_higher(mat: array, compared_num: int, replacement: int) -> array:
    """
    The function returns an array's copy of the received mat parameter, which all its values that are higher then
    the received compared_num parameter, replaced by the received replacement parameter value.
    :param mat: The copied matrix.
    :param compared_num: The value compared to.
    :param replacement: The value replaced with.
    :return: A copy of the mat parameter which all its values that are higher then the compared parameter replaced by
             the received replacement value.
    """
    return where(mat > compared_num, replacement, mat)


if __name__ == "__main__":
    matrix = array([random.randint(10, size=10) for i in range(10)])
    print("base matrix:\n", matrix)
    print("Replaced values equals to: 5 with: -1:\n", replace_equal(matrix, 5, -1), "\n")
    print("Replaced values: lower then: 5 with: -1:\n", replace_lower(matrix, 5, -1), "\n")
    print("Replaced values higher then: 5 with: -1:\n", replace_higher(matrix, 5, -1), "\n")
