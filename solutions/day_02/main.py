from typing import List


def import_input(path: str) -> List[List[int]]:
    with open(path, 'r') as file:
        return [[int(val) for val in line.split(" ")]
                for line in file.readlines()]


def is_increasing_arr(arr: List[int], min_change: int, max_change: int) -> bool:
    isIncreasing = (arr[1]-arr[0]) > 0
    for i in range(1, len(arr)):
        change = arr[i] - arr[i-1]
        if not (min_change <= abs(change) <= max_change):
            return False
        if isIncreasing != (change > 0):
            return False
    return True


def part_one_solve(reports: List[List[int]], min_change: int, max_change: int) -> int:
    safe_reports = 0
    for report in reports:
        if is_increasing_arr_pythonic(report, min_change, max_change):
            safe_reports += 1
    return safe_reports


if __name__ == "__main__":
    data = import_input("puzzle_input.txt")
    part_one_solution = part_one_solve(data, 1, 3)
    print(
        f"Day 01 | Part One - Solution: {part_one_solution}")
    pass
