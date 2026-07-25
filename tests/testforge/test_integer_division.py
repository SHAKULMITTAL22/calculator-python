# tests/testforge/test_integer_division.py
import pytest
from calc_advance import AdvancedCalculator

def test_divide_two_positive_integers():
    """
    [happy] Divide two positive integers
    """
    assert AdvancedCalculator.integer_division(10, 2) == 5

def test_divide_positive_by_negative():
    """
    [happy] Divide a positive integer by a negative integer
    """
    assert AdvancedCalculator.integer_division(10, -2) == -5

def test_divide_two_negative_integers():
    """
    [happy] Divide two negative integers
    """
    assert AdvancedCalculator.integer_division(-10, -2) == 5

def test_divide_zero_by_non_zero():
    """
    [happy] Divide zero by a non-zero integer
    """
    assert AdvancedCalculator.integer_division(0, 5) == 0

def test_divide_with_truncation():
    """
    [edge] Divide a positive integer by a smaller positive integer, resulting in truncation
    """
    assert AdvancedCalculator.integer_division(10, 3) == 3

def test_divide_by_zero():
    """
    [error] Attempt to divide by zero
    """
    # NOTE: The implementation returns a string instead of raising ZeroDivisionError.
    # This test asserts the current behavior.
    assert AdvancedCalculator.integer_division(10, 0) == "Cannot perform integer division by zero"

def test_divide_when_num1_is_multiple_of_num2():
    """
    [boundary] Divide when num1 is a multiple of num2
    """
    assert AdvancedCalculator.integer_division(12, 4) == 3

