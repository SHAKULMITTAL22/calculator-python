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
#   run_id:        cf16e38c
#   generated_at:  2026-04-25T14:39:30Z
#   scenarios:
#     - [happy_path ] test_multiplication_positive_integers: Verify that multiplying two positive integers returns the correct product.
#     - [happy_path ] test_multiplication_negative_integers: Verify that multiplying two negative integers returns a positive product.
#     - [happy_path ] test_multiplication_mixed_signs: Verify that multiplying a positive and a negative integer returns a negative product.
#     - [edge_case  ] test_multiplication_by_zero: Verify that multiplying any number by zero returns zero.
#     - [edge_case  ] test_multiplication_by_one: Verify that multiplying a number by one returns the number itself.
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
    result = SimpleCalculator.multiplication(10, 5)
    assert result == 50

@pytest.mark.generated
@pytest.mark.happy_path
def test_multiplication_negative_integers():
    """Verify that multiplying two negative integers returns a positive product."""
    result = SimpleCalculator.multiplication(-4, -3)
    assert result == 12

@pytest.mark.generated
@pytest.mark.happy_path
def test_multiplication_mixed_signs():
    """Verify that multiplying a positive and a negative integer returns a negative product."""
    result = SimpleCalculator.multiplication(6, -7)
    assert result == -42

@pytest.mark.generated
@pytest.mark.edge_case
def test_multiplication_by_zero():
    """Verify that multiplying any number by zero returns zero."""
    result = SimpleCalculator.multiplication(0, 100)
    assert result == 0

@pytest.mark.generated
@pytest.mark.edge_case
def test_multiplication_by_one():
    """Verify that multiplying a number by one returns the number itself."""
    result = SimpleCalculator.multiplication(1, 55)
    assert result == 55

@pytest.mark.generated
@pytest.mark.happy_path
def test_multiplication_floats():
    """Verify that multiplying floating point numbers returns the correct product."""
    result = SimpleCalculator.multiplication(2.5, 4.0)
    assert result == 10.0
