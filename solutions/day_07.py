from typing import List, Tuple, Optional, Callable
from .types import SolutionClass


class Solution(SolutionClass[List[Tuple[int, List[int]]], int]):
    data: List[Tuple[int, List[int]]]

    def __init__(self, path: Optional[str] = None):
        super()
        if path:
            self.import_from_file(path)

    @classmethod
    def import_from_file(self, path: str) -> List[Tuple[int, List[int]]]:
        self.data = import_from_file(path)
        return self.data

    @classmethod
    def part_one(self):
        return

    @classmethod
    def part_two(self, *args):
        raise NotImplementedError


def import_from_file(path: str) -> List[Tuple[int, List[int]]]:
    with open(path, 'r') as file:
        res = []
        for line in file.readlines():
            val, expression = line.strip().split(":")
            res.append((int(val), [int(num)
                       for num in expression.strip().split()]))

        return res


def backtrack(result: int, values: List[int], functions: List[Callable], index: int = 0, current_value: int = 0) -> bool:
    if index == len(values):
        return current_value == result
    else:
        for func in functions:
            if backtrack(result, values, functions, index + 1, func(current_value, values[index])):
                return True
        # if backtrack(result, values, index + 1, current_value + values[index]):
        #     return True
        # if backtrack(result, values, index + 1, current_value * values[index]):
        #     return True
        # if backtrack(result, values, index + 1, int(str(current_value) + str(values[index]))):
        #     return True
    return False


def total_calibration(data: List[Tuple[int, List[int]]], functions: List[Callable[[int, int], int]]) -> int:
    x = 0
    for result, values in data:
        if backtrack(result, values, functions, 1, values[0]):
            x += result
    return x
