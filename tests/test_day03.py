from solutions.day_03 import *
from . import *


TEST_FILE = get_root_path().joinpath("data/example_day03.txt")
test_solution = Solution()


def test_import():
    actual = ["xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"]
    assert actual == import_from_file(TEST_FILE)
    pass


def test_find_valid_multiples():
    actual = ["xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"]
    result = 161

    assert result == find_valid_multiples(actual)
