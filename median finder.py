from numpy import array
from numpy import median
from numpy import random


def get_median(arr: array) -> int:
    """
    The function returns the median of the received array.
    :param arr: The array which its median wanted.
    :return: The received array median.
    """
    return median(arr)


if __name__ == "__main__":
    example_arr = random.randint(200, size=10)
    print("The array: ", example_arr, "\nThe array median: ", get_median(example_arr))
