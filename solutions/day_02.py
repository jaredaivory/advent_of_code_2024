from .types import SolutionClass
from typing import List, Optional


class Solution(SolutionClass[List[List[int]], int]):
    data: List[List[int]]

    def __init__(self, path: Optional[str] = None):
        if path:
            self.data = self.import_from_file(path)

    @classmethod
    def import_from_file(self, path: str) -> List[List[int]]:
        self.data = import_from_file(path)
        return self.data

    @classmethod
    def part_one(self, min_change: int, max_change: int) -> int:
        return find_safe_reports(self.data, min_change, max_change)

    @classmethod
    def part_two(self, *args):
        raise NotImplementedError

    pass


def import_from_file(path: str) -> List[List[int]]:
    with open(path, "r") as file:
        return [[int(val) for val in line.split(" ")] for line in file.readlines()]


def is_increasing_arr(arr: List[int], min_change: int, max_change: int) -> bool:
    isIncreasing = (arr[1] - arr[0]) > 0
    for i in range(1, len(arr)):
        change = arr[i] - arr[i - 1]
        if not (min_change <= abs(change) <= max_change):
            return False
        if isIncreasing != (change > 0):
            return False
    return True


def find_safe_reports(
    reports: List[List[int]], min_change: int, max_change: int
) -> int:
    safe_reports = 0
    for report in reports:
        if is_increasing_arr(report, min_change, max_change):
            safe_reports += 1
    return safe_reports
