from .types import SolutionClass
from typing import Iterable, List, Tuple, Set, Optional
import re

type GameStrTuple = Tuple[str, str, str]
type Button = Tuple[int, int]
type Prize = Tuple[int, int]
type Game = Tuple[Button, Button, Prize]


class Solution(SolutionClass[int, int]):
    data: List[Game]

    def __init__(self, path: Optional = None):
        super()
        if path:
            self.import_from_file(path)

    @classmethod
    def import_from_file(self, path):
        self.data = import_from_file(path)
        return self.data

    @classmethod
    def part_one(self, *args):
        return total_cheapest_win(self.data)

    @classmethod
    def part_two(self, prizeAugment: int):
        def augmentPrize(game):
            game = (game[0],
                    game[1],
                    (game[2][0] + prizeAugment, game[2][1] + prizeAugment))
            return game

        games = list(map(augmentPrize, self.data[::]))
        return total_cheapest_win(games)


def chunks(iterable: Iterable, n: int):
    for i in range(0, len(iterable), n):
        yield tuple(iterable[i:i + n])


def parse_game(game: GameStrTuple) -> Game:
    button_regex = r"([A-Z])\+([0-9]+),?"
    prize_regex = r"([A-Z])=([0-9]+),?"
    xA, yA = re.findall(button_regex, game[0])
    xB, yB = re.findall(button_regex, game[1])
    xP, yP = re.findall(prize_regex, game[2])

    buttonA = (int(xA[1]), int(yA[1]))
    buttonB = (int(xB[1]), int(yB[1]))
    prize = (int(xP[1]), int(yP[1]))
    game = (buttonA, buttonB, prize)
    return game


def find_cheapest_win(game: Game) -> int:
    buttonA, buttonB, prize = game
    bN = prize[1]*buttonA[0]-prize[0]*buttonA[1]
    bD = buttonB[1]*buttonA[0]-buttonB[0]*buttonA[1]
    if bN % bD != 0:
        return 0

    b = bN // bD

    aN = (prize[0]-b*buttonB[0])
    aD = buttonA[0]

    if aN % aD != 0:
        return 0

    a = aN // aD
    return a * 3 + b


def total_cheapest_win(games: List[Game]) -> int:
    return sum([find_cheapest_win(game) for game in games])


def import_from_file(path: str) -> List[Game]:
    with open(path) as file:
        lines = list(filter(None, [line.strip() for line in file.readlines()]))
        game_strs = [game_str for game_str in chunks(lines, 3)]
        games = [parse_game(s) for s in game_strs]
        return games
