from abc import ABC, abstractmethod
from typing import Optional


class SolutionClass[D, R](ABC):
    data: D

    @classmethod
    @abstractmethod
    def import_from_file(self, path: str) -> D:
        raise NotImplementedError

    @classmethod
    @abstractmethod
    def part_one(self, *args) -> R:
        raise NotImplementedError

    @classmethod
    @abstractmethod
    def part_two(self, *args) -> R:
        raise NotImplementedError
