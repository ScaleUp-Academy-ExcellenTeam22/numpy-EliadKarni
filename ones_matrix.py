from numpy import ones
from numpy import array


def ones_matrix() -> array:
    """
    The function creates a 10x10 matrix, in which the elements on its borders will be equal to 1, and its inside 0.
    :return: A 10x10 matrix, in which the elements on its borders will be equal to 1, and its inside 0.
    """
    ans = ones((10, 10))
    ans[1:-1, 1:-1] = 0
    return ans


if __name__ == "__main__":
    print(ones_matrix())
