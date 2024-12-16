from solutions import day_01
from . import *

TEST_FILE = get_root_path().joinpath("data/example_day01.txt")


test_solution = day_01.Solution()


def test_import():
    actual1 = [3, 4, 2, 1, 3, 3]
    actual2 = [4, 3, 5, 3, 9, 3]
    arr1, arr2 = test_solution.import_from_file(TEST_FILE)
    assert actual1 == arr1
    assert actual2 == arr2
    pass


def test_distance_between_lists():
    actual1 = [3, 4, 2, 1, 3, 3]
    actual2 = [4, 3, 5, 3, 9, 3]
    answer = 11
    assert answer == day_01.total_distance_between_lists(actual1, actual2)
    pass
