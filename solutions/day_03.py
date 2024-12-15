from .types import SolutionClass
from typing import List, Optional, Pattern
import re


class Day03Solution(SolutionClass[List[str], int]):
    data: List[str]

    def __init__(self, path: Optional[str] = None):
        super()
        if path:
            self.data = self.import_from_file(path)

    @classmethod
    def import_from_file(self, path: str) -> List[str]:
        self.data = import_from_file(path)
        return self.data

    @classmethod
    def part_one(self):
        return find_valid_multiples(self.data)

    @classmethod
    def part_two(self, *args):
        raise NotImplementedError


def import_from_file(path: str) -> List[str]:
    with open(path, 'r') as file:
        return [line for line in file.readlines()]
    pass


def find_valid_multiples(data: List[str]) -> int:
    regex = r"mul\((-?\d+),\s*(-?\d+)\)"
    res = 0
    for line in data:
        for val1, val2 in re.findall(regex, line):
            res += int(val1) * int(val2)
    return res
