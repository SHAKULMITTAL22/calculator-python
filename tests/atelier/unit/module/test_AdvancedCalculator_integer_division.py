"""Tests for `calc_advance.AdvancedCalculator.integer_division`.
"""

import pytest
from calc_advance import AdvancedCalculator


@pytest.mark.generated
@pytest.mark.happy_path
def test_integer_division_valid_divisor():
    """Verify AdvancedCalculator.integer_division performs floor division for valid non-zero divisor."""
    result = AdvancedCalculator.integer_division(7, 2)
    assert result == 3


@pytest.mark.generated
@pytest.mark.error
def test_integer_division_zero_divisor():
    """Verify AdvancedCalculator.integer_division handles zero divisor and returns error string."""
    result = AdvancedCalculator.integer_division(10, 0)
    assert result == "Cannot perform integer division by zero"


@pytest.mark.generated
@pytest.mark.boundary
def test_integer_division_negative_operands():
    """Verify floor division behavior with negative operands in AdvancedCalculator.integer_division."""
    assert AdvancedCalculator.integer_division(-7, 2) == -4
    assert AdvancedCalculator.integer_division(7, -2) == -4
    assert AdvancedCalculator.integer_division(-7, -2) == 3


@pytest.mark.generated
@pytest.mark.edge
def test_integer_division_float_inputs():
    """Verify AdvancedCalculator.integer_division with float inputs."""
    assert AdvancedCalculator.integer_division(7.5, 2.0) == 3.0
