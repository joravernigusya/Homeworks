import pytest
from HW4 import mult_nums


@pytest.mark.parametrize(
    "num, expected",
    [
        (5, 120),  # Положительная проверка небольшого числа
        (1, 1),  # Проверка граничного значения 1
        (0, 0),  # Негативна проверка числа 0
        (
            49,
            608281864034267560872252163321295376887552831379210240000000000,
        ),  # Проверка большого числа
        (7.3, TypeError),  # Негативная проверка дробного числа
        (-5, TypeError),  # Негативная проверка отрицательного числа
    ],
)
def test_mult_nums(num, expected):
    if expected == TypeError:
        with pytest.raises(TypeError):
            mult_nums(num)
    else:
        assert mult_nums(num) == expected
