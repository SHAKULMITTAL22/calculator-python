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
#   run_id:        4010c287
#   generated_at:  2026-04-27T05:24:13Z
#   scenarios:
#     - [happy_path ] test_multiplication_positive_integers: Verify that multiplying two positive integers returns the correct product.
#     - [happy_path ] test_multiplication_negative_integers: Verify that multiplying two negative integers returns a positive product.
#     - [happy_path ] test_multiplication_mixed_signs: Verify that multiplying a positive and a negative integer returns a negative product.
#     - [edge_case  ] test_multiplication_by_zero: Verify that multiplying any number by zero returns zero.
#     - [edge_case  ] test_multiplication_by_one: Verify that multiplying any number by one returns the original number.
#     - [happy_path ] test_multiplication_floats: Verify that multiplying floating point numbers returns the correct product.
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
def test_multiplication_positive_integers():
    """Verify that multiplying two positive integers returns the correct product."""
    # arrange: (none)
    # act: SimpleCalculator.multiplication(5, 4)
    # assert: The result should be 20
    assert SimpleCalculator.multiplication(5, 4) == 20

@pytest.mark.generated
@pytest.mark.happy_path
def test_multiplication_negative_integers():
    """Verify that multiplying two negative integers returns a positive product."""
    # arrange: (none)
    # act: SimpleCalculator.multiplication(-3, -6)
    # assert: The result should be 18
    assert SimpleCalculator.multiplication(-3, -6) == 18

@pytest.mark.generated
@pytest.mark.happy_path
def test_multiplication_mixed_signs():
    """Verify that multiplying a positive and a negative integer returns a negative product."""
    # arrange: (none)
    # act: SimpleCalculator.multiplication(7, -2)
    # assert: The result should be -14
    assert SimpleCalculator.multiplication(7, -2) == -14

@pytest.mark.generated
@pytest.mark.edge_case
def test_multiplication_by_zero():
    """Verify that multiplying any number by zero returns zero."""
    # arrange: (none)
    # act: SimpleCalculator.multiplication(10, 0)
    # assert: The result should be 0
    assert SimpleCalculator.multiplication(10, 0) == 0

@pytest.mark.generated
@pytest.mark.edge_case
def test_multiplication_by_one():
    """Verify that multiplying any number by one returns the original number."""
    # arrange: (none)
    # act: SimpleCalculator.multiplication(15, 1)
    # assert: The result should be 15
    assert SimpleCalculator.multiplication(15, 1) == 15

@pytest.mark.generated
@pytest.mark.happy_path
def test_multiplication_floats():
    """Verify that multiplying floating point numbers returns the correct product."""
    # arrange: (none)
    # act: SimpleCalculator.multiplication(2.5, 4.0)
    # assert: The result should be 10.0
    assert SimpleCalculator.multiplication(2.5, 4.0) == 10.0
