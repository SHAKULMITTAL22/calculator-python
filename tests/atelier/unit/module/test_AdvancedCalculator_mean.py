"""Tests for `calc_advance.AdvancedCalculator.mean`."""

import pytest
from calc_advance import AdvancedCalculator


@pytest.mark.generated
@pytest.mark.happy_path
def test_mean_integers():
    """Calculates mean for a list of integers."""
    assert AdvancedCalculator.mean([1, 2, 3, 4, 5]) == 3.0
    assert AdvancedCalculator.mean([10, 20, 30]) == 20.0


@pytest.mark.generated
@pytest.mark.happy_path
def test_mean_floats():
    """Calculates mean for floating point numbers."""
    assert AdvancedCalculator.mean([1.5, 2.5, 3.5, 4.5]) == 3.0


@pytest.mark.generated
@pytest.mark.happy_path
def test_mean_single_element():
    """Calculates mean for a single-element collection."""
    assert AdvancedCalculator.mean([42]) == 42


@pytest.mark.generated
@pytest.mark.happy_path
def test_mean_negative_numbers():
    """Calculates mean for negative numbers."""
    assert AdvancedCalculator.mean([-10, 0, 10]) == 0.0
    assert AdvancedCalculator.mean([-5, -15]) == -10.0


@pytest.mark.generated
@pytest.mark.happy_path
def test_mean_tuple():
    """Calculates mean when passed a tuple."""
    assert AdvancedCalculator.mean((2, 4, 6, 8)) == 5.0


@pytest.mark.generated
@pytest.mark.happy_path
def test_mean_instance_method():
    """Verifies mean can be called on an instance."""
    calc = AdvancedCalculator()
    assert calc.mean([2, 4, 6]) == 4.0


@pytest.mark.generated
@pytest.mark.error_path
def test_mean_empty_list_raises_value_error():
    """Asserts calculating mean of an empty collection raises ValueError."""
    with pytest.raises(ValueError):
        AdvancedCalculator.mean([])


@pytest.mark.generated
@pytest.mark.error_path
def test_mean_invalid_elements_raises_type_error():
    """Asserts non-numeric elements in sequence raise TypeError."""
    with pytest.raises(TypeError):
        AdvancedCalculator.mean([1, "2", 3])
