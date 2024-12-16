from solutions.day_05 import *
from . import *

TEST_FILE = get_root_path().joinpath("data/example_day05.txt")
TEST_PAGE_ORDERING_RULES = [
    (47, 53),
    (97, 13),
    (97, 61),
    (97, 47),
    (75, 29),
    (61, 13),
    (75, 53),
    (29, 13),
    (97, 29),
    (53, 29),
    (61, 53),
    (97, 53),
    (61, 29),
    (47, 13),
    (75, 47),
    (97, 75),
    (47, 61),
    (75, 61),
    (47, 29),
    (75, 13),
    (53, 13)]
TEST_UPDATES = [
    [75, 47, 61, 53, 29],
    [97, 61, 53, 29, 13],
    [75, 29, 13],
    [75, 97, 47, 61, 53],
    [61, 13, 29],
    [97, 13, 75, 29, 47],
]
TEST_ORDERING_HASH = {
    47: {53, 13, 61, 29},
    97: {13, 61, 47, 29, 53, 75},
    75: {29, 53, 47, 61, 13},
    61: {13, 53, 29},
    29: {13},
    53: {29, 13},
}

test_solution = Solution()


def test_import():
    page_ordering_rules, updates = import_from_file(TEST_FILE)
    assert TEST_PAGE_ORDERING_RULES == page_ordering_rules
    assert TEST_UPDATES == updates
    pass


def test_create_order_hash():
    assert TEST_ORDERING_HASH == create_order_hash(TEST_PAGE_ORDERING_RULES)


def test_is_correctly_ordered():
    bools = [True, True, True, False, False, False]
    for update, is_ordered in zip(TEST_UPDATES, bools):
        assert is_ordered == is_correctly_ordered(TEST_ORDERING_HASH, update)


def test_add_valid_updates():
    assert 143 == add_valid_updates(TEST_PAGE_ORDERING_RULES, TEST_UPDATES)
