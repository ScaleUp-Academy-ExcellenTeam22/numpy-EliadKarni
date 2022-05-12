from numpy import random
from numpy import array


def generate_random_array() -> array:
    """
    The function generates an array 20 long, with random values between 0 to 20.
    Then it changes the values in the 8-15 indexes to negative values.
    :return: Array 20 long, with values between 0 to 20, that its value in the 8 to 15 indexes are negative.
    """
    arr = random.randint(0, high=20, size=20)
    arr[8:15] *= -1
    return arr


if __name__ == "__main__":
    print(generate_random_array())
