from typing import List, Tuple, Mapping, Set, Optional
from .types import SolutionClass


class Day05Solution(SolutionClass[Tuple[List[Tuple[int, int]], List[List[int]]], int]):
    data: Tuple[List[Tuple[int, int]], List[List[int]]]

    def __init__(self, path: Optional[str] = None):
        super()
        if path:
            self.data = self.import_from_file(path)

    @classmethod
    def import_from_file(self, path: str):
        self.data = import_from_file(path)
        return self.data

    @classmethod
    def part_one(self):
        return add_valid_updates(self.data[0], self.data[1])

    @classmethod
    def part_two(self, *args):
        raise NotImplementedError


def create_order_hash(ordering_rules: List[Tuple[int, int]]) -> Mapping[int, Set[int]]:
    ordering_hash_set: Mapping[int, Set[int]] = {}
    for frm, to in ordering_rules:
        if frm not in ordering_hash_set:
            ordering_hash_set[frm] = set()
        ordering_hash_set[frm].add(to)
    return ordering_hash_set


def is_correctly_ordered(ordering_hash_set: Mapping[int, Set[int]], update: List[int]) -> bool:
    current_set = set()
    for val in update[::-1]:
        if val in current_set:
            break
        if val in ordering_hash_set:
            current_set |= ordering_hash_set[val]
        else:
            current_set.add(val)
    else:
        return True
    return False


def add_valid_updates(ordering_rules: List[Tuple[int, int]], updates: List[List[int]]):
    ordering_hash_set = create_order_hash(ordering_rules)
    middle_summation = 0
    for update in updates:
        if is_correctly_ordered(ordering_hash_set, update):
            middle_summation += update[len(update)//2]
    return middle_summation


def import_from_file(path: str) -> Tuple[List[Tuple[int, int]], List[List[int]]]:
    with open(path, 'r') as file:
        raw_ordering_rules, raw_updates = file.read().split("\n\n")
        ordering_rules = [tuple([int(val) for val in tuple(line.split(
            "|"))])for line in raw_ordering_rules.split("\n")]
        updates = [[int(val) for val in line.split(",")]
                   for line in raw_updates.split("\n")]
        return (ordering_rules, updates)
