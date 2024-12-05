from typing import List
import re


def import_input(path: str) -> List[str]:
    with open(path, 'r') as file:
        return [line for line in file.readlines()]
    pass


def part_one_solve(data: List[str]) -> int:
    regex_match = r"mul\((-?\d+),\s*(-?\d+)\)"
    solution = 0
    for line in data:
        for val1, val2 in re.findall(regex_match, line):
            print(val1, val2)
            solution += int(val1) * int(val2)
    return solution


if __name__ == "__main__":
    data = import_input("puzzle_input.txt")
    print(data)
    part_one_solution = part_one_solve(data)
    print(
        f"Day 01 | Part One - Solution: {part_one_solution}")
