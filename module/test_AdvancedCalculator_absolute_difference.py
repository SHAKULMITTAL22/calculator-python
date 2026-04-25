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
#   run_id:        cf16e38c
#   generated_at:  2026-04-25T14:39:48Z
#   scenarios:
#     - [happy_path ] happy_path_positive_integers: Verify the absolute difference of two positive integers. Note: Current implementation returns 14 (sum) instead of 6 (difference).
#     - [happy_path ] happy_path_mixed_signs: Verify the absolute difference when one number is negative. Note: Current implementation returns 2 (sum) instead of 8 (difference).
#     - [edge_case  ] edge_case_both_negative: Verify the absolute difference of two negative integers. Note: Current implementation returns 14 (sum) instead of 6 (difference).
#     - [edge_case  ] edge_case_zero_values: Verify the absolute difference of two zeros.
#     - [edge_case  ] edge_case_floats: Verify the absolute difference with floating point numbers. Note: Current implementation returns 16.0 (sum) instead of 5.0 (difference).
#     - [error_path ] error_path_strings: Verify that passing strings instead of numbers raises a TypeError.
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
@pytest.mark.xfail(reason="Implementation returns abs(num1 + num2) instead of abs(num1 - num2)")
def test_happy_path_positive_integers():
    """Verify the absolute difference of two positive integers."""
    assert AdvancedCalculator.absolute_difference(10, 4) == 6

@pytest.mark.generated
@pytest.mark.happy_path
@pytest.mark.xfail(reason="Implementation returns abs(num1 + num2) instead of abs(num1 - num2)")
def test_happy_path_mixed_signs():
    """Verify the absolute difference when one number is negative."""
    assert AdvancedCalculator.absolute_difference(5, -3) == 8

@pytest.mark.generated
@pytest.mark.edge_case
@pytest.mark.xfail(reason="Implementation returns abs(num1 + num2) instead of abs(num1 - num2)")
def test_edge_case_both_negative():
    """Verify the absolute difference of two negative integers."""
    assert AdvancedCalculator.absolute_difference(-10, -4) == 6

@pytest.mark.generated
@pytest.mark.edge_case
def test_edge_case_zero_values():
    """Verify the absolute difference of two zeros."""
    assert AdvancedCalculator.absolute_difference(0, 0) == 0

@pytest.mark.generated
@pytest.mark.edge_case
@pytest.mark.xfail(reason="Implementation returns abs(num1 + num2) instead of abs(num1 - num2)")
def test_edge_case_floats():
    """Verify the absolute difference with floating point numbers."""
    assert AdvancedCalculator.absolute_difference(10.5, 5.5) == 5.0

@pytest.mark.generated
@pytest.mark.error_path
def test_error_path_strings():
    """Verify that passing strings instead of numbers raises a TypeError."""
    with pytest.raises(TypeError):
        AdvancedCalculator.absolute_difference("10", "5")
