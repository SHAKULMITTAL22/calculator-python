"""Tests for `calc_advance.AdvancedCalculator.logarithm`."""

import pytest
from calc_advance import AdvancedCalculator


@pytest.mark.generated
@pytest.mark.happy_path
def test_logarithm_default_base():
    """Calculates logarithm with default base 10."""
    assert AdvancedCalculator.logarithm(100) == pytest.approx(2.0)
    assert AdvancedCalculator.logarithm(10) == pytest.approx(1.0)
    assert AdvancedCalculator.logarithm(1) == pytest.approx(0.0)


@pytest.mark.generated
@pytest.mark.happy_path
def test_logarithm_custom_base():
    """Calculates logarithm with custom base."""
    assert AdvancedCalculator.logarithm(8, 2) == pytest.approx(3.0)
    assert AdvancedCalculator.logarithm(27, 3) == pytest.approx(3.0)
    assert AdvancedCalculator.logarithm(16, 4) == pytest.approx(2.0)


@pytest.mark.generated
@pytest.mark.happy_path
def test_logarithm_instance_method():
    """Verifies logarithm can be called on an instance."""
    calc = AdvancedCalculator()
    assert calc.logarithm(1000) == pytest.approx(3.0)


@pytest.mark.generated
@pytest.mark.error_path
def test_logarithm_zero_num_raises_value_error():
    """Asserts logarithm of 0 raises ValueError."""
    with pytest.raises(ValueError, match="Logarithm domain error"):
        AdvancedCalculator.logarithm(0)


@pytest.mark.generated
@pytest.mark.error_path
def test_logarithm_negative_num_raises_value_error():
    """Asserts logarithm of negative number raises ValueError."""
    with pytest.raises(ValueError, match="Logarithm domain error"):
        AdvancedCalculator.logarithm(-10)


@pytest.mark.generated
@pytest.mark.error_path
def test_logarithm_invalid_base_one_raises_value_error():
    """Asserts logarithm with base 1 raises ValueError."""
    with pytest.raises(ValueError, match="Logarithm base must be positive and not equal to 1"):
        AdvancedCalculator.logarithm(10, base=1)


@pytest.mark.generated
@pytest.mark.error_path
def test_logarithm_invalid_base_non_positive_raises_value_error():
    """Asserts logarithm with non-positive base raises ValueError."""
    with pytest.raises(ValueError, match="Logarithm base must be positive and not equal to 1"):
        AdvancedCalculator.logarithm(10, base=0)
    with pytest.raises(ValueError, match="Logarithm base must be positive and not equal to 1"):
        AdvancedCalculator.logarithm(10, base=-2)


@pytest.mark.generated
@pytest.mark.error_path
def test_logarithm_invalid_type_raises_type_error():
    """Asserts non-numeric arguments raise TypeError."""
    with pytest.raises(TypeError):
        AdvancedCalculator.logarithm("100")
