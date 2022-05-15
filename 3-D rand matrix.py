from numpy import array
from numpy import random
from numpy import uint8


def random_array(shape: tuple = (300, 400, 5)) -> array:
    """
    The function creates a three-dimension array with shape (300,400,5) by default.
    Then, it fills the array elements with values using unsigned integer (0 to 255).
    :param shape: The wanted matrix shape.
    :return: A three-dimension array with shape (300,400,5) by default.
    Then, it fills the array elements with values using unsigned integer (0 to 255).
    """
    return random.randint(low=0, high=256, size=shape, dtype=uint8)


if __name__ == "__main__":
    print("rand matrix received:\n", random_array())
