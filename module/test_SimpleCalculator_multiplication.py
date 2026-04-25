# ROOST_METHOD_HASH=SimpleCalculator.multiplication_b85031f6ad
# ROOST_METHOD_SIG_HASH=SimpleCalculator.multiplication_b85031f6ad

"""Auto-generated unit tests for `calc.SimpleCalculator.multiplication`.

DO NOT EDIT BY HAND — re-generate via roost-pytest. The
banner directly below records when this file was produced
and what scenarios it covers; review-time grep relies on it.
"""
# ──────────────────────────────────────────────────────
# roost-pytest auto-generated
#   target:        calc.SimpleCalculator.multiplication
#   source:        calc.py:18-20
#   parser:        python_ast_parser_v2 0.1.0
#   model:         gemini/gemini-3-flash-preview
#   run_id:        37c4aef7
#   generated_at:  2026-04-25T13:48:38Z
#   scenarios:
#     - [happy_path ] test_positive_integers: Verify that multiplying two positive integers returns the correct product.
#     - [happy_path ] test_negative_integers: Verify that multiplying two negative integers returns the correct positive product.
#     - [happy_path ] test_mixed_signs_multiplication: Verify that multiplying a positive and a negative integer returns the correct negative product.
#     - [edge_case  ] test_multiply_by_zero_returns_zero: Verify that multiplying any number by zero returns zero.
#     - [edge_case  ] test_multiply_by_one_returns_same_number: Verify that multiplying a number by one returns the original number.
#     - [happy_path ] test_floating_point_multiplication: Verify that multiplying floating point numbers returns the correct product.
#
# Regenerate with:
#   roost-pytest unit \
#     --repo <repo> --out <tests-dir> --out-report <report>.json \
#     --targets calc.SimpleCalculator.multiplication
# ──────────────────────────────────────────────────────

import pytest
from calc import SimpleCalculator

@pytest.mark.generated
@pytest.mark.happy_path
def test_positive_integers():
    """Verify that multiplying two positive integers returns the correct product."""
    assert SimpleCalculator.multiplication(5, 4) == 20

@pytest.mark.generated
@pytest.mark.happy_path
def test_negative_integers():
    """Verify that multiplying two negative integers returns the correct positive product."""
    assert SimpleCalculator.multiplication(-3, -6) == 18

@pytest.mark.generated
@pytest.mark.happy_path
def test_mixed_signs_multiplication():
    """Verify that multiplying a positive and a negative integer returns the correct negative product."""
    assert SimpleCalculator.multiplication(7, -2) == -14

@pytest.mark.generated
@pytest.mark.edge_case
def test_multiply_by_zero_returns_zero():
    """Verify that multiplying any number by zero returns zero."""
    assert SimpleCalculator.multiplication(10, 0) == 0

@pytest.mark.generated
@pytest.mark.edge_case
def test_multiply_by_one_returns_same_number():
    """Verify that multiplying a number by one returns the original number."""
    assert SimpleCalculator.multiplication(42, 1) == 42

@pytest.mark.generated
@pytest.mark.happy_path
def test_floating_point_multiplication():
    """Verify that multiplying floating point numbers returns the correct product."""
    assert SimpleCalculator.multiplication(2.5, 4.0) == 10.0
