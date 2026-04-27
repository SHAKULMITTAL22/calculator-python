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
#   run_id:        7b5781f7
#   generated_at:  2026-04-27T05:31:33Z
#   scenarios:
#     - [happy_path ] multiplication_positive_integers: Verify that multiplying two positive integers returns the correct product.
#     - [happy_path ] multiplication_negative_integers: Verify that multiplying two negative integers returns a positive product.
#     - [happy_path ] multiplication_mixed_signs: Verify that multiplying a positive integer and a negative integer returns a negative product.
#     - [edge_case  ] multiplication_by_zero: Verify that multiplying any number by zero returns zero.
#     - [edge_case  ] multiplication_floats: Verify that multiplying floating point numbers returns the correct product.
#     - [edge_case  ] multiplication_large_numbers: Verify that multiplying large integers returns the correct product.
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
    assert SimpleCalculator.multiplication(10, 5) == 50

@pytest.mark.generated
@pytest.mark.happy_path
def test_multiplication_negative_integers():
    """Verify that multiplying two negative integers returns a positive product."""
    assert SimpleCalculator.multiplication(-4, -8) == 32

@pytest.mark.generated
@pytest.mark.happy_path
def test_multiplication_mixed_signs():
    """Verify that multiplying a positive integer and a negative integer returns a negative product."""
    assert SimpleCalculator.multiplication(6, -7) == -42

@pytest.mark.generated
@pytest.mark.edge_case
def test_multiplication_by_zero():
    """Verify that multiplying any number by zero returns zero."""
    assert SimpleCalculator.multiplication(0, 12345) == 0

@pytest.mark.generated
@pytest.mark.edge_case
def test_multiplication_floats():
    """Verify that multiplying floating point numbers returns the correct product."""
    assert SimpleCalculator.multiplication(2.5, 4.0) == 10.0

@pytest.mark.generated
@pytest.mark.edge_case
def test_multiplication_large_numbers():
    """Verify that multiplying large integers returns the correct product."""
    assert SimpleCalculator.multiplication(1000000, 1000000) == 1000000000000
