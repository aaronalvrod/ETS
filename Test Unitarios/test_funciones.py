import pytest
from funciones import sum_numbers
def test_sum_numbers():
    assert sum_numbers(2,2) == 4
    
def test_is_greater_than():
    assert is_greater_than(10,2)

