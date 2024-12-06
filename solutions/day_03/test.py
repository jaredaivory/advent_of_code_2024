from main import import_input, part_one_solve, part_two_solve


def test_import():
    actual = [
        "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"]
    assert actual == import_input('example.txt')
    pass


def test_part_one_solve():
    actual = [
        "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"]
    result = 161

    assert result == part_one_solve(actual)


def test_part_two_solve():
    actual = [
        "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"]
    result = 48

    assert result == part_two_solve(actual)
