"""Tests for `calc.SimpleCalculator.subtraction`."""

import pytest
from calc import SimpleCalculator

@pytest.mark.generated
@pytest.mark.happy_path
def test_subtraction_positive_numbers():
    """Passing num1=10 and num2=5 must return 5."""
    assert SimpleCalculator.subtraction(10, 5) == 5

@pytest.mark.generated
@pytest.mark.happy_path
def test_subtraction_zeros():
    """Passing num1=0 and num2=0 must return 0."""
    assert SimpleCalculator.subtraction(0, 0) == 0

@pytest.mark.generated
@pytest.mark.happy_path
def test_subtraction_negative_numbers():
    """Passing num1=-10 and num2=-5 must return -5."""
    assert SimpleCalculator.subtraction(-10, -5) == -5

@pytest.mark.generated
@pytest.mark.happy_path
def test_subtraction_mixed_signs():
    """Passing num1=5 and num2=-3 must return 8."""
    assert SimpleCalculator.subtraction(5, -3) == 8

@pytest.mark.generated
@pytest.mark.happy_path
def test_subtraction_floats():
    """Passing num1=5.5 and num2=2.0 must return 3.5."""
    assert SimpleCalculator.subtraction(5.5, 2.0) == 3.5

@pytest.mark.generated
@pytest.mark.error_path
def test_subtraction_type_error():
    """Passing invalid types must raise TypeError."""
    with pytest.raises(TypeError):
        SimpleCalculator.subtraction(1, "2")
