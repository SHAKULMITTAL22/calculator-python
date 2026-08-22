"""Tests for `calc_advance.AdvancedCalculator.factorial`."""

import pytest
from calc_advance import AdvancedCalculator


@pytest.mark.generated
@pytest.mark.happy_path
def test_factorial_zero():
    """Calculates factorial of 0."""
    assert AdvancedCalculator.factorial(0) == 1


@pytest.mark.generated
@pytest.mark.happy_path
def test_factorial_one():
    """Calculates factorial of 1."""
    assert AdvancedCalculator.factorial(1) == 1


@pytest.mark.generated
@pytest.mark.happy_path
def test_factorial_positive_integers():
    """Calculates factorial of positive integers."""
    assert AdvancedCalculator.factorial(5) == 120
    assert AdvancedCalculator.factorial(6) == 720
    assert AdvancedCalculator.factorial(10) == 3628800


@pytest.mark.generated
@pytest.mark.happy_path
def test_factorial_instance_method():
    """Verifies factorial can be called on an instance."""
    calc = AdvancedCalculator()
    assert calc.factorial(4) == 24


@pytest.mark.generated
@pytest.mark.error_path
def test_factorial_negative_raises_value_error():
    """Asserts factorial of a negative integer raises ValueError."""
    with pytest.raises(ValueError, match="Factorial is only defined for non-negative integers"):
        AdvancedCalculator.factorial(-1)
    with pytest.raises(ValueError, match="Factorial is only defined for non-negative integers"):
        AdvancedCalculator.factorial(-5)


@pytest.mark.generated
@pytest.mark.error_path
def test_factorial_float_raises_type_error():
    """Asserts factorial of a float raises TypeError."""
    with pytest.raises(TypeError):
        AdvancedCalculator.factorial(5.5)


@pytest.mark.generated
@pytest.mark.error_path
def test_factorial_boolean_raises_type_error():
    """Asserts factorial of a boolean raises TypeError."""
    with pytest.raises(TypeError):
        AdvancedCalculator.factorial(True)


@pytest.mark.generated
@pytest.mark.error_path
def test_factorial_string_raises_type_error():
    """Asserts factorial of a string raises TypeError."""
    with pytest.raises(TypeError):
        AdvancedCalculator.factorial("5")
