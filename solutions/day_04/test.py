from main import import_input, part_one_solve


test_data = [['M', 'M', 'M', 'S', 'X', 'X', 'M', 'A', 'S', 'M'],
             ['M', 'S', 'A', 'M', 'X', 'M', 'S', 'M', 'S', 'A'],
             ['A', 'M', 'X', 'S', 'X', 'M', 'A', 'A', 'M', 'M'],
             ['M', 'S', 'A', 'M', 'A', 'S', 'M', 'S', 'M', 'X'],
             ['X', 'M', 'A', 'S', 'A', 'M', 'X', 'A', 'M', 'M'],
             ['X', 'X', 'A', 'M', 'M', 'X', 'X', 'A', 'M', 'A'],
             ['S', 'M', 'S', 'M', 'S', 'A', 'S', 'X', 'S', 'S'],
             ['S', 'A', 'X', 'A', 'M', 'A', 'S', 'A', 'A', 'A'],
             ['M', 'A', 'M', 'M', 'M', 'X', 'M', 'M', 'M', 'M'],
             ['M', 'X', 'M', 'X', 'A', 'X', 'M', 'A', 'S', 'X']]


def test_import():
    assert test_data == import_input("example.txt")


def test_part_one_solve():
    assert 18 == part_one_solve(test_data, "XMAS")
