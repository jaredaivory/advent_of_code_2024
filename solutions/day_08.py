from .types import SolutionClass
from typing import List, Optional


class Solution(SolutionClass[List[List[str]], int]):
    data: List[List[str]]

    def __init__(self, path: Optional[str] = None):
        super()
        if path:
            self.data = self.import_from_file(path)

    @classmethod
    def import_from_file(self, path) -> List[List[str]]:
        self.data = import_from_file(path)
        return self.data

    @classmethod
    def part_one(self):
        ROWS, COLS = len(self.data), len(self.data[0])
        antennas = {}
        unique_annodes = set()
        for row in range(ROWS):
            for col in range(COLS):
                c = self.data[row][col]
                if c == ".":
                    continue
                if c not in antennas:
                    antennas[c] = []
                for pos in antennas[c]:
                    dR, dC = row - pos[0], col - pos[1]
                    if (0 <= row + dR < ROWS) and (0 <= col + dC < COLS):
                        unique_annodes.add((row + dR, col + dC))
                    if (0 <= pos[0] - dR < ROWS) and (0 <= pos[1] - dC < COLS):
                        unique_annodes.add((pos[0] - dR, pos[1] - dC))
                antennas[c].append((row, col))
        return len(unique_annodes)

    @classmethod
    def part_two(self):
        ROWS, COLS = len(self.data), len(self.data[0])
        antennas = {}
        unique_annodes = set()
        for row in range(ROWS):
            for col in range(COLS):
                c = self.data[row][col]
                if c == ".":
                    continue
                if c not in antennas:
                    antennas[c] = []
                for pos in antennas[c]:
                    unique_annodes.add((row, col))
                    unique_annodes.add((pos[0], pos[1]))
                    currRow = row
                    currCol = col
                    dR, dC = currRow - pos[0], currCol - pos[1]
                    while (0 <= currRow + dR < ROWS) and (0 <= currCol + dC < COLS):
                        unique_annodes.add((currRow + dR, currCol + dC))
                        currRow += dR
                        currCol += dC
                    currRow = pos[0]
                    currCol = pos[1]
                    while (0 <= currRow - dR < ROWS) and (0 <= currCol - dC < COLS):
                        unique_annodes.add((currRow - dR, currCol - dC))
                        currRow -= dR
                        currCol -= dC
                antennas[c].append((row, col))
        return len(unique_annodes)


def import_from_file(path) -> List[List[str]]:
    with open(path, 'r') as file:
        return [[c for c in line.strip()]
                for line in file.readlines()]
