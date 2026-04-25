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
#   run_id:        cf16e38c
#   generated_at:  2026-04-25T14:39:29Z
#   scenarios:
#     - [happy_path ] test_exact_division: Verify that integer division of two positive integers with no remainder returns the correct quotient.
#     - [happy_path ] test_division_with_remainder: Verify that integer division floors the result when there is a remainder.
#     - [edge_case  ] test_division_by_zero: Verify that dividing by zero returns the expected error message instead of raising an exception.
#     - [edge_case  ] test_negative_dividend_flooring: Verify that floor division behavior is maintained with negative dividends (flooring towards negative infinity).
#     - [edge_case  ] test_zero_dividend: Verify that zero divided by any non-zero integer returns zero.
#     - [edge_case  ] test_large_integers: Verify that the method handles very large integers correctly.
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
def test_exact_division():
    """Verify that integer division of two positive integers with no remainder returns the correct quotient."""
    # arrange: from calc_advance import AdvancedCalculator
    # act: AdvancedCalculator.integer_division(20, 4)
    result = AdvancedCalculator.integer_division(20, 4)
    # assert: The result should be 5
    assert result == 5

@pytest.mark.generated
@pytest.mark.happy_path
def test_division_with_remainder():
    """Verify that integer division floors the result when there is a remainder."""
    # arrange: from calc_advance import AdvancedCalculator
    # act: AdvancedCalculator.integer_division(20, 3)
    result = AdvancedCalculator.integer_division(20, 3)
    # assert: The result should be 6
    assert result == 6

@pytest.mark.generated
@pytest.mark.edge_case
def test_division_by_zero():
    """Verify that dividing by zero returns the expected error message instead of raising an exception."""
    # arrange: from calc_advance import AdvancedCalculator
    # act: AdvancedCalculator.integer_division(10, 0)
    result = AdvancedCalculator.integer_division(10, 0)
    # assert: The result should be the string "Cannot perform integer division by zero"
    assert result == "Cannot perform integer division by zero"

@pytest.mark.generated
@pytest.mark.edge_case
def test_negative_dividend_flooring():
    """Verify that floor division behavior is maintained with negative dividends (flooring towards negative infinity)."""
    # arrange: from calc_advance import AdvancedCalculator
    # act: AdvancedCalculator.integer_division(-20, 3)
    result = AdvancedCalculator.integer_division(-20, 3)
    # assert: The result should be -7
    assert result == -7

@pytest.mark.generated
@pytest.mark.edge_case
def test_zero_dividend():
    """Verify that zero divided by any non-zero integer returns zero."""
    # arrange: from calc_advance import AdvancedCalculator
    # act: AdvancedCalculator.integer_division(0, 5)
    result = AdvancedCalculator.integer_division(0, 5)
    # assert: The result should be 0
    assert result == 0

@pytest.mark.generated
@pytest.mark.edge_case
def test_large_integers():
    """Verify that the method handles very large integers correctly."""
    # arrange: from calc_advance import AdvancedCalculator
    # act: AdvancedCalculator.integer_division(10**18, 10**9)
    result = AdvancedCalculator.integer_division(10**18, 10**9)
    # assert: The result should be 10**9
    assert result == 10**9
