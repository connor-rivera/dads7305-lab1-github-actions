import pytest
from src import calculator


@pytest.mark.parametrize("x, y, expected", [
    (2, 3, 5),
    (5, 0, 5),
    (-1, 1, 0),
    (-1, -1, -2),
    (1.5, 2.5, 4.0),
])
def test_add(x, y, expected):
    assert calculator.add(x, y) == expected


@pytest.mark.parametrize("x, y, expected", [
    (2, 3, -1),
    (5, 0, 5),
    (-1, 1, -2),
    (-1, -1, 0),
])
def test_subtract(x, y, expected):
    assert calculator.subtract(x, y) == expected


@pytest.mark.parametrize("x, y, expected", [
    (2, 3, 6),
    (5, 0, 0),
    (-1, 1, -1),
    (-1, -1, 1),
])
def test_multiply(x, y, expected):
    assert calculator.multiply(x, y) == expected


@pytest.mark.parametrize("x, y, z, expected", [
    (2, 3, 5, 10),
    (5, 0, -1, 4),
    (-1, -1, -1, -3),
    (-1, -1, 100, 98),
])
def test_add_three_nums(x, y, z, expected):
    assert calculator.add_three_nums(x, y, z) == expected


@pytest.mark.parametrize("x, y, expected", [
    (6, 3, 2.0),
    (7, 2, 3.5),
    (-9, 3, -3.0),
])
def test_divide(x, y, expected):
    assert calculator.divide(x, y) == expected


@pytest.mark.parametrize("x, y, expected", [
    (2, 3, 8),
    (5, 0, 1),
    (2, -1, 0.5),
])
def test_power(x, y, expected):
    assert calculator.power(x, y) == expected


@pytest.mark.parametrize("numbers, expected", [
    ([2, 4, 6], 4.0),
    ([7], 7.0),
    ([-1, 1], 0.0),
])
def test_average(numbers, expected):
    assert calculator.average(numbers) == expected


@pytest.mark.parametrize("func, args", [
    (calculator.add, ("a", 1)),
    (calculator.subtract, (1, "b")),
    (calculator.multiply, (None, 2)),
    (calculator.add_three_nums, (1, 2, "3")),
    (calculator.divide, ("6", 3)),
    (calculator.divide, (1, 0)),
    (calculator.power, ("2", 3)),
    (calculator.average, ([],)),
    (calculator.average, ([1, "a", 3],)),
])
def test_invalid_inputs_raise_value_error(func, args):
    with pytest.raises(ValueError):
        func(*args)   
