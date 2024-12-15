from . import *
from solutions.day_10 import *

TEST_FILE = get_root_path().joinpath("data/example_day10.txt")
TEST_DATA = [[8, 9, 0, 1, 0, 1, 2, 3],
             [7, 8, 1, 2, 1, 8, 7, 4],
             [8, 7, 4, 3, 0, 9, 6, 5],
             [9, 6, 5, 4, 9, 8, 7, 4],
             [4, 5, 6, 7, 8, 9, 0, 3],
             [3, 2, 0, 1, 9, 0, 1, 2],
             [0, 1, 3, 2, 9, 8, 0, 1],
             [1, 0, 4, 5, 6, 7, 3, 2]]

TEST_TRAILHEADS = [(0, 2), (0, 4), (2, 4), (4, 6), (5, 2),
                   (5, 5), (6, 0), (6, 6), (7, 1)]


def test_import_from_file():
    assert TEST_DATA == import_from_file(TEST_FILE)


def test_find_trailheads():
    assert TEST_TRAILHEADS == find_trailheads(TEST_DATA)


def test_get_trailhead_scores():
    assert 36 == get_trailhead_scores(TEST_TRAILHEADS, TEST_DATA)
