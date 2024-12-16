from solutions.day_02 import *
from . import *


TEST_FILE = get_root_path().joinpath("data/example_day02.txt")
test_solution = Solution()


def test_import():
    actual = [
        [7, 6, 4, 2, 1],
        [1, 2, 7, 8, 9],
        [9, 7, 6, 2, 1],
        [1, 3, 2, 4, 5],
        [8, 6, 4, 4, 1],
        [1, 3, 6, 7, 9],
    ]
    assert actual == import_from_file(TEST_FILE)
    pass


def test_is_increasing_arr():
    data = [([1, 2, 3, 4, 5], True), ([5, 4, 3, 2, 1], True), ([1, 2, 5, 4, 3], False)]
    for arr, isIncreasing in data:
        assert isIncreasing == is_increasing_arr(arr, 1, 3)
    pass


def test_find_safe_reports():
    reports = [
        [7, 6, 4, 2, 1],
        [1, 2, 7, 8, 9],
        [9, 7, 6, 2, 1],
        [1, 3, 2, 4, 5],
        [8, 6, 4, 4, 1],
        [1, 3, 6, 7, 9],
    ]
    assert 2 == find_safe_reports(reports, 1, 3)
