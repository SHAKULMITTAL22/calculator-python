"""Tests for `calc.division`.
"""

import pytest
from calc import division
from calc_advance import AdvancedCalculator


@pytest.mark.generated
@pytest.mark.happy
def test_division_standard_quotients():
    """Verify standard division of numbers resulting in integer and float quotients."""
    assert division(20, 4) == 5.0
    assert division(7, 2) == 3.5


@pytest.mark.generated
@pytest.mark.error
def test_division_by_integer_zero():
    """Verify division by integer zero returns error message."""
    assert division(10, 0) == "Cannot divide by zero"


@pytest.mark.generated
@pytest.mark.edge
def test_division_float_zero_and_negative_zero_divisors():
    """Verify floating-point zero (0.0) and negative zero (-0.0) divisors in division and integer division."""
    assert division(10, 0.0) == "Cannot divide by zero"
    assert division(10, -0.0) == "Cannot divide by zero"
    assert AdvancedCalculator.integer_division(10, 0.0) == "Cannot perform integer division by zero"
    assert AdvancedCalculator.integer_division(10, -0.0) == "Cannot perform integer division by zero"
