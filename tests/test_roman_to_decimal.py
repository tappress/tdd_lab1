import pytest

from converter import int_to_roman


@pytest.mark.parametrize("input_value,expected_output", [(1, "I"), (5, "V"), (10, "X")])
def test_standard_numbers(input_value, expected_output):
    assert int_to_roman(input_value) == expected_output


@pytest.mark.parametrize(
    "input_value,expected_output",
    [(4, "IV"), (9, "IX"), (40, "XL"), (90, "XC"), (400, "CD"), (900, "CM")],
)
def test_subtractive_notation(input_value, expected_output):
    assert int_to_roman(input_value) == expected_output


@pytest.mark.parametrize(
    "input_value,expected_output", [(58, "LVIII"), (1994, "MCMXCIV")]
)
def test_complex_numbers(input_value, expected_output):
    assert int_to_roman(input_value) == expected_output


@pytest.mark.parametrize("input_value,expected_output", [(1, "I")])
def test_lower_boundary(input_value, expected_output):
    assert int_to_roman(input_value) == expected_output


@pytest.mark.parametrize("input_value,expected_output", [(3888, "MMMDCCCLXXXVIII")])
def test_larger_number(input_value, expected_output):
    assert int_to_roman(input_value) == expected_output


@pytest.mark.parametrize("input_value", [0, -1])
def test_zero_or_negative_input(input_value):
    with pytest.raises(ValueError):
        int_to_roman(input_value)


@pytest.mark.parametrize(
    "input_value,expected_output",
    [
        (2, "II"),  # standard repetition
        (3, "III"),  # maximum allowed repetitions
        (20, "XX"),  # double digit, simple repetition
        (276, "CCLXXVI"),  # combination of symbols
        (3000, "MMM"),  # large number, simple repetition
        (38, "XXXVIII"),  # intermediate value with repetition
        (99, "XCIX"),  # sequential subtractive notation
        (494, "CDXCIV"),  # complex number with subtractive notations
    ],
)
def test_varied_numbers(input_value, expected_output):
    assert int_to_roman(input_value) == expected_output
