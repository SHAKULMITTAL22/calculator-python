import pytest
from calc import SimpleCalculator

@pytest.mark.smoke
@pytest.mark.valid
@pytest.mark.positive
def test_subtract_positive_integers():
    num1, num2 = 10, 5
    result = SimpleCalculator.subtraction(num1, num2)
    assert result == 5, f"Expected 5, but got {result}"

@pytest.mark.smoke
@pytest.mark.valid
@pytest.mark.positive
def test_subtract_smaller_from_larger():
    num1, num2 = 15, 7
    result = SimpleCalculator.subtraction(num1, num2)
    assert result == 8, f"Expected 8, but got {result}"

@pytest.mark.smoke
@pytest.mark.valid
@pytest.mark.negative
def test_subtract_larger_from_smaller():
    num1, num2 = 4, 9
    result = SimpleCalculator.subtraction(num1, num2)
    assert result == -5, f"Expected -5, but got {result}"

@pytest.mark.smoke
@pytest.mark.valid
@pytest.mark.boundary
def test_subtract_zero():
    num1, num2 = 23, 0
    result = SimpleCalculator.subtraction(num1, num2)
    assert result == 23, f"Expected 23, but got {result}"

@pytest.mark.smoke
@pytest.mark.valid
@pytest.mark.boundary
def test_subtract_same_number():
    num1, num2 = 7, 7
    result = SimpleCalculator.subtraction(num1, num2)
    assert result == 0, f"Expected 0, but got {result}"

@pytest.mark.regression
@pytest.mark.valid
@pytest.mark.negative
def test_subtract_negative_numbers():
    num1, num2 = -4, -6
    result = SimpleCalculator.subtraction(num1, num2)
    assert result == 2, f"Expected 2, but got {result}"

@pytest.mark.regression
@pytest.mark.valid
def test_subtract_mixed_positive_and_negative():
    num1, num2 = 8, -3
    result = SimpleCalculator.subtraction(num1, num2)
    assert result == 11, f"Expected 11, but got {result}"

@pytest.mark.regression
@pytest.mark.valid
@pytest.mark.performance
def test_subtract_floating_point_numbers():
    num1, num2 = 10.5, 3.2
    result = SimpleCalculator.subtraction(num1, num2)
    assert result == 7.3, f"Expected 7.3, but got {result}"

@pytest.mark.smoke
@pytest.mark.valid
def test_subtract_resulting_in_zero():
    num1, num2 = 5, 5
    result = SimpleCalculator.subtraction(num1, num2)
    assert result == 0, f"Expected 0, but got {result}"

@pytest.mark.performance
@pytest.mark.valid
def test_subtract_large_numbers():
    num1, num2 = 10**12, 10**11
    result = SimpleCalculator.subtraction(num1, num2)
    assert result == 9 * 10**11, f"Expected {9 * 10**11}, but got {result}"

@pytest.mark.performance
@pytest.mark.valid
def test_subtract_small_floating_point():
    num1, num2 = 0.0005, 0.0003
    result = SimpleCalculator.subtraction(num1, num2)
    assert result == 0.0002, f"Expected 0.0002, but got {result}"
