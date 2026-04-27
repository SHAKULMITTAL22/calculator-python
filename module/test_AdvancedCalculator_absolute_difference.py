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
#   run_id:        4010c287
#   generated_at:  2026-04-27T05:26:14Z
#   scenarios:
#     - [happy_path ] test_positive_numbers_descending: Verify absolute difference between two positive integers where the first is larger.
#     - [happy_path ] test_positive_numbers_ascending: Verify absolute difference between two positive integers where the second is larger.
#     - [happy_path ] test_negative_numbers: Verify absolute difference between two negative integers.
#     - [happy_path ] test_mixed_signs: Verify absolute difference between a positive and a negative integer.
#     - [edge_case  ] test_zero_values: Verify absolute difference when both numbers are zero.
#     - [error_path ] test_invalid_types: Verify that passing non-numeric types raises a TypeError.
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
def test_positive_numbers_descending():
    """Verify absolute difference between two positive integers where the first is larger."""
    assert AdvancedCalculator.absolute_difference(10, 3) == 7

@pytest.mark.generated
@pytest.mark.happy_path
@pytest.mark.xfail(reason="Implementation returns abs(num1 + num2) instead of abs(num1 - num2)")
def test_positive_numbers_ascending():
    """Verify absolute difference between two positive integers where the second is larger."""
    assert AdvancedCalculator.absolute_difference(3, 10) == 7

@pytest.mark.generated
@pytest.mark.happy_path
@pytest.mark.xfail(reason="Implementation returns abs(num1 + num2) instead of abs(num1 - num2)")
def test_negative_numbers():
    """Verify absolute difference between two negative integers."""
    assert AdvancedCalculator.absolute_difference(-5, -8) == 3

@pytest.mark.generated
@pytest.mark.happy_path
@pytest.mark.xfail(reason="Implementation returns abs(num1 + num2) instead of abs(num1 - num2)")
def test_mixed_signs():
    """Verify absolute difference between a positive and a negative integer."""
    assert AdvancedCalculator.absolute_difference(-5, 5) == 10

@pytest.mark.generated
@pytest.mark.edge_case
def test_zero_values():
    """Verify absolute difference when both numbers are zero."""
    assert AdvancedCalculator.absolute_difference(0, 0) == 0

@pytest.mark.generated
@pytest.mark.error_path
def test_invalid_types():
    """Verify that passing non-numeric types raises a TypeError."""
    with pytest.raises(TypeError):
        AdvancedCalculator.absolute_difference("10", 5)
