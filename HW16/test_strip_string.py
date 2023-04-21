import pytest
from HW3 import strip_string


@pytest.mark.parametrize(
    "input_string, expected_output",
    [
        # Проверка удаления пробелов слева
        ("  some text", "some text"),
        # Проверка удаления пробелов справа
        ("some text  ", "some text"),
        # Проверка удаления пробелов с слева и справа
        ("  some text  ", "some text"),
        # Проверка удаление одного пробела
        (" ", ""),
        # Проверка текста без пробелов
        ("some text", "some text"),
        # Проверка ввода целого числа
        (4535, ValueError),
        # Проверка ввода дробного числа
        (23.2, ValueError),
    ],
)
def test_strip_string(input_string, expected_output):
    if expected_output == ValueError:
        with pytest.raises(ValueError):
            strip_string(input_string)
    else:
        assert strip_string(input_string) == expected_output
