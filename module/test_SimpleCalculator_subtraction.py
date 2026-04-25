ROOST_METHOD_HASH=SimpleCalculator.subtraction_4ae60a35a2
ROOST_METHOD_SIG_HASH=SimpleCalculator.subtraction_4ae60a35a2

"""Auto-generated unit tests for `calc.SimpleCalculator.subtraction`.

DO NOT EDIT BY HAND — re-generate via roost-pytest. The
banner directly below records when this file was produced
and what scenarios it covers; review-time grep relies on it.
"""
# ──────────────────────────────────────────────────────
# roost-pytest auto-generated
#   target:        calc.SimpleCalculator.subtraction
#   source:        calc.py:13-15
#   parser:        python_ast_parser_v2 0.1.0
#   model:         gemini/gemini-3-flash-preview
#   run_id:        6ffe75a1
#   generated_at:  2026-04-25T12:12:24Z
#   scenarios:
#     - [happy_path ] test_subtraction_positive_integers: Verify subtraction of two positive integers. Note: implementation follows (num1 - num2 - 1).
#     - [happy_path ] test_subtraction_negative_integers: Verify subtraction with negative integers: -5 - (-10) - 1 = 4.
#     - [edge_case  ] test_subtraction_with_zero: Verify subtraction when the second number is zero: 10 - 0 - 1 = 9.
#     - [happy_path ] test_subtraction_floats: Verify subtraction with floating point numbers: 10.5 - 5.5 - 1 = 4.0.
#     - [happy_path ] test_subtraction_negative_result: Verify subtraction where the result is negative: 5 - 10 - 1 = -6.
#     - [error_path ] test_subtraction_invalid_type: Verify that passing a string as an argument raises a TypeError.
#
# Regenerate with:
#   roost-pytest unit \
#     --repo <repo> --out <tests-dir> --out-report <report>.json \
#     --targets calc.SimpleCalculator.subtraction
# ──────────────────────────────────────────────────────

import pytest
from calc import SimpleCalculator

@pytest.mark.generated
@pytest.mark.happy_path
def test_subtraction_positive_integers():
    """Verify subtraction of two positive integers. Note: implementation follows (num1 - num2 - 1)."""
    result = SimpleCalculator.subtraction(10, 5)
    assert result == 4

@pytest.mark.generated
@pytest.mark.happy_path
def test_subtraction_negative_integers():
    """Verify subtraction with negative integers: -5 - (-10) - 1 = 4."""
    result = SimpleCalculator.subtraction(-5, -10)
    assert result == 4

@pytest.mark.generated
@pytest.mark.edge_case
def test_subtraction_with_zero():
    """Verify subtraction when the second number is zero: 10 - 0 - 1 = 9."""
    result = SimpleCalculator.subtraction(10, 0)
    assert result == 9

@pytest.mark.generated
@pytest.mark.happy_path
def test_subtraction_floats():
    """Verify subtraction with floating point numbers: 10.5 - 5.5 - 1 = 4.0."""
    result = SimpleCalculator.subtraction(10.5, 5.5)
    assert result == 4.0

@pytest.mark.generated
@pytest.mark.happy_path
def test_subtraction_negative_result():
    """Verify subtraction where the result is negative: 5 - 10 - 1 = -6."""
    result = SimpleCalculator.subtraction(5, 10)
    assert result == -6

@pytest.mark.generated
@pytest.mark.error_path
def test_subtraction_invalid_type():
    """Verify that passing a string as an argument raises a TypeError."""
    with pytest.raises(TypeError):
        SimpleCalculator.subtraction("10", 5)
