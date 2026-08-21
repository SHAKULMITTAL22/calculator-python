"""Tests for `calc_advance.AdvancedCalculator.absolute_difference`."""

import pytest
from calc_advance import AdvancedCalculator

@pytest.mark.generated
@pytest.mark.happy_path
def test_absolute_difference_positive_order():
    """Passing num1=10 and num2=5 must return 5."""
    assert AdvancedCalculator.absolute_difference(10, 5) == 5

@pytest.mark.generated
@pytest.mark.happy_path
def test_absolute_difference_reversed_order():
    """Passing num1=5 and num2=10 must return 5."""
    assert AdvancedCalculator.absolute_difference(5, 10) == 5

@pytest.mark.generated
@pytest.mark.happy_path
def test_absolute_difference_identical_numbers():
    """Passing identical numbers must return 0."""
    assert AdvancedCalculator.absolute_difference(7, 7) == 0

@pytest.mark.generated
@pytest.mark.happy_path
def test_absolute_difference_mixed_signs():
    """Passing mixed sign numbers must return absolute difference."""
    assert AdvancedCalculator.absolute_difference(5, -3) == 8
    assert AdvancedCalculator.absolute_difference(-5, 3) == 8
    assert AdvancedCalculator.absolute_difference(-5, -3) == 2

@pytest.mark.generated
@pytest.mark.happy_path
def test_absolute_difference_floats():
    """Passing floating point numbers must return absolute difference."""
    assert AdvancedCalculator.absolute_difference(5.5, 2.0) == 3.5
    assert AdvancedCalculator.absolute_difference(2.0, 5.5) == 3.5

@pytest.mark.generated
@pytest.mark.error_path
def test_absolute_difference_type_error():
    """Passing invalid types must raise TypeError."""
    with pytest.raises(TypeError):
        AdvancedCalculator.absolute_difference(1, "2")
