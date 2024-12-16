from collections import Counter
from solutions.types import SolutionClass
from typing import List, Tuple, Optional
import heapq


class Solution(SolutionClass[Tuple[List[int], List[int]], int]):
    data: Tuple[List[int], List[int]]

    def __init__(self, path: Optional[str] = None):
        super()
        if path:
            self.data = self.import_from_file(path)

    @classmethod
    def import_from_file(self, path):
        with open(path, 'r') as file:
            arr_1, arr_2 = [list(arr) for arr in zip(
                *[[int(num) for num in line.split()] for line in file.readlines()])]
            self.data = (arr_1, arr_2)
            return self.data

    @classmethod
    def part_one(self):
        arr1 = self.data[0][::]
        arr2 = self.data[1][::]

        return total_distance_between_lists(arr1, arr2)

    @classmethod
    def part_two(self):
        return similarity_score(self.data[0], self.data[1])


def total_distance_between_lists(arr1: List[int], arr2: List[int]) -> int:
    heapq.heapify(arr1)
    heapq.heapify(arr2)

    total_distance = 0
    while arr2:
        total_distance += abs(heapq.heappop(arr1) -
                              heapq.heappop(arr2))
    return total_distance


def similarity_score(arr1: List[int], arr2: List[int]) -> int:
    location_id_count = Counter(arr1)

    similarity_score = 0

    for location_id in arr2:
        similarity_score += location_id_count[location_id] * \
            location_id if location_id in location_id_count else 0

    return similarity_score
