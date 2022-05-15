from numpy import array
from numpy import eye


def diagonal_array(size: int = 3) -> array:
    """
    The function returns an diagonal matrix of the received size.
    :param size: The wanted diagonal matrix size.
    :return: Diagonal matrix of the received size.
    """
    return eye(size)


if __name__ == "__main__":
    print("Diagonal matrix of the size 3:\n", diagonal_array(3))

