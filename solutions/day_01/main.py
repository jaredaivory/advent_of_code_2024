
from collections import Counter
from typing import List, Tuple
import heapq


def import_input(path: str) -> Tuple[List[int], List[int]]:
    with open(path, 'r') as file:
        arr_0, arr_1 = [list(arr) for arr in zip(
            *[[int(num) for num in line.split()] for line in file.readlines()])]
        return (arr_0, arr_1)
    pass


class PartOneSolution:
    def solve(arr1: List[int], arr2: List[int]) -> int:
        heapq.heapify(arr1)
        heapq.heapify(arr2)

        total_distance = 0
        while arr1:
            total_distance += abs(heapq.heappop(arr1) - heapq.heappop(arr2))
        return total_distance


class PartTwoSolution:
    def solve(arr1: List[int], arr2: List[int]) -> int:
        location_id_count = Counter(arr2)

        similarity_score = 0

        for location_id in arr1:
            similarity_score += location_id_count[location_id] * \
                location_id if location_id in location_id_count else 0

        return similarity_score


if __name__ == "__main__":
    arr1, arr2 = import_input('puzzle_input.txt')
    print(
        f"Day 01 | Part One - Solution: {PartOneSolution.solve(arr1[::], arr2[::])}")
    print(
        f"Day 02 | Part Two - Solution: {PartTwoSolution.solve(arr1[::], arr2[::])}")
