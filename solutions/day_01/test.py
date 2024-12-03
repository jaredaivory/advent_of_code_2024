from main import PartOneSolution


def test_import():
    actual1 = [3, 4, 2, 1, 3, 3]
    actual2 = [4, 3, 5, 3, 9, 3]
    arr1, arr2 = PartOneSolution.import_input("example.txt")
    assert actual1 == arr1
    assert actual2 == arr2
    pass


def test_solve():
    actual1 = [3, 4, 2, 1, 3, 3]
    actual2 = [4, 3, 5, 3, 9, 3]
    answer = 11
    assert answer == PartOneSolution.solve(actual1, actual2)
    pass
