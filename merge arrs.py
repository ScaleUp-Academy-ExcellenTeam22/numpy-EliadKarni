from numpy import array
from numpy import random
from numpy import dstack


def merge_array(arr1: array, arr2: array) -> array:
    """
    The function converts (in sequence depth wise (along third axis)),
    two 1-D arrays into a 2-D array.
    :param arr1: An 1-D array wanted to be converted.
    :param arr2: An 1-D array wanted to be converted.
    :return: 2-D array made of the 2 received 1-D array.
    """
    return dstack((arr1, arr2))


if __name__ == "__main__":
    array1 = random.randint(100, size=10)
    array2 = random.randint(100, size=10)
    print("arr1:", array1, "\n arr2: ", array2)
    print("\nmerged arrays:\n", merge_array(array1, array2))
