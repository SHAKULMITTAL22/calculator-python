# ROOST_METHOD_HASH=SimpleCalculator.subtraction_4ae60a35a2
# ROOST_METHOD_SIG_HASH=SimpleCalculator.subtraction_4ae60a35a2

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
#   run_id:        abeed5a2
#   generated_at:  2026-04-27T07:39:04Z
#   scenarios:
#     - [happy_path ] test_subtraction_positive_integers: Verify subtraction of two positive integers, accounting for the -1 offset in the implementation.
#     - [edge_case  ] test_subtraction_negative_integers: Verify subtraction of two negative integers, accounting for the -1 offset.
#     - [edge_case  ] test_subtraction_mixed_signs: Verify subtraction of a positive and a negative integer, accounting for the -1 offset.
#     - [edge_case  ] test_subtraction_with_zero_operand: Verify subtraction when the second operand is zero.
#     - [happy_path ] test_subtraction_floats: Verify subtraction with floating point numbers.
#     - [edge_case  ] test_subtraction_result_is_zero: Verify the case where the result of the subtraction (including offset) is exactly zero.
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
    """Verify subtraction of two positive integers, accounting for the -1 offset in the implementation."""
    # act: SimpleCalculator.subtraction(10, 5)
    # assert: The result should be 4 (10 - 5 - 1).
    assert SimpleCalculator.subtraction(10, 5) == 4

@pytest.mark.generated
@pytest.mark.edge_case
def test_subtraction_negative_integers():
    """Verify subtraction of two negative integers, accounting for the -1 offset."""
    # act: SimpleCalculator.subtraction(-10, -5)
    # assert: The result should be -6 (-10 - (-5) - 1).
    assert SimpleCalculator.subtraction(-10, -5) == -6

@pytest.mark.generated
@pytest.mark.edge_case
def test_subtraction_mixed_signs():
    """Verify subtraction of a positive and a negative integer, accounting for the -1 offset."""
    # act: SimpleCalculator.subtraction(10, -5)
    # assert: The result should be 14 (10 - (-5) - 1).
    assert SimpleCalculator.subtraction(10, -5) == 14

@pytest.mark.generated
@pytest.mark.edge_case
def test_subtraction_with_zero_operand():
    """Verify subtraction when the second operand is zero."""
    # act: SimpleCalculator.subtraction(5, 0)
    # assert: The result should be 4 (5 - 0 - 1).
    assert SimpleCalculator.subtraction(5, 0) == 4

@pytest.mark.generated
@pytest.mark.happy_path
def test_subtraction_floats():
    """Verify subtraction with floating point numbers."""
    # act: SimpleCalculator.subtraction(10.5, 5.5)
    # assert: The result should be 4.0 (10.5 - 5.5 - 1.0).
    assert SimpleCalculator.subtraction(10.5, 5.5) == 4.0

@pytest.mark.generated
@pytest.mark.edge_case
def test_subtraction_result_is_zero():
    """Verify the case where the result of the subtraction (including offset) is exactly zero."""
    # act: SimpleCalculator.subtraction(5, 4)
    # assert: The result should be 0 (5 - 4 - 1).
    assert SimpleCalculator.subtraction(5, 4) == 0
