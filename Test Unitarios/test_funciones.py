import pytest
from funciones import is_greater_than, sum_numbers


def test_sum_numbers():
    assert sum_numbers(2, 2) == 4


def test_is_greater_than():
    assert is_greater_than(10, 2)


@pytest.mark.parametrize(
    'input_x, input_y, expected',
    [
        (5, 1, 6),
        (6, sum_numbers(4, 2), 12),
        (sum_numbers(19, 1), 15, 35),
        (-7, 10, sum_numbers(-7, 10)),
    ],
)
def test_sum_numbers_params(input_x, input_y, expected):
    assert sum_numbers(input_x, input_y) == expected
