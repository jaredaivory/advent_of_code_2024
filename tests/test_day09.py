from . import *
from solutions.day_09 import *

TEST_FILE = get_root_path().joinpath("data/example_day09.txt")
TEST_DATA = "2333133121414131402"
TEST_MEMORY_BLOCK = [0, 0, None, None, None, 1, 1, 1, None, None, None, 2, None, None, None, 3, 3,
                     3, None, 4, 4, None, 5, 5, 5, 5, None, 6, 6, 6, 6, None, 7, 7, 7, None, 8, 8, 8, 8, 9, 9]
TEST_COMPACTED_MEMORY = [0, 0, 9, 9, 8, 1, 1, 1, 8, 8, 8,
                         2, 7, 7, 7, 3, 3, 3, 6, 4, 4, 6, 5, 5, 5, 5, 6, 6]


def test_import_from_file():
    assert TEST_DATA == import_from_file(TEST_FILE)


def test_diskmap_to_list():
    assert TEST_MEMORY_BLOCK == diskmap_to_list(TEST_DATA)
    assert [0, None, None, 1, 1, 1, None, None, None,
            None, 2, 2, 2, 2, 2] == diskmap_to_list("12345")


def test_compact_memory():
    assert TEST_COMPACTED_MEMORY == compact_memory(TEST_MEMORY_BLOCK[::])


def test_file_checksum():
    assert 1928 == file_checksum(TEST_COMPACTED_MEMORY)


def test_get_free_space():
    assert [(2, 5), (8, 11), (12, 15), (18, 19), (21, 22),
            (26, 27), (31, 32), (35, 36,)] == get_free_space(TEST_MEMORY_BLOCK)


def test_compact_memory_segments():
    test = TEST_MEMORY_BLOCK[::]
    assert [0, 0, 9, 9, 2, 1, 1, 1, 7, 7, 7, None, 4, 4, None, 3, 3, 3, None, None, None, None, 5, 5, 5, 5,
            None, 6, 6, 6, 6, None, None, None, None, None, 8, 8, 8, 8, None, None,] == compact_memory_segments(test)
