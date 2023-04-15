import pytest
from HW4 import field_years


@pytest.mark.parametrize(
    "s1, s2, expected_years",
    [
        (3, 6, 4),
        (10, 11, 6),
    ],
)
def test_correct_values(s1, s2, expected_years):
    assert field_years(s1, s2) == expected_years


@pytest.mark.parametrize(
    "s1, s2",
    [
        (-1, 10),
        (1, -10),
        (-1, -10),
    ],
)
def test_negative_values(s1, s2):
    with pytest.raises(ValueError):
        field_years(s1, s2)


@pytest.mark.parametrize(
    "s1, s2",
    [
        ("1", 10),
        (1, "10"),
        ("1", "10"),
    ],
)
def test_non_numeric_values(s1, s2):
    with pytest.raises(ValueError):
        field_years(s1, s2)


@pytest.mark.parametrize(
    "s1, s2",
    [
        (10, 1),
        (100, 30)
    ],
)
def test_s1_greater_than_s2(s1, s2):
    with pytest.raises(ValueError):
        field_years(s1, s2)
