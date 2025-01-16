from . import *
from solutions.day_13 import *

TEST_FILE = get_root_path().joinpath("data/example_day13.txt")
TEST_DATA = [((94, 34),
              (22, 67),
              (8400, 5400)),
             ((26, 66),
              (67, 21),
              (12748, 12176)),
             ((17, 86),
              (84, 37),
              (7870, 6450)),
             ((69, 23),
              (27, 71),
              (18641, 10279))]


def test_import_from_file():
    assert TEST_DATA == import_from_file(TEST_FILE)
    pass


def test_find_cheapest_win():
    TEST_RESULTS = [280, 0, 200, 0]
    for i in range(len(TEST_DATA)):
        assert TEST_RESULTS[i] == find_cheapest_win(TEST_DATA[i])


def test_total_cheapest_win():
    480 == total_cheapest_win(TEST_DATA)
