
from typing import List, Tuple
import heapq


class PartOneSolution:

    def solve(arr1: List[int], arr2: List[int]) -> int:
        heapq.heapify(arr1)
        heapq.heapify(arr2)

        total_distance = 0
        while arr1:
            total_distance += abs(heapq.heappop(arr1) - heapq.heappop(arr2))
        return total_distance

    def import_input(path: str) -> Tuple[List[int], List[int]]:
        with open(path, 'r') as file:
            arr_0, arr_1 = [list(arr) for arr in zip(
                *[[int(num) for num in line.split()] for line in file.readlines()])]
            return (arr_0, arr_1)
        pass


if __name__ == "__main__":
    arr1, arr2 = PartOneSolution.import_input('puzzle_input.txt')
    print(PartOneSolution.solve(arr1, arr2))
