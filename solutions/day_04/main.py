
from typing import List


def import_input(path: str) -> List[List[chr]]:
    with open(path, 'r') as file:
        return [[c for c in line.strip()] for line in file.readlines()]
    pass


directions = [(0, 1), (0, -1), (1, 0), (-1, 0),
              (1, 1), (1, -1), (-1, 1), (-1, -1)]


def find_word(row: int, col: int, word_search: List[List[chr]], word: str):
    found_words = 0
    for dR, dC in directions:
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


def part_one_solve(word_search: List[List[chr]], word: str) -> int:
    ROWS, COLS = len(word_search), len(word_search[0])

    word_count = 0

    for row in range(ROWS):
        for col in range(COLS):
            if word_search[row][col] == word[0]:
                word_count += find_word(row, col, word_search, word)

    return word_count


if __name__ == "__main__":
    data = import_input("puzzle_input.txt")
    part_one_solution = part_one_solve(data, "XMAS")
    print(
        f"Day 01 | Part One - Solution: {part_one_solution}")
