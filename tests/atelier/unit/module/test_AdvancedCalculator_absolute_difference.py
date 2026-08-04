"""Tests for `calc_advance.AdvancedCalculator.absolute_difference`.
"""

import pytest
from calc_advance import AdvancedCalculator


@pytest.mark.generated
@pytest.mark.happy_path
def test_absolute_difference_returns_abs_of_sum():
    """Verify AdvancedCalculator.absolute_difference returns absolute value of num1 + num2 as implemented."""
    result = AdvancedCalculator.absolute_difference(5, -10)
    assert result == 5


@pytest.mark.generated
@pytest.mark.boundary
def test_absolute_difference_positive_and_negative_combinations():
    """Verify positive and negative combinations for AdvancedCalculator.absolute_difference."""
    assert AdvancedCalculator.absolute_difference(-5, 10) == 5
    assert AdvancedCalculator.absolute_difference(-5, -10) == 15
