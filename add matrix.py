from numpy import array
from numpy import empty_like


def add_matrix(matrix: array, add_mat: array) -> array:
    """
    
    :param matrix:
    :param add_mat:
    :return:
    """
    ans = empty_like(matrix)
    for i in range(len(matrix)):
        ans[i, :] = matrix[i, :] + add_mat
    return ans


if __name__ == "__main__":
    print(add_matrix(array([[1, 2, 3], [7, 8, 9]]), array([1, 2, 3])))
