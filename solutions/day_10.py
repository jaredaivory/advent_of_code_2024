from .types import SolutionClass
from typing import List, Optional, Tuple, Set

Point = Tuple[int, int]
DIRECTIONS = [[0, 1], [0, -1], [1, 0], [-1, 0]]


class Solution(SolutionClass[List[List[int]], int]):

    def __init__(self, path: Optional[str] = None):
        super()
        if path:
            self.import_from_file(path)

    @classmethod
    def import_from_file(self, path):
        self.data = import_from_file(path)
        return self.data

    @classmethod
    def part_one(self, *args):
        trailheads = find_trailheads(self.data)
        return get_trailhead_scores_unique(trailheads, self.data)

    @classmethod
    def part_two(self, *args):
        trailheads = find_trailheads(self.data)
        return get_trailhead_scores(trailheads, self.data)


def import_from_file(path: str) -> List[List[int]]:
    with open(path, "r") as file:
        return [[int(c) for c in line.strip()] for line in file.readlines()]


def find_trailheads(map: List[List[int]]) -> List[Point]:
    ROWS, COLS = len(map), len(map[0])
    trailheads = []
    for row in range(ROWS):
        for col in range(COLS):
            if map[row][col] == 0:
                trailheads.append((row, col))
    return trailheads


def is_within_bounds(row: int, col: int, map: List[List[int]]):
    if 0 <= row < len(map) and 0 <= col < len(map[0]):
        return True
    return False


def trailhead_score_unique(row: int, col: int, map: List[List[int]]):
    visited = set()

    def dfs(row: int, col: int, map: List[List[int]], current_point: int = 0):
        if current_point == 9 and (row, col) not in visited:
            visited.add((row, col))
            return 1
        total_points = 0
        for dR, dC in DIRECTIONS:
            if (
                is_within_bounds(row + dR, col + dC, map)
                and map[row + dR][col + dC] == current_point + 1
            ):
                total_points += dfs(row + dR, col + dC, map, current_point + 1)
        return total_points

    return dfs(row, col, map)


def trailhead_score(row: int, col: int, map: List[List[int]], current_point: int = 0):
    def dfs(row: int, col: int, map: List[List[int]], current_point: int = 0):
        if current_point == 9:
            return 1
        total_points = 0
        for dR, dC in DIRECTIONS:
            if (
                is_within_bounds(row + dR, col + dC, map)
                and map[row + dR][col + dC] == current_point + 1
            ):
                total_points += dfs(row + dR, col + dC, map, current_point + 1)
        return total_points

    return dfs(row, col, map)


def get_trailhead_scores_unique(trailheads: List[Point], map: List[List[int]]):
    trailhead_points = {}
    for trailhead in trailheads:
        trailhead_points[trailhead] = trailhead_score_unique(
            trailhead[0], trailhead[1], map
        )
    return sum(trailhead_points.values())


def get_trailhead_scores(trailheads: List[Point], map: List[List[int]]):
    total_score = 0
    for trailhead in trailheads:
        total_score += trailhead_score(trailhead[0], trailhead[1], map)
    return total_score
