from solutions.day_04 import *
from . import *

TEST_FILE = get_root_path().joinpath("data/example_day04.txt")
TEST_DATA = [['M', 'M', 'M', 'S', 'X', 'X', 'M', 'A', 'S', 'M'],
             ['M', 'S', 'A', 'M', 'X', 'M', 'S', 'M', 'S', 'A'],
             ['A', 'M', 'X', 'S', 'X', 'M', 'A', 'A', 'M', 'M'],
             ['M', 'S', 'A', 'M', 'A', 'S', 'M', 'S', 'M', 'X'],
             ['X', 'M', 'A', 'S', 'A', 'M', 'X', 'A', 'M', 'M'],
             ['X', 'X', 'A', 'M', 'M', 'X', 'X', 'A', 'M', 'A'],
             ['S', 'M', 'S', 'M', 'S', 'A', 'S', 'X', 'S', 'S'],
             ['S', 'A', 'X', 'A', 'M', 'A', 'S', 'A', 'A', 'A'],
             ['M', 'A', 'M', 'M', 'M', 'X', 'M', 'M', 'M', 'M'],
             ['M', 'X', 'M', 'X', 'A', 'X', 'M', 'A', 'S', 'X']]


test_solution = Day04Solution()


def test_import():
    assert TEST_DATA == import_from_file(TEST_FILE)
    pass


def test_find_words():
    positions = [(2, (3, 9)), (1, (0, 5)), (0, (0, 0))]
    for count, (row, col) in positions:
        assert count == find_word(row, col, TEST_DATA, "XMAS")
    pass


def test_find_word_count():
    assert 18 == find_word_count(TEST_DATA, "XMAS")
