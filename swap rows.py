from numpy import arange
from numpy import array


def get_rand_matrix_4x4() -> array:
    return arange(16).reshape(-1, 4)


def swap_last_and_first_row(matrix: array) -> array:
    return matrix[::-1]


if __name__ == "__main__":
    mat = get_rand_matrix_4x4()
    print(mat, "\n")
    print(swap_last_and_first_row(mat))
