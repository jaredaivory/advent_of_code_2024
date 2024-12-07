from typing import List, Tuple, Optional


def import_input(path: str) -> List[List[chr]]:
    with open(path, 'r') as file:
        return [[c for c in line.strip()] for line in file.readlines()]


def get_starting_point(grid: List[List[chr]], key: chr) -> Optional[Tuple[int, int]]:
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == key:
                return (row, col)
    raise KeyError(key)


UP = (-1, 0)
RIGHT = (0, 1)
DOWN = (1, 0)
LEFT = (0, -1)
directions = [UP, RIGHT, DOWN, LEFT]


def is_within_bounds(grid: List[List[chr]], row: int, col: int) -> bool:
    if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]):
        return False
    return True


def part_one_solve(grid: List[List[chr]], row: int, col: int) -> int:
    positions = set()
    positions.add((row, col))
    grid[row][col] = "."
    direction = 0
    while is_within_bounds(grid, row, col):
        dR, dC = directions[direction]
        if not is_within_bounds(grid, row + dR, col + dC):
            break
        if grid[row + dR][col + dC] == '.':
            row += dR
            col += dC
            positions.add((row, col))
        else:
            direction = (direction + 1) % 4

    return len(positions)


if __name__ == "__main__":
    grid = import_input("puzzle_input.txt")
    starting_row, starting_col = get_starting_point(grid, '^')
    part_one_solution = part_one_solve(grid, starting_row, starting_col)
    print(
        f"Day 01 | Part One - Solution: {part_one_solution}")
