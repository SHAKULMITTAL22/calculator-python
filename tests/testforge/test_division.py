from calc import division

def test_division_positive():
    """Test division of two positive numbers."""
    assert division(10, 2) == 5

def test_division_negative():
    """Test division with a negative number."""
    assert division(-10, 2) == -5

def test_division_by_zero():
    """Test division by zero."""
    assert division(10, 0) == "Cannot divide by zero"

def test_division_zero_by_number():
    """Test division of zero by a number."""
    assert division(0, 5) == 0

def test_division_float():
    """Test division that results in a float."""
    assert division(5, 2) == 2.5

