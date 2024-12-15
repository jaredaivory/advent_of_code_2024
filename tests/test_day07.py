from . import *
from solutions.day_07 import *
TEST_FILE = get_root_path().joinpath("data/example_day07.txt")


TEST_DATA = [
    (190, [10, 19]),
    (3267, [81, 40, 27]),
    (83, [17, 5]),
    (156, [15, 6]),
    (7290, [6, 8, 6, 15]),
    (161011, [16, 10, 13]),
    (192, [17, 8, 14]),
    (21037, [9, 7, 18, 13]),
    (292, [11, 6, 16, 20])
]


def test_import():
    assert TEST_DATA == import_from_file(TEST_FILE)


def test_total_calibration():
    def add(x, y): return x + y
    def mult(x, y): return x * y
    functions = [add, mult]
    assert 3749 == total_calibration(TEST_DATA, functions)
