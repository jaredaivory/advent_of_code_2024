from main import import_input, get_starting_point, part_one_solve


actual_grid = [
    ['.', '.', '.', '.', '#', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.', '#'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '#', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '#', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '#', '.', '.', '^', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '#', '.'],
    ['#', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '#', '.', '.', '.'],
]


def test_import():
    assert actual_grid == import_input("example.txt")


def test_get_starting_point():
    assert (6, 4) == get_starting_point(actual_grid, '^')


def test_part_one_solve():
    assert 41 == part_one_solve(actual_grid, 6, 4)
