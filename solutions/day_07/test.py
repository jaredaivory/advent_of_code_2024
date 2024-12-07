from main import import_input, part_one_solve


actual = [
    (190, [10, 19]),
    (3267, [81, 40, 27]),
    (83, [17, 5]),
    (156, [15, 6]),
    (7290, [6, 8, 6, 15]),
    (161011, [16, 10, 13]),
    (192, [17, 8, 14]),
    (21037, [9, 7, 18, 13]),
    (292, [11, 6, 16, 20])
]


def test_import():
    assert actual == import_input("example.txt")


def test_part_one_solve():
    assert 3749 == part_one_solve(actual)
