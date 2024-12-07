from typing import List, Tuple


def import_input(path: str) -> List[Tuple[int, List[int]]]:
    with open(path, 'r') as file:
        res = []
        for line in file.readlines():
            val, expression = line.strip().split(":")
            res.append((int(val), [int(num)
                       for num in expression.strip().split()]))

        return res


def backtrack(result: int, values: List[int], index: int = 0, current_value: int = 0) -> bool:
    if index == len(values):
        return current_value == result
    else:
        if backtrack(result, values, index + 1, current_value + values[index]):
            return True
        if backtrack(result, values, index + 1, current_value * values[index]):
            return True
    return False


def part_one_solve(data: List[Tuple[int, List[int]]]) -> int:
    x = 0
    for result, values in data:
        if backtrack(result, values, 1, values[0]):
            x += result
    return x


if __name__ == "__main__":
    data = import_input("puzzle_input.txt")
    result = part_one_solve(data)
    print(result)
