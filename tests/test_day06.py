from . import *
from solutions.day_06 import *

TEST_FILE = get_root_path().joinpath("data/example_day06.txt")
test_solution = Solution()


TEST_GRID = [
    ['.', '.', '.', '.', '#', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.', '#'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '#', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '#', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '#', '.', '.', '^', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '#', '.'],
    ['#', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '#', '.', '.', '.'],
]


def test_import():
    assert TEST_GRID == import_from_file(TEST_FILE)


def test_get_starting_point():
    assert (6, 4) == get_starting_point(TEST_GRID, '^')


def test_number_of_unique_positions():
    assert 41 == number_of_unique_positions(TEST_GRID, 6, 4)
