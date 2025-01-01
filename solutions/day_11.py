from .types import SolutionClass
from itertools import chain
from typing import List


class Solution(SolutionClass[List[int], int]):
    def __init__(self, path: str):
        super()
        self.import_from_file(path)

    @classmethod
    def import_from_file(self, path):
        self.data = import_from_file(path)
        return self.data

    @classmethod
    def part_one(self, n: int):
        return get_total_rocks(self.data, n)

    @classmethod
    def part_two(self, n: int):
        return get_total_rocks(self.data, n)


def import_from_file(path: str):
    with open(path) as file:
        return [int(word) for word in file.readline().split(" ")]


def memoize(func):
    memo = {}

    def _(*args):
        val, num = args
        if (val, num) in memo:
            return memo[(val, num)]
        memo[(val, num)] = func(*args)
        return memo[(val, num)]

    return _


def apply_rules(val: int):
    if val == 0:
        return [1]
    elif len(str(val)) % 2 == 0:
        s = str(val)
        left = int(s[: len(s) // 2])
        right = int(s[len(s) // 2:])
        return [left, right]
    return [val * 2024]


@memoize
def total_rocks(val: int, blinks: int):
    if blinks == 0:
        return 1
    if val == 0:
        return total_rocks(1, blinks - 1)
    elif len(str(val)) % 2 == 0:
        s = str(val)
        left = int(s[: len(s) // 2])
        right = int(s[len(s) // 2:])
        return total_rocks(left, blinks - 1) + total_rocks(right, blinks - 1)
    return total_rocks(val * 2024, blinks - 1)


def get_total_rocks(values: List[int], n: int) -> List[int]:
    total = 0
    for val in values:
        total += total_rocks(val, n)
    return total
