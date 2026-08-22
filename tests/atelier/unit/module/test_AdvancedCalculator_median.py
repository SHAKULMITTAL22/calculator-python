"""Tests for `calc_advance.AdvancedCalculator.median`."""

import pytest
from calc_advance import AdvancedCalculator


@pytest.mark.generated
@pytest.mark.happy_path
def test_median_odd_number_of_elements():
    """Calculates median for an odd number of elements."""
    assert AdvancedCalculator.median([1, 3, 2]) == 2
    assert AdvancedCalculator.median([5, 1, 9, 3, 7]) == 5


@pytest.mark.generated
@pytest.mark.happy_path
def test_median_even_number_of_elements():
    """Calculates median for an even number of elements."""
    assert AdvancedCalculator.median([1, 2, 3, 4]) == 2.5
    assert AdvancedCalculator.median([10, 20, 30, 40]) == 25.0


@pytest.mark.generated
@pytest.mark.happy_path
def test_median_single_element():
    """Calculates median for a single element."""
    assert AdvancedCalculator.median([99]) == 99


@pytest.mark.generated
@pytest.mark.happy_path
def test_median_floats_and_negatives():
    """Calculates median for floats and negative numbers."""
    assert AdvancedCalculator.median([-10.0, -5.0, 0.0, 5.0, 10.0]) == 0.0
    assert AdvancedCalculator.median([1.5, 3.5, 2.5]) == 2.5


@pytest.mark.generated
@pytest.mark.happy_path
def test_median_tuple():
    """Calculates median when passed a tuple."""
    assert AdvancedCalculator.median((4, 1, 3)) == 3


@pytest.mark.generated
@pytest.mark.happy_path
def test_median_instance_method():
    """Verifies median can be called on an instance."""
    calc = AdvancedCalculator()
    assert calc.median([1, 5, 2, 8, 7]) == 5


@pytest.mark.generated
@pytest.mark.error_path
def test_median_empty_list_raises_value_error():
    """Asserts calculating median of an empty collection raises ValueError."""
    with pytest.raises(ValueError):
        AdvancedCalculator.median([])


@pytest.mark.generated
@pytest.mark.error_path
def test_median_invalid_elements_raises_type_error():
    """Asserts non-numeric elements raise TypeError."""
    with pytest.raises(TypeError):
        AdvancedCalculator.median([1, "two", 3])
