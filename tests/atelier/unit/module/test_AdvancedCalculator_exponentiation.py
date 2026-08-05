"""Tests for `calc_advance.AdvancedCalculator.exponentiation`.
"""

import pytest
from calc_advance import AdvancedCalculator


@pytest.mark.generated
@pytest.mark.happy_path
def test_exponentiation_base_raised_to_exponent():
    """Verify AdvancedCalculator.exponentiation calculates base raised to exponent."""
    result = AdvancedCalculator.exponentiation(2, 3)
    assert result == 8


@pytest.mark.generated
@pytest.mark.boundary
def test_exponentiation_zero_exponent_and_zero_base():
    """Verify AdvancedCalculator.exponentiation handles zero exponent and zero base cases."""
    res_zero_exp = AdvancedCalculator.exponentiation(5, 0)
    res_zero_base = AdvancedCalculator.exponentiation(0, 5)
    assert res_zero_exp == 1
    assert res_zero_base == 0


@pytest.mark.generated
@pytest.mark.edge
def test_exponentiation_negative_base_and_negative_exponent():
    """Verify AdvancedCalculator.exponentiation handles negative bases and negative exponents."""
    res_neg_exp = AdvancedCalculator.exponentiation(2, -1)
    res_neg_base = AdvancedCalculator.exponentiation(-2, 3)
    assert res_neg_exp == 0.5
    assert res_neg_base == -8


@pytest.mark.generated
@pytest.mark.edge
def test_exponentiation_fractional_powers_and_zero_zero_indeterminate():
    """Verify fractional powers and zero base raised to zero exponent."""
    assert AdvancedCalculator.exponentiation(4, 0.5) == 2.0
    assert AdvancedCalculator.exponentiation(0, 0) == 1
