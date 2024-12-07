from typing import List, Tuple, Mapping, Set


def part_one_solve(ordering_rules: List[Tuple[int, int]], updates: List[List[int]]):
    ordering_hash_set: Mapping[int, Set[int]] = {}
    for frm, to in ordering_rules:
        if frm not in ordering_hash_set:
            ordering_hash_set[frm] = set()
        ordering_hash_set[frm].add(to)

    middle_summation = 0
    for update in updates:
        current_set = set()
        for val in update[::-1]:
            if val in current_set:
                break
            if val in ordering_hash_set:
                current_set |= ordering_hash_set[val]
            else:
                current_set.add(val)
        else:
            middle_summation += update[len(update)//2]
    return middle_summation


def import_input(path: str) -> Tuple[List[Tuple[int, int]], List[List[int]]]:
    with open(path, 'r') as file:
        raw_ordering_rules, raw_updates = file.read().split("\n\n")
        ordering_rules = [tuple([int(val) for val in tuple(line.split(
            "|"))])for line in raw_ordering_rules.split("\n")]
        updates = [[int(val) for val in line.split(",")]
                   for line in raw_updates.split("\n")]
        return (ordering_rules, updates)


if __name__ == "__main__":
    ordering_rules, updates = import_input("puzzle_input.txt")
    part_one_solution = part_one_solve(ordering_rules, updates)
    print(
        f"Day 01 | Part One - Solution: {part_one_solution}")
