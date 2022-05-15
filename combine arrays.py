from numpy import array
from numpy import random
from numpy import nditer


def combination(one_dimension_matrix: array, two_dimension_matrix: array) -> None:
    """
    The function combines a one and a two dimensional arrays together and display their elements.
    :param one_dimension_matrix: A one dimension array.
    :param two_dimension_matrix:A two dimension array.
    :return: None
    """
    for one_dimension_value, two_dimension_value in nditer([one_dimension_matrix, two_dimension_matrix]):
        print("%d:%d" % (one_dimension_value, two_dimension_value))


if __name__ == "__main__":
    one_dimension_array = random.randint(100, size=3)
    two_dimension_array = array([random.randint(100, size=3) for i in range(2)])
    print("One dimension arr:\n", one_dimension_array)
    print("Two dimension arr:\n", two_dimension_array)
    print("combination:")
    combination(one_dimension_array, two_dimension_array)
