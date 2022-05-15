import numpy as np


def evenly_distributed_vector():
    """
    The function creates a vector of length 10, with values evenly distributed between 5 and 50.
    :return: A vector of length 10, with values evenly distributed between 5 and 50.
    """
    return np.linspace(10, 49, 5)


if __name__ == "__main__":
    print(evenly_distributed_vector())
