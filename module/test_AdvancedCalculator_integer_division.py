# ROOST_METHOD_HASH=AdvancedCalculator.integer_division_6e0bd798e7
# ROOST_METHOD_SIG_HASH=AdvancedCalculator.integer_division_6e0bd798e7

"""Auto-generated unit tests for `calc_advance.AdvancedCalculator.integer_division`.

DO NOT EDIT BY HAND — re-generate via roost-pytest. The
banner directly below records when this file was produced
and what scenarios it covers; review-time grep relies on it.
"""
# ──────────────────────────────────────────────────────
# roost-pytest auto-generated
#   target:        calc_advance.AdvancedCalculator.integer_division
#   source:        calc_advance.py:15-19
#   parser:        python_ast_parser_v2 0.1.0
#   model:         gemini/gemini-3-flash-preview
#   run_id:        37c4aef7
#   generated_at:  2026-04-25T13:50:20Z
#   scenarios:
#     - [happy_path ] positive_integers: Test integer division with two positive integers where the result is not exact.
#     - [happy_path ] negative_result: Test integer division with a negative numerator, verifying floor division behavior.
#     - [error_path ] division_by_zero: Test integer division by zero, which should return a specific error message string.
#     - [happy_path ] zero_numerator: Test integer division where the numerator is zero.
#     - [happy_path ] both_negative_integers: Test integer division with two negative integers.
#     - [happy_path ] exact_division: Test integer division where the numerator is exactly divisible by the denominator.
#
# Regenerate with:
#   roost-pytest unit \
#     --repo <repo> --out <tests-dir> --out-report <report>.json \
#     --targets calc_advance.AdvancedCalculator.integer_division
# ──────────────────────────────────────────────────────

import pytest
from calc_advance import AdvancedCalculator

@pytest.mark.generated
@pytest.mark.happy_path
def test_positive_integers():
    """Test integer division with two positive integers where the result is not exact."""
    assert AdvancedCalculator.integer_division(10, 3) == 3

@pytest.mark.generated
@pytest.mark.happy_path
def test_negative_result():
    """Test integer division with a negative numerator, verifying floor division behavior."""
    assert AdvancedCalculator.integer_division(-10, 3) == -4

@pytest.mark.generated
@pytest.mark.error_path
def test_division_by_zero():
    """Test integer division by zero, which should return a specific error message string."""
    assert AdvancedCalculator.integer_division(10, 0) == "Cannot perform integer division by zero"

@pytest.mark.generated
@pytest.mark.happy_path
def test_zero_numerator():
    """Test integer division where the numerator is zero."""
    assert AdvancedCalculator.integer_division(0, 5) == 0

@pytest.mark.generated
@pytest.mark.happy_path
def test_both_negative_integers():
    """Test integer division with two negative integers."""
    assert AdvancedCalculator.integer_division(-10, -3) == 3

@pytest.mark.generated
@pytest.mark.happy_path
def test_exact_division():
    """Test integer division where the numerator is exactly divisible by the denominator."""
    assert AdvancedCalculator.integer_division(20, 5) == 4
