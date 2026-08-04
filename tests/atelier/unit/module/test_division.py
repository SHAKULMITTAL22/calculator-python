"""Tests for `calc.division`.
"""

import pytest
from calc import division
from calc_advance import AdvancedCalculator


@pytest.mark.generated
@pytest.mark.edge
def test_division_float_zero_and_negative_zero_divisors():
    """Verify floating-point zero (0.0) and negative zero (-0.0) divisors in division and integer division."""
    assert division(10, 0.0) == "Cannot divide by zero"
    assert division(10, -0.0) == "Cannot divide by zero"
    assert AdvancedCalculator.integer_division(10, 0.0) == "Cannot perform integer division by zero"
    assert AdvancedCalculator.integer_division(10, -0.0) == "Cannot perform integer division by zero"
