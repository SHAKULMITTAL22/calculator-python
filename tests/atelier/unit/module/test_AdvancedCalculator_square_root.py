"""Tests for `calc_advance.AdvancedCalculator.square_root`."""

import pytest
from calc_advance import AdvancedCalculator


@pytest.mark.generated
@pytest.mark.happy_path
def test_square_root_positive_integer():
    """Calculates square root of a positive integer."""
    assert AdvancedCalculator.square_root(4) == 2.0
    assert AdvancedCalculator.square_root(16) == 4.0


@pytest.mark.generated
@pytest.mark.happy_path
def test_square_root_zero():
    """Calculates square root of zero."""
    assert AdvancedCalculator.square_root(0) == 0.0


@pytest.mark.generated
@pytest.mark.happy_path
def test_square_root_floating_point():
    """Calculates square root of a floating point number."""
    assert AdvancedCalculator.square_root(2.25) == 1.5


@pytest.mark.generated
@pytest.mark.happy_path
def test_square_root_instance_method():
    """Verifies square_root can be called on an instance."""
    calc = AdvancedCalculator()
    assert calc.square_root(9) == 3.0


@pytest.mark.generated
@pytest.mark.error_path
def test_square_root_negative_raises_value_error():
    """Asserts calculating square root of a negative number raises ValueError."""
    with pytest.raises(ValueError, match="Cannot calculate square root of a negative number"):
        AdvancedCalculator.square_root(-4)


@pytest.mark.generated
@pytest.mark.error_path
def test_square_root_invalid_type_raises_type_error():
    """Asserts passing a non-numeric type raises TypeError."""
    with pytest.raises(TypeError):
        AdvancedCalculator.square_root("4")
