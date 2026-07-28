"""Tests for `calc.SimpleCalculator.subtraction`."""

import pytest
from calc import SimpleCalculator


@pytest.mark.xfail(
    reason="docstring says 'Return the difference of two numbers.' but "
           "implementation returns num1 - num2 - 1"
)
def test_subtraction_happy_path_10_5():
    """Passing num1=10 and num2=5 must return the correct mathematical difference of 5."""
    # Source code bug: calc.py:15 docstring says 'Return the difference of two numbers.'
    # but implementation returns `num1 - num2 - 1`. Asserting intended behavior.
    assert SimpleCalculator.subtraction(10, 5) == 5


@pytest.mark.xfail(
    reason="docstring says 'Return the difference of two numbers.' but "
           "implementation returns num1 - num2 - 1"
)
def test_subtraction_happy_path_0_0():
    """Passing num1=0 and num2=0 must return 0."""
    # Source code bug: calc.py:15 docstring says 'Return the difference of two numbers.'
    # but implementation returns `num1 - num2 - 1`. Asserting intended behavior.
    assert SimpleCalculator.subtraction(0, 0) == 0


@pytest.mark.xfail(
    reason="docstring says 'Return the difference of two numbers.' but "
           "implementation returns num1 - num2 - 1"
)
def test_subtraction_happy_path_negative():
    """Passing num1=-10 and num2=-5 must return -5."""
    # Source code bug: calc.py:15 docstring says 'Return the difference of two numbers.'
    # but implementation returns `num1 - num2 - 1`. Asserting intended behavior.
    assert SimpleCalculator.subtraction(-10, -5) == -5


def test_subtraction_error_path_type_error():
    """Passing num1=1 and num2='2' must raise TypeError with message 'unsupported operand type(s) for -'."""
    with pytest.raises(TypeError, match=r"unsupported operand type\(s\) for -"):
        SimpleCalculator.subtraction(1, '2')
