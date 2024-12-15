from .types import SolutionClass
from typing import List, Optional, Tuple


class Solution(SolutionClass[str, int]):
    data: str

    def __init__(self, path: Optional[str] = None):
        super()
        if path:
            self.import_from_file(path)

    @classmethod
    def import_from_file(self, path: str) -> str:
        self.data = import_from_file(path)
        return self.data

    @classmethod
    def part_one(self):
        memory = diskmap_to_list(self.data)
        compacted_memory = compact_memory(memory)
        return file_checksum(compacted_memory)

    @classmethod
    def part_two(self, *args):
        raise NotImplementedError


def import_from_file(path) -> str:
    with open(path, 'r') as file:
        return ''.join(file.readline())


def diskmap_to_list(diskmap: str) -> List[chr]:
    memory_block = []
    id = 0
    isFreeSpace = False
    for c in diskmap:
        if c != "0":
            memory = [None if isFreeSpace else id for _ in range(int(c))]
            memory_block.extend(memory)
        isFreeSpace = not isFreeSpace
        id += 0 if isFreeSpace else 1
    return memory_block


def compact_memory(memory_block: List[Optional[int]]) -> List[int]:
    i = 0
    j = len(memory_block) - 1
    while i < j:
        while i < j and memory_block[i] != None:
            i += 1
        while i < j and memory_block[j] == None:
            j -= 1
        if i >= j:
            break
        if i < j and memory_block[i] == None and memory_block[j] != None:
            memory_block[i], memory_block[j] = memory_block[j], memory_block[i]

    return memory_block[:j]


def compact_memory_segments(memory_block: List[Optional[int]]) -> List[int]:
    free_space = get_free_space(memory_block)
    print(free_space)

    def swap(
        x, y): memory_block[x], memory_block[y] = memory_block[y], memory_block[x]

    for i in range(len(memory_block)-1, -1, -1):
        if memory_block[i] == None:
            continue
        j = i
        while j > 0 and memory_block[j-1] == memory_block[i]:
            j -= 1
        for idx, (frm, to) in enumerate(free_space):
            memory_size = i - j + 1
            if (to - frm) >= memory_size:
                for k in range(memory_size):
                    swap(frm+k, j+k)
                free_space[idx] = (frm+memory_size, to)
                break
    return memory_block


def get_free_space(memory_block: List[Optional[int]]) -> List[Tuple[int, int]]:
    free_space = []
    is_empty = memory_block[0] == None
    prev = 0
    for i in range(1, len(memory_block)):
        if (memory_block[i] == None) != is_empty:
            if is_empty:
                free_space.append((prev, i))
            is_empty = not is_empty
            prev = i
    return free_space


def file_checksum(memory_block: List[int]) -> int:
    return sum([val * i if val else 0 for i, val in enumerate(memory_block)])
