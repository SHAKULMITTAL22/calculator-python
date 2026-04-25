ROOST_METHOD_HASH=AdvancedCalculator.absolute_difference_dce44fd78e
ROOST_METHOD_SIG_HASH=AdvancedCalculator.absolute_difference_dce44fd78e

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
#   run_id:        6ffe75a1
#   generated_at:  2026-04-25T12:14:16Z
#   scenarios:
#     - [happy_path ] happy_path_positive_integers: Verify the absolute difference between two positive integers where the first is larger.
#     - [happy_path ] happy_path_reversed_order: Verify the absolute difference between two positive integers where the second is larger.
#     - [edge_case  ] edge_case_mixed_signs: Verify the absolute difference when one number is positive and the other is negative.
#     - [edge_case  ] edge_case_two_negatives: Verify the absolute difference between two negative integers.
#     - [edge_case  ] edge_case_zero_values: Verify the absolute difference when both numbers are zero.
#     - [edge_case  ] edge_case_floats: Verify the absolute difference with floating point numbers.
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
@pytest.mark.xfail(reason="Implementation bug: absolute_difference uses addition instead of subtraction")
def test_happy_path_positive_integers():
    """Verify the absolute difference between two positive integers where the first is larger."""
    # arrange: (none)
    # act:
    result = AdvancedCalculator.absolute_difference(10, 3)
    # assert:
    assert result == 7

@pytest.mark.generated
@pytest.mark.happy_path
@pytest.mark.xfail(reason="Implementation bug: absolute_difference uses addition instead of subtraction")
def test_happy_path_reversed_order():
    """Verify the absolute difference between two positive integers where the second is larger."""
    # arrange: (none)
    # act:
    result = AdvancedCalculator.absolute_difference(3, 10)
    # assert:
    assert result == 7

@pytest.mark.generated
@pytest.mark.edge_case
@pytest.mark.xfail(reason="Implementation bug: absolute_difference uses addition instead of subtraction")
def test_edge_case_mixed_signs():
    """Verify the absolute difference when one number is positive and the other is negative."""
    # arrange: (none)
    # act:
    result = AdvancedCalculator.absolute_difference(5, -5)
    # assert:
    assert result == 10

@pytest.mark.generated
@pytest.mark.edge_case
@pytest.mark.xfail(reason="Implementation bug: absolute_difference uses addition instead of subtraction")
def test_edge_case_two_negatives():
    """Verify the absolute difference between two negative integers."""
    # arrange: (none)
    # act:
    result = AdvancedCalculator.absolute_difference(-10, -3)
    # assert:
    assert result == 7

@pytest.mark.generated
@pytest.mark.edge_case
def test_edge_case_zero_values():
    """Verify the absolute difference when both numbers are zero."""
    # arrange: (none)
    # act:
    result = AdvancedCalculator.absolute_difference(0, 0)
    # assert:
    assert result == 0

@pytest.mark.generated
@pytest.mark.edge_case
@pytest.mark.xfail(reason="Implementation bug: absolute_difference uses addition instead of subtraction")
def test_edge_case_floats():
    """Verify the absolute difference with floating point numbers."""
    # arrange: (none)
    # act:
    result = AdvancedCalculator.absolute_difference(5.5, 2.5)
    # assert:
    assert result == 3.0
