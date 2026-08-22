"""Tests for `calc.SimpleCalculator.absolute`."""

import pytest
from calc import SimpleCalculator


@pytest.mark.generated
@pytest.mark.happy_path
def test_absolute_positive_number():
    """Returns absolute value of a positive number."""
    assert SimpleCalculator.absolute(10) == 10
    assert SimpleCalculator.absolute(3.14) == 3.14


@pytest.mark.generated
@pytest.mark.happy_path
def test_absolute_negative_number():
    """Returns absolute value of a negative number."""
    assert SimpleCalculator.absolute(-10) == 10
    assert SimpleCalculator.absolute(-3.14) == 3.14


@pytest.mark.generated
@pytest.mark.happy_path
def test_absolute_zero():
    """Returns absolute value of zero."""
    assert SimpleCalculator.absolute(0) == 0
    assert SimpleCalculator.absolute(0.0) == 0.0


@pytest.mark.generated
@pytest.mark.happy_path
def test_absolute_instance_method():
    """Verifies absolute can be called on an instance."""
    calc = SimpleCalculator()
    assert calc.absolute(-42) == 42


@pytest.mark.generated
@pytest.mark.error_path
def test_absolute_type_error():
    """Asserts passing a string results in TypeError."""
    with pytest.raises(TypeError):
        SimpleCalculator.absolute("string")
