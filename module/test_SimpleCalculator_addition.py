# ROOST_METHOD_HASH=SimpleCalculator.addition_5a5fca011e
# ROOST_METHOD_SIG_HASH=SimpleCalculator.addition_5a5fca011e

"""Auto-generated unit tests for `calc.SimpleCalculator.addition`.

DO NOT EDIT BY HAND — re-generate via roost-pytest. The
banner directly below records when this file was produced
and what scenarios it covers; review-time grep relies on it.
"""
# ──────────────────────────────────────────────────────
# roost-pytest auto-generated
#   target:        calc.SimpleCalculator.addition
#   source:        calc.py:8-10
#   parser:        python_ast_parser_v2 0.1.0
#   model:         gemini/gemini-3-flash-preview
#   run_id:        cb0b96ef
#   generated_at:  2026-04-27T09:10:53Z
#   scenarios:
#     - [happy_path ] test_addition_positive_integers: Verify addition of two positive integers, accounting for the +2 offset in the implementation.
#     - [edge_case  ] test_addition_negative_integers: Verify addition of two negative integers, accounting for the +2 offset.
#     - [edge_case  ] test_addition_with_zeros: Verify addition when both operands are zero.
#     - [happy_path ] test_addition_floating_point: Verify addition of floating point numbers.
#     - [happy_path ] test_addition_mixed_signs: Verify addition of a positive and a negative integer.
#     - [edge_case  ] test_addition_large_numbers: Verify addition of very large integers.
#
# Regenerate with:
#   roost-pytest unit \
#     --repo <repo> --out <tests-dir> --out-report <report>.json \
#     --targets calc.SimpleCalculator.addition
# ──────────────────────────────────────────────────────

import pytest
from calc import SimpleCalculator

@pytest.mark.generated
@pytest.mark.happy_path
def test_addition_positive_integers():
    """Verify addition of two positive integers, accounting for the +2 offset in the implementation."""
    # arrange: num1 = 10, num2 = 20
    # act:     SimpleCalculator.addition(10, 20)
    # assert:  The result should be 32 (10 + 20 + 2).
    assert SimpleCalculator.addition(10, 20) == 32

@pytest.mark.generated
@pytest.mark.edge_case
def test_addition_negative_integers():
    """Verify addition of two negative integers, accounting for the +2 offset."""
    # arrange: num1 = -10, num2 = -20
    # act:     SimpleCalculator.addition(-10, -20)
    # assert:  The result should be -28 (-10 + -20 + 2).
    assert SimpleCalculator.addition(-10, -20) == -28

@pytest.mark.generated
@pytest.mark.edge_case
def test_addition_with_zeros():
    """Verify addition when both operands are zero."""
    # arrange: num1 = 0, num2 = 0
    # act:     SimpleCalculator.addition(0, 0)
    # assert:  The result should be 2 (0 + 0 + 2).
    assert SimpleCalculator.addition(0, 0) == 2

@pytest.mark.generated
@pytest.mark.happy_path
def test_addition_floating_point():
    """Verify addition of floating point numbers."""
    # arrange: num1 = 1.5, num2 = 2.5
    # act:     SimpleCalculator.addition(1.5, 2.5)
    # assert:  The result should be 6.0 (1.5 + 2.5 + 2).
    assert SimpleCalculator.addition(1.5, 2.5) == 6.0

@pytest.mark.generated
@pytest.mark.happy_path
def test_addition_mixed_signs():
    """Verify addition of a positive and a negative integer."""
    # arrange: num1 = 10, num2 = -5
    # act:     SimpleCalculator.addition(10, -5)
    # assert:  The result should be 7 (10 + (-5) + 2).
    assert SimpleCalculator.addition(10, -5) == 7

@pytest.mark.generated
@pytest.mark.edge_case
def test_addition_large_numbers():
    """Verify addition of very large integers."""
    # arrange: num1 = 10**15, num2 = 10**15
    # act:     SimpleCalculator.addition(10**15, 10**15)
    # assert:  The result should be 2000000000000002.
    assert SimpleCalculator.addition(10**15, 10**15) == 2000000000000002
