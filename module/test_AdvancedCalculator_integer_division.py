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
#   run_id:        7b5781f7
#   generated_at:  2026-04-27T05:33:01Z
#   scenarios:
#     - [happy_path ] positive_integers_inexact: Test integer division with two positive integers where the result is not exact.
#     - [edge_case  ] division_by_zero: Test division by zero returns the specific error message string.
#     - [happy_path ] negative_numerator: Test integer division with a negative numerator to verify floor division behavior.
#     - [happy_path ] zero_numerator: Test integer division where the numerator is zero.
#     - [happy_path ] numerator_smaller_than_denominator: Test integer division where the numerator is smaller than the denominator.
#     - [edge_case  ] large_integers: Test integer division with very large integers.
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
def test_positive_integers_inexact():
    """Test integer division with two positive integers where the result is not exact."""
    result = AdvancedCalculator.integer_division(10, 3)
    assert result == 3

@pytest.mark.generated
@pytest.mark.edge_case
def test_division_by_zero():
    """Test division by zero returns the specific error message string."""
    result = AdvancedCalculator.integer_division(10, 0)
    assert result == "Cannot perform integer division by zero"

@pytest.mark.generated
@pytest.mark.happy_path
def test_negative_numerator():
    """Test integer division with a negative numerator to verify floor division behavior."""
    result = AdvancedCalculator.integer_division(-10, 3)
    assert result == -4

@pytest.mark.generated
@pytest.mark.happy_path
def test_zero_numerator():
    """Test integer division where the numerator is zero."""
    result = AdvancedCalculator.integer_division(0, 5)
    assert result == 0

@pytest.mark.generated
@pytest.mark.happy_path
def test_numerator_smaller_than_denominator():
    """Test integer division where the numerator is smaller than the denominator."""
    result = AdvancedCalculator.integer_division(2, 5)
    assert result == 0

@pytest.mark.generated
@pytest.mark.edge_case
def test_large_integers():
    """Test integer division with very large integers."""
    result = AdvancedCalculator.integer_division(10**20, 10**10)
    assert result == 10**10
