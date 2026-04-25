# ROOST_METHOD_HASH=AdvancedCalculator.absolute_difference_dce44fd78e
# ROOST_METHOD_SIG_HASH=AdvancedCalculator.absolute_difference_dce44fd78e

"""Auto-generated unit tests for `calc_advance.AdvancedCalculator.absolute_difference`.

DO NOT EDIT BY HAND — re-generate via roost-pytest. The
banner directly below records when this file was produced
and what scenarios it covers; review-time grep relies on it.
"""
# ──────────────────────────────────────────────────────
# roost-pytest auto-generated
#   target:        calc_advance.AdvancedCalculator.absolute_difference
#   source:        calc_advance.py:22-24
#   parser:        python_ast_parser_v2 0.1.0
#   model:         gemini/gemini-3-flash-preview
#   run_id:        37c4aef7
#   generated_at:  2026-04-25T13:50:56Z
#   scenarios:
#     - [happy_path ] test_positive_integers: Verify the absolute difference of two positive integers.
#     - [happy_path ] test_mixed_signs: Verify the absolute difference when one number is negative and the other is positive.
#     - [happy_path ] test_both_negative_integers: Verify the absolute difference of two negative integers.
#     - [edge_case  ] test_floating_point_numbers: Verify the absolute difference with floating point numbers.
#     - [edge_case  ] test_identical_values_is_zero: Verify that the absolute difference of two identical numbers is zero.
#     - [edge_case  ] test_large_numbers_difference: Verify the absolute difference with very large integers.
#
# Regenerate with:
#   roost-pytest unit \
#     --repo <repo> --out <tests-dir> --out-report <report>.json \
#     --targets calc_advance.AdvancedCalculator.absolute_difference
# ──────────────────────────────────────────────────────

import pytest
from calc_advance import AdvancedCalculator

@pytest.mark.generated
@pytest.mark.happy_path
def test_positive_integers():
    """Verify the absolute difference of two positive integers."""
    # arrange: num1 = 10; num2 = 3
    # act: AdvancedCalculator.absolute_difference(10, 3)
    # assert: result == 7
    result = AdvancedCalculator.absolute_difference(10, 3)
    assert result == 7

@pytest.mark.generated
@pytest.mark.happy_path
def test_mixed_signs():
    """Verify the absolute difference when one number is negative and the other is positive."""
    # arrange: num1 = -5; num2 = 8
    # act: AdvancedCalculator.absolute_difference(-5, 8)
    # assert: result == 13
    result = AdvancedCalculator.absolute_difference(-5, 8)
    assert result == 13

@pytest.mark.generated
@pytest.mark.happy_path
def test_both_negative_integers():
    """Verify the absolute difference of two negative integers."""
    # arrange: num1 = -10; num2 = -4
    # act: AdvancedCalculator.absolute_difference(-10, -4)
    # assert: result == 6
    result = AdvancedCalculator.absolute_difference(-10, -4)
    assert result == 6

@pytest.mark.generated
@pytest.mark.edge_case
def test_floating_point_numbers():
    """Verify the absolute difference with floating point numbers."""
    # arrange: num1 = 5.5; num2 = 2.0
    # act: AdvancedCalculator.absolute_difference(5.5, 2.0)
    # assert: result == 3.5
    result = AdvancedCalculator.absolute_difference(5.5, 2.0)
    assert result == 3.5

@pytest.mark.generated
@pytest.mark.edge_case
def test_identical_values_is_zero():
    """Verify that the absolute difference of two identical numbers is zero."""
    # arrange: num1 = 7; num2 = 7
    # act: AdvancedCalculator.absolute_difference(7, 7)
    # assert: result == 0
    result = AdvancedCalculator.absolute_difference(7, 7)
    assert result == 0

@pytest.mark.generated
@pytest.mark.edge_case
def test_large_numbers_difference():
    """Verify the absolute difference with very large integers."""
    # arrange: num1 = 10**18; num2 = 10**18 + 5
    # act: AdvancedCalculator.absolute_difference(10**18, 10**18 + 5)
    # assert: result == 5
    num1 = 10**18
    num2 = 10**18 + 5
    result = AdvancedCalculator.absolute_difference(num1, num2)
    assert result == 5
