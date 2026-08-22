"""Tests for `calc_advance.AdvancedCalculator.round_number`."""

import pytest
from calc_advance import AdvancedCalculator


@pytest.mark.generated
@pytest.mark.happy_path
def test_round_number_default_decimals():
    """Rounds number to 0 decimal places by default."""
    assert AdvancedCalculator.round_number(3.14159) == 3.0
    assert AdvancedCalculator.round_number(3.7) == 4.0
    assert AdvancedCalculator.round_number(-3.7) == -4.0


@pytest.mark.generated
@pytest.mark.happy_path
def test_round_number_specified_decimals():
    """Rounds number to specified number of decimal places."""
    assert AdvancedCalculator.round_number(3.14159265, 2) == 3.14
    assert AdvancedCalculator.round_number(3.14159265, 4) == 3.1416
    assert AdvancedCalculator.round_number(-2.567, 1) == -2.6


@pytest.mark.generated
@pytest.mark.happy_path
def test_round_number_negative_decimals():
    """Rounds number to negative decimal places (powers of 10)."""
    assert AdvancedCalculator.round_number(1234.56, -2) == 1200.0


@pytest.mark.generated
@pytest.mark.happy_path
def test_round_number_instance_method():
    """Verifies round_number can be called on an instance."""
    calc = AdvancedCalculator()
    assert calc.round_number(2.71828, 3) == 2.718


@pytest.mark.generated
@pytest.mark.error_path
def test_round_number_invalid_num_raises_type_error():
    """Asserts non-numeric num raises TypeError."""
    with pytest.raises(TypeError):
        AdvancedCalculator.round_number("3.14", 2)


@pytest.mark.generated
@pytest.mark.error_path
def test_round_number_invalid_decimals_raises_type_error():
    """Asserts non-integer decimals argument raises TypeError."""
    with pytest.raises(TypeError):
        AdvancedCalculator.round_number(3.14, "2")
    with pytest.raises(TypeError):
        AdvancedCalculator.round_number(3.14, 2.5)
    with pytest.raises(TypeError):
        AdvancedCalculator.round_number(3.14, True)
