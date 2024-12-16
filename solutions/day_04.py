
from typing import List
from .types import SolutionClass


DIRECTIONS = [(0, 1), (0, -1), (1, 0), (-1, 0),
              (1, 1), (1, -1), (-1, 1), (-1, -1)]


class Solution(SolutionClass[List[List[chr]], int]):
    data: List[List[chr]]

    @classmethod
    def import_from_file(self, path: str) -> List[List[chr]]:
        self.data = import_from_file(path)
        return self.data

    @classmethod
    def part_one(self):
        return find_word_count(self.data, "XMAS")

    @classmethod
    def part_two(self, *args):
        raise NotImplementedError


def import_from_file(path: str) -> List[List[chr]]:
    with open(path, 'r') as file:
        return [[c for c in line.strip()] for line in file.readlines()]
    pass


def find_word(row: int, col: int, word_search: List[List[chr]], word: str):
    found_words = 0
    for dR, dC in DIRECTIONS:
        currRow, currCol = row, col
        word_index = 0
        while 0 <= currRow < len(word_search) and 0 <= currCol < len(word_search):

            if word_search[currRow][currCol] != word[word_index]:
                break
            word_index += 1
            currRow += dR
            currCol += dC
            if word_index == len(word):
                found_words += 1
                break
    return found_words


def find_word_count(word_search: List[List[chr]], word: str) -> int:
    ROWS, COLS = len(word_search), len(word_search[0])

    word_count = 0

    for row in range(ROWS):
        for col in range(COLS):
            if word_search[row][col] == word[0]:
                word_count += find_word(row, col, word_search, word)

    return word_count
