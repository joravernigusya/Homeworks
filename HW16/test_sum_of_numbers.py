import pytest
from HW4 import sum_of_numbers


@pytest.mark.parametrize(
    "a,b,expected_sum",
    [(4, 8, 30), (5, 5, 5), (10000, 100000, 4950055000), (-5, 5, 0), (0, 0, 0)],
)
def test_sum_of_numbers(a, b, expected_sum):
    assert sum_of_numbers(a, b) == expected_sum
