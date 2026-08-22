"""Tests for `calc.SimpleCalculator.division`."""

import pytest
from calc import SimpleCalculator


@pytest.mark.generated
@pytest.mark.happy_path
def test_division_positive_integers():
    """Calculates quotient for standard positive integers."""
    assert SimpleCalculator.division(20, 4) == 5.0


@pytest.mark.generated
@pytest.mark.happy_path
def test_division_handles_zero_divisor():
    """Handles zero divisor by returning sentinel error message."""
    assert SimpleCalculator.division(10, 0) == "Cannot divide by zero"


@pytest.mark.generated
@pytest.mark.happy_path
def test_division_negative_numbers():
    """Calculates quotient when both operands are negative."""
    assert SimpleCalculator.division(-18, -2) == 9.0


@pytest.mark.generated
@pytest.mark.happy_path
def test_division_mixed_signs():
    """Calculates quotient with mixed signs."""
    assert SimpleCalculator.division(15, -3) == -5.0
    assert SimpleCalculator.division(-15, 3) == -5.0


@pytest.mark.generated
@pytest.mark.happy_path
def test_division_zero_dividend():
    """Calculates quotient when dividend is zero."""
    assert SimpleCalculator.division(0, 5) == 0.0


@pytest.mark.generated
@pytest.mark.happy_path
def test_division_floating_point():
    """Calculates quotient for floating point numbers."""
    assert SimpleCalculator.division(7.5, 2.5) == 3.0


@pytest.mark.generated
@pytest.mark.happy_path
def test_division_instance_method():
    """Verifies division can be called on an instance of SimpleCalculator."""
    calc = SimpleCalculator()
    assert calc.division(10, 2) == 5.0
    assert calc.division(10, 0) == "Cannot divide by zero"


@pytest.mark.generated
@pytest.mark.error_path
def test_division_type_error_first_operand():
    """Asserts passing a string as first operand results in TypeError."""
    with pytest.raises(TypeError):
        SimpleCalculator.division("10", 2)


@pytest.mark.generated
@pytest.mark.error_path
def test_division_type_error_second_operand():
    """Asserts passing a string as second operand results in TypeError."""
    with pytest.raises(TypeError):
        SimpleCalculator.division(10, "2")
