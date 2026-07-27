"""Tests for `calc.division` function."""

import pytest
from calc import division


@pytest.mark.negative
def test_division_by_zero():
    """Division by zero returns the string 'Cannot divide by zero'."""
    result = division(10, 0)
    assert result == "Cannot divide by zero"


@pytest.mark.positive
def test_positive_integer_division():
    """Positive integer division returns correct quotient."""
    result = division(20, 4)
    assert result == 5.0


@pytest.mark.positive
def test_division_by_one():
    """Division by one returns the original number."""
    result = division(42, 1)
    assert result == 42.0


@pytest.mark.fractional
def test_division_decimal_results():
    """Division resulting in decimal/float quotients."""
    result = division(7, 2)
    assert result == 3.5


@pytest.mark.mixed_sign
def test_division_negative_and_mixed_signs():
    """Division with negative and mixed sign operands."""
    assert division(-18, -2) == 9.0
    assert division(15, -3) == -5.0
