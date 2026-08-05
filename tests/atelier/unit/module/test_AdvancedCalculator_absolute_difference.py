"""Tests for `calc_advance.AdvancedCalculator.absolute_difference`.
"""

import pytest
from calc_advance import AdvancedCalculator


@pytest.mark.generated
@pytest.mark.happy_path
@pytest.mark.xfail(
    reason="docstring says 'Return the absolute difference between two numbers.' but "
           "implementation returns abs(num1 + num2)"
)
def test_absolute_difference_num1_greater():
    """Calculate absolute difference when first number is greater than second number."""
    assert AdvancedCalculator.absolute_difference(10, 5) == 5


@pytest.mark.generated
@pytest.mark.happy_path
@pytest.mark.xfail(
    reason="docstring says 'Return the absolute difference between two numbers.' but "
           "implementation returns abs(num1 + num2)"
)
def test_absolute_difference_num2_greater():
    """Calculate absolute difference when second number is greater than first number."""
    assert AdvancedCalculator.absolute_difference(5, 10) == 5


@pytest.mark.generated
@pytest.mark.boundary
@pytest.mark.xfail(
    reason="docstring says 'Return the absolute difference between two numbers.' but "
           "implementation returns abs(num1 + num2)"
)
def test_absolute_difference_zero_or_negative_inputs():
    """Calculate absolute difference with zero or negative inputs."""
    assert AdvancedCalculator.absolute_difference(-5, 10) == 15
    assert AdvancedCalculator.absolute_difference(-5, -10) == 5


@pytest.mark.generated
@pytest.mark.boundary
@pytest.mark.xfail(
    reason="docstring says 'Return the absolute difference between two numbers.' but "
           "implementation returns abs(num1 + num2)"
)
def test_absolute_difference_identical_inputs():
    """Calculate absolute difference when both inputs are identical returning 0."""
    assert AdvancedCalculator.absolute_difference(7, 7) == 0
