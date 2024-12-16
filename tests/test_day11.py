from . import *
from solutions.day_11 import *

TEST_FILE = get_root_path().joinpath("data/example_day11.txt")
TEST_DATA = [[125, 17],
             [253000, 1, 7],
             [253, 0, 2024, 14168],
             [512072, 1, 20, 24, 28676032],
             [512, 72, 2024, 2, 0, 2, 4, 2867, 6032],
             [1036288, 7, 2, 20, 24, 4048, 1, 4048, 8096, 28, 67, 60, 32],
             [2097446912, 14168, 4048, 2, 0, 2, 4, 40, 48, 2024, 40, 48, 80, 96, 2, 8, 6, 7, 6, 0, 3, 2]]


def test_import_from_file():
    assert TEST_DATA[0] == import_from_file(TEST_FILE)


def test_apply_rules():
    # 0 1 10 99 999 => 1 2024 1 0 9 9 2021976
    assert [1] == apply_rules(0)
    assert [2024] == apply_rules(1)
    assert [1, 0] == apply_rules(10)
    assert [9, 9] == apply_rules(99)
    assert [2021976] == apply_rules(999)
