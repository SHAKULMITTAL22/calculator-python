"""Tests for `calc.SimpleCalculator.addition`."""

import pytest
from calc import SimpleCalculator

@pytest.mark.generated
@pytest.mark.happy_path
def test_addition_happy_path_10_5():
    """Passing num1=10 and num2=5 must return the correct mathematical sum of 15."""
    assert SimpleCalculator.addition(10, 5) == 15

@pytest.mark.generated
@pytest.mark.happy_path
def test_addition_happy_path_0_0():
    """Passing num1=0 and num2=0 must return 0."""
    assert SimpleCalculator.addition(0, 0) == 0

@pytest.mark.generated
@pytest.mark.happy_path
def test_addition_happy_path_negative():
    """Passing num1=-10 and num2=-5 must return -15."""
    assert SimpleCalculator.addition(-10, -5) == -15

@pytest.mark.generated
@pytest.mark.error_path
def test_addition_error_path_type_error():
    """Passing num1=1 and num2='2' must raise TypeError with message 'unsupported operand type(s) for +'."""
    with pytest.raises(TypeError, match=r"unsupported operand type\(s\) for \+"):
        SimpleCalculator.addition(1, '2')
