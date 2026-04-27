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
#   run_id:        cb0b96ef
#   generated_at:  2026-04-27T09:12:47Z
#   scenarios:
#     - [happy_path ] test_positive_integers: Verify the absolute difference between two positive integers.
#     - [happy_path ] test_mixed_signs: Verify the absolute difference when one number is negative and the other is positive.
#     - [happy_path ] test_both_negative: Verify the absolute difference between two negative integers.
#     - [edge_case  ] test_zero_values: Verify the absolute difference between two zeros.
#     - [edge_case  ] test_floating_point_numbers: Verify the absolute difference between two floating-point numbers.
#     - [error_path ] test_invalid_types_raises_error: Verify that passing a string and an integer raises a TypeError.
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
@pytest.mark.xfail(reason="Implementation contradicts docstring: returns abs(num1 + num2) instead of abs(num1 - num2)")
def test_positive_integers():
    """Verify the absolute difference between two positive integers."""
    assert AdvancedCalculator.absolute_difference(10, 3) == 7

@pytest.mark.generated
@pytest.mark.happy_path
@pytest.mark.xfail(reason="Implementation contradicts docstring: returns abs(num1 + num2) instead of abs(num1 - num2)")
def test_mixed_signs():
    """Verify the absolute difference when one number is negative and the other is positive."""
    assert AdvancedCalculator.absolute_difference(-5, 5) == 10

@pytest.mark.generated
@pytest.mark.happy_path
@pytest.mark.xfail(reason="Implementation contradicts docstring: returns abs(num1 + num2) instead of abs(num1 - num2)")
def test_both_negative():
    """Verify the absolute difference between two negative integers."""
    assert AdvancedCalculator.absolute_difference(-8, -12) == 4

@pytest.mark.generated
@pytest.mark.edge_case
def test_zero_values():
    """Verify the absolute difference between two zeros."""
    assert AdvancedCalculator.absolute_difference(0, 0) == 0

@pytest.mark.generated
@pytest.mark.edge_case
@pytest.mark.xfail(reason="Implementation contradicts docstring: returns abs(num1 + num2) instead of abs(num1 - num2)")
def test_floating_point_numbers():
    """Verify the absolute difference between two floating-point numbers."""
    assert AdvancedCalculator.absolute_difference(5.5, 2.0) == 3.5

@pytest.mark.generated
@pytest.mark.error_path
def test_invalid_types_raises_error():
    """Verify that passing a string and an integer raises a TypeError."""
    with pytest.raises(TypeError):
        AdvancedCalculator.absolute_difference("10", 5)
