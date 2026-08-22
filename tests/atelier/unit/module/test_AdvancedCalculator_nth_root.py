"""Tests for `calc_advance.AdvancedCalculator.nth_root`."""

import pytest
from calc_advance import AdvancedCalculator


@pytest.mark.generated
@pytest.mark.happy_path
def test_nth_root_standard():
    """Calculates nth root of standard positive numbers."""
    assert AdvancedCalculator.nth_root(8, 3) == pytest.approx(2.0)
    assert AdvancedCalculator.nth_root(27, 3) == pytest.approx(3.0)
    assert AdvancedCalculator.nth_root(16, 2) == pytest.approx(4.0)


@pytest.mark.generated
@pytest.mark.happy_path
def test_nth_root_of_one():
    """Calculates nth root of 1."""
    assert AdvancedCalculator.nth_root(1, 5) == 1.0


@pytest.mark.generated
@pytest.mark.happy_path
def test_nth_root_of_zero():
    """Calculates nth root of 0."""
    assert AdvancedCalculator.nth_root(0, 3) == 0.0


@pytest.mark.generated
@pytest.mark.happy_path
def test_nth_root_fractional_exponent():
    """Calculates nth root with float root."""
    assert AdvancedCalculator.nth_root(4, 0.5) == 16.0


@pytest.mark.generated
@pytest.mark.happy_path
def test_nth_root_instance_method():
    """Verifies nth_root can be called on an instance."""
    calc = AdvancedCalculator()
    assert calc.nth_root(64, 3) == pytest.approx(4.0)


@pytest.mark.generated
@pytest.mark.error_path
def test_nth_root_negative_base_raises_value_error():
    """Asserts calculating root of a negative base raises ValueError."""
    with pytest.raises(ValueError, match="Cannot calculate nth root of a negative number"):
        AdvancedCalculator.nth_root(-8, 3)


@pytest.mark.generated
@pytest.mark.error_path
def test_nth_root_zero_root_raises_value_error():
    """Asserts root of 0 raises ValueError."""
    with pytest.raises(ValueError, match="Root cannot be zero"):
        AdvancedCalculator.nth_root(8, 0)


@pytest.mark.generated
@pytest.mark.error_path
def test_nth_root_invalid_type_raises_type_error():
    """Asserts non-numeric arguments raise TypeError."""
    with pytest.raises(TypeError):
        AdvancedCalculator.nth_root("8", 3)
    with pytest.raises(TypeError):
        AdvancedCalculator.nth_root(8, "3")
