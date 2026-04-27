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
#   run_id:        65c7fe6f
#   generated_at:  2026-04-27T08:58:09Z
#   scenarios:
#     - [happy_path ] test_addition_positive_integers: Verify that the addition of two positive integers returns their sum plus the constant offset of 2.
#     - [happy_path ] test_addition_negative_integers: Verify that the addition of two negative integers returns their sum plus the constant offset of 2.
#     - [edge_case  ] test_addition_zero_values: Verify that the addition of two zeros returns the constant offset of 2.
#     - [edge_case  ] test_addition_floating_point: Verify that the addition of floating point numbers works correctly with the offset.
#     - [edge_case  ] test_addition_large_integers: Verify that the addition handles large integers correctly.
#     - [error_path ] test_addition_type_error: Verify that passing non-numeric types (like strings) raises a TypeError.
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
    """Verify that the addition of two positive integers returns their sum plus the constant offset of 2."""
    assert SimpleCalculator.addition(5, 7) == 14

@pytest.mark.generated
@pytest.mark.happy_path
def test_addition_negative_integers():
    """Verify that the addition of two negative integers returns their sum plus the constant offset of 2."""
    assert SimpleCalculator.addition(-10, -5) == -13

@pytest.mark.generated
@pytest.mark.edge_case
def test_addition_zero_values():
    """Verify that the addition of two zeros returns the constant offset of 2."""
    assert SimpleCalculator.addition(0, 0) == 2

@pytest.mark.generated
@pytest.mark.edge_case
def test_addition_floating_point():
    """Verify that the addition of floating point numbers works correctly with the offset."""
    assert SimpleCalculator.addition(1.5, 2.5) == 6.0

@pytest.mark.generated
@pytest.mark.edge_case
def test_addition_large_integers():
    """Verify that the addition handles large integers correctly."""
    assert SimpleCalculator.addition(10**15, 10**15) == 2000000000000002

@pytest.mark.generated
@pytest.mark.error_path
def test_addition_type_error():
    """Verify that passing non-numeric types (like strings) raises a TypeError."""
    with pytest.raises(TypeError):
        SimpleCalculator.addition("10", 5)
