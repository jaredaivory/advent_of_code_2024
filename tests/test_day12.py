from . import *
from solutions.day_12 import *

TEST_FILE = get_root_path().joinpath("data/example_day12.txt")
TEST_DATA = [["R", "R", "R", "R", "I", "I", "C", "C", "F", "F"],
             ["R", "R", "R", "R", "I", "I", "C", "C", "C", "F"],
             ["V", "V", "R", "R", "R", "C", "C", "F", "F", "F"],
             ["V", "V", "R", "C", "C", "C", "J", "F", "F", "F"],
             ["V", "V", "V", "V", "C", "J", "J", "C", "F", "E"],
             ["V", "V", "I", "V", "C", "C", "J", "J", "E", "E"],
             ["V", "V", "I", "I", "I", "C", "J", "J", "E", "E"],
             ["M", "I", "I", "I", "I", "I", "J", "J", "E", "E"],
             ["M", "I", "I", "I", "S", "I", "J", "E", "E", "E"],
             ["M", "M", "M", "I", "S", "S", "J", "E", "E", "E"]]


def test_import_from_file():
    assert TEST_DATA == import_from_file(TEST_FILE)


def test_calculate_fence_pricing():
    assert 1930 == calculate_fence_pricing(TEST_DATA)
