from numpy import array
from numpy import random
from numpy import lexsort


def sort_info(ides: array, heights: array) -> array:
    """
    The function finds the sorted id's indexes with increasing heights from given ides array and heights array.
    Then it prints the results.
    :param ides: The array of the ides.
    :param heights: The array of the heights.
    :return: None
    """
    print(lexsort((ides, heights)))


if __name__ == "__main__":
    students_ides = random.randint(low=999999, high=10000000, size=10)
    students_heights = (210 - 155) * random.random_sample(10) + 155
    print("students ides: ", students_ides, "\nstudents heights: ", students_heights, "\n")
    print("sorted indexes: \n")
    sort_info(students_ides, students_heights)