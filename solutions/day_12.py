from .types import SolutionClass
from typing import List, Tuple, Set, Optional


class Solution(SolutionClass[List[List[str]], int]):
    def __init__(self, path: str):
        super()
        self.import_from_file(path)

    @classmethod
    def import_from_file(self, path):
        self.data = import_from_file(path)
        return self.data

    @classmethod
    def part_one(self):
        return calculate_fence_pricing(self.data)

    @classmethod
    def part_two(self, n: int):
        pass


def import_from_file(path: str):
    with open(path) as file:
        return [int(word) for word in file.readline().split(" ")]


UP = (-1, 0)
RIGHT = (0, 1)
DOWN = (1, 0)
LEFT = (0, -1)
DIRECTIONS = [UP, RIGHT, DOWN, LEFT]


def import_from_file(path: str) -> List[List[chr]]:
    with open(path) as file:
        return [[char for char in line.strip()] for line in file.readlines()]


def is_within_bounds(row: int, col: int, matrix: List[List[chr]]) -> bool:
    if 0 <= row < len(matrix) and 0 <= col < len(matrix[0]):
        return True
    return False


def get_zones(
    matrix: List[List[chr]], func: Optional[callable] = None
) -> List[Tuple[chr, int, int]]:
    if not func:
        func = get_area_perimeter
    visited = set()
    zones = []
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if (row, col) not in visited:
                zone = func(row, col, matrix, visited)
                zones.append((matrix[row][col], *zone))
    return zones


def calculate_fence_pricing(matrix: List[List[chr]]) -> int:
    zones = get_zones(matrix)
    return sum([area * mult for _, area, mult in zones])


def get_area_perimeter(
    row: int, col: int, matrix: List[List[chr]], visited: Set[Tuple[int, int]]
) -> Tuple[int, int]:
    visited.add((row, col))
    area = 1
    perimeter = 4
    for dR, dC in DIRECTIONS:
        if (
            is_within_bounds(row + dR, col + dC, matrix)
            and matrix[row][col] == matrix[row + dR][col + dC]
        ):
            if (row + dR, col + dC) in visited:
                perimeter -= 1
            else:
                perimeter -= 1  # Perimeter has an opening
                zone = get_area_perimeter(row + dR, col + dC, matrix, visited)
                area += zone[0]
                perimeter += zone[1]

    return (area, perimeter)


def get_area_sides(
    row: int, col: int, matrix: List[List[chr]], visited: Set[Tuple[int, int]]
) -> Tuple[int, int]:
    visited.add((row, col))
    area = 1
    for dR, dC in DIRECTIONS:
        if (
            is_within_bounds(row + dR, col + dC, matrix)
            and matrix[row][col] == matrix[row + dR][col + dC]
        ):
            if (row + dR, col + dC) in visited:
                perimeter -= 1
            else:
                perimeter -= 1  # Perimeter has an opening
                zone = get_area_perimeter(row + dR, col + dC, matrix, visited)
                area += zone[0]
                perimeter += zone[1]

    return (area, perimeter)


def calculate_fence_pricing_with_sides(matrix: List[List[chr]]) -> int:
    zones = get_zones(matrix, get_area_sides)
