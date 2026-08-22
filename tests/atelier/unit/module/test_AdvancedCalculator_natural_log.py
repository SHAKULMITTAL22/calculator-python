"""Tests for `calc_advance.AdvancedCalculator.natural_log`."""

import math
import pytest
from calc_advance import AdvancedCalculator


@pytest.mark.generated
@pytest.mark.happy_path
def test_natural_log_one():
    """Calculates natural log of 1."""
    assert AdvancedCalculator.natural_log(1) == pytest.approx(0.0)


@pytest.mark.generated
@pytest.mark.happy_path
def test_natural_log_e():
    """Calculates natural log of Euler's constant e."""
    assert AdvancedCalculator.natural_log(math.e) == pytest.approx(1.0)


@pytest.mark.generated
@pytest.mark.happy_path
def test_natural_log_positive_number():
    """Calculates natural log of arbitrary positive numbers."""
    assert AdvancedCalculator.natural_log(10) == pytest.approx(math.log(10))
    assert AdvancedCalculator.natural_log(2.718) == pytest.approx(math.log(2.718))


@pytest.mark.generated
@pytest.mark.happy_path
def test_natural_log_instance_method():
    """Verifies natural_log can be called on an instance."""
    calc = AdvancedCalculator()
    assert calc.natural_log(math.e ** 2) == pytest.approx(2.0)


@pytest.mark.generated
@pytest.mark.error_path
def test_natural_log_zero_raises_value_error():
    """Asserts natural log of 0 raises ValueError."""
    with pytest.raises(ValueError, match="Natural log domain error"):
        AdvancedCalculator.natural_log(0)


@pytest.mark.generated
@pytest.mark.error_path
def test_natural_log_negative_raises_value_error():
    """Asserts natural log of negative number raises ValueError."""
    with pytest.raises(ValueError, match="Natural log domain error"):
        AdvancedCalculator.natural_log(-1)


@pytest.mark.generated
@pytest.mark.error_path
def test_natural_log_invalid_type_raises_type_error():
    """Asserts non-numeric arguments raise TypeError."""
    with pytest.raises(TypeError):
        AdvancedCalculator.natural_log("10")
