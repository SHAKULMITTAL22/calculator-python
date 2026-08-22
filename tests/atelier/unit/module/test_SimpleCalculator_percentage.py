"""Tests for `calc.SimpleCalculator.percentage`."""

import pytest
from calc import SimpleCalculator


@pytest.mark.generated
@pytest.mark.happy_path
def test_percentage_standard_values():
    """Calculates percentage for standard positive numbers."""
    assert SimpleCalculator.percentage(200, 15) == 30.0
    assert SimpleCalculator.percentage(50, 10) == 5.0


@pytest.mark.generated
@pytest.mark.happy_path
def test_percentage_zero_total():
    """Calculates percentage when total is zero."""
    assert SimpleCalculator.percentage(0, 50) == 0.0


@pytest.mark.generated
@pytest.mark.happy_path
def test_percentage_zero_percent():
    """Calculates percentage when percent is zero."""
    assert SimpleCalculator.percentage(100, 0) == 0.0


@pytest.mark.generated
@pytest.mark.happy_path
def test_percentage_negative_values():
    """Calculates percentage with negative inputs."""
    assert SimpleCalculator.percentage(-100, 20) == -20.0
    assert SimpleCalculator.percentage(100, -20) == -20.0


@pytest.mark.generated
@pytest.mark.happy_path
def test_percentage_floating_point():
    """Calculates percentage with floating point inputs."""
    assert SimpleCalculator.percentage(150.5, 10.0) == 15.05


@pytest.mark.generated
@pytest.mark.happy_path
def test_percentage_instance_method():
    """Verifies percentage can be called on an instance."""
    calc = SimpleCalculator()
    assert calc.percentage(200, 10) == 20.0


@pytest.mark.generated
@pytest.mark.error_path
def test_percentage_type_error_total():
    """Asserts passing a non-numeric total results in TypeError."""
    with pytest.raises(TypeError):
        SimpleCalculator.percentage("100", 10)


@pytest.mark.generated
@pytest.mark.error_path
def test_percentage_type_error_percent():
    """Asserts passing a non-numeric percent results in TypeError."""
    with pytest.raises(TypeError):
        SimpleCalculator.percentage(100, "10")
