from main import part_one_solve, import_input


def test_import():
    actual = [[7, 6, 4, 2, 1],
              [1, 2, 7, 8, 9],
              [9, 7, 6, 2, 1],
              [1, 3, 2, 4, 5],
              [8, 6, 4, 4, 1],
              [1, 3, 6, 7, 9]]
    assert actual == import_input('example.txt')
    pass


def test_solve_part1():
    data = [[7, 6, 4, 2, 1],
            [1, 2, 7, 8, 9],
            [9, 7, 6, 2, 1],
            [1, 3, 2, 4, 5],
            [8, 6, 4, 4, 1],
            [1, 3, 6, 7, 9]]
    result = 2
    assert result == part_one_solve(data, 1, 3)
