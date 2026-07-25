
import pytest
from calc_advance import AdvancedCalculator

def test_divide_two_positive_integers():
    """
    [happy] Divide two positive integers (e.g., 10 // 3 should be 3).
    """
    assert AdvancedCalculator.integer_division(10, 3) == 3

def test_divide_positive_by_negative():
    """
    [happy] Divide a positive integer by a negative integer (e.g., 10 // -3 should be -4).
    """
    assert AdvancedCalculator.integer_division(10, -3) == -4

def test_divide_two_negative_integers():
    """
    [happy] Divide two negative integers (e.g., -10 // -3 should be 3).
    """
    assert AdvancedCalculator.integer_division(-10, -3) == 3

def test_divide_zero_by_non_zero():
    """
    [happy] Divide zero by a non-zero integer (e.g., 0 // 5 should be 0).
    """
    assert AdvancedCalculator.integer_division(0, 5) == 0

def test_divide_integer_by_larger_integer():
    """
    [edge] Divide an integer by a larger integer (e.g., 3 // 10 should be 0).
    """
    assert AdvancedCalculator.integer_division(3, 10) == 0

def test_divide_by_zero():
    """
    [error] Attempt to divide by zero (e.g., 10 // 0 should return 'Cannot perform integer division by zero').
    """
    assert AdvancedCalculator.integer_division(10, 0) == "Cannot perform integer division by zero"

