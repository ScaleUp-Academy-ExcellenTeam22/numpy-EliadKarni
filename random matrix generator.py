from numpy import array
from numpy import random


def generate_rand_array() -> array:
    """
    The method generates an array 20 long with values between 0 - 20, and its values in the indexes 8 - 14 are
    negative numbers.
    :return: an array with values between 0 to 20, which its values between the indexes 8 - 14 are negative values.
    """
    arr = random.randint(20, size=20)
    arr[8:14] *= -1
    return arr


if __name__ == "__main__":
    print(generate_rand_array())
