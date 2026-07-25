import pytest
from calc import division

def test_error_division_by_zero():
    """
    Test division by zero, expecting 'Cannot divide by zero'.
    """
    assert division(10, 0) == "Cannot divide by zero"

def test_happy_positive_integers():
    """
    Test division with both num1 and num2 as positive integers,
    expecting a positive quotient.
    """
    assert division(10, 2) == 5

def test_happy_zero_numerator():
    """
    Test division with num1 as zero and num2 as a non-zero integer,
    expecting zero.
    """
    assert division(0, 5) == 0

def test_edge_negative_numbers():
    """
    Test division with negative numbers, expecting correct signed quotients.
    """
    assert division(10, -2) == -5
    assert division(-10, 2) == -5
    assert division(-10, -2) == 5

def test_edge_floating_point_numbers():
    """
    Test division with floating-point numbers, expecting a correct float quotient.
    """
    assert division(5.0, 2.0) == 2.5
    assert division(-5.0, 2.0) == -2.5
