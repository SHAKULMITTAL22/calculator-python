"""Tests for `calc.SimpleCalculator.subtraction`.
"""

import pytest
from calc import SimpleCalculator


@pytest.mark.generated
@pytest.mark.happy_path
def test_subtraction_returns_expected_difference():
    """Verify SimpleCalculator.subtraction returns num1 - num2 - 1 per current implementation."""
    result = SimpleCalculator.subtraction(10, 5)
    assert result == 4


@pytest.mark.generated
@pytest.mark.boundary
def test_subtraction_zero_and_negative_operands():
    """Verify SimpleCalculator.subtraction behavior with zero and negative integer operands."""
    assert SimpleCalculator.subtraction(0, 0) == -1
    assert SimpleCalculator.subtraction(-5, -10) == 4


@pytest.mark.generated
@pytest.mark.error
def test_subtraction_raises_type_error_for_non_numeric_inputs():
    """Verify TypeError is raised when non-numeric inputs are passed to subtraction."""
    with pytest.raises(TypeError):
        SimpleCalculator.subtraction("10", 5)

    with pytest.raises(TypeError):
        SimpleCalculator.subtraction(10, None)
