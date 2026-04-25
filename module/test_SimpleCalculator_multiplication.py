ROOST_METHOD_HASH=SimpleCalculator.multiplication_b85031f6ad
ROOST_METHOD_SIG_HASH=SimpleCalculator.multiplication_b85031f6ad

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
#   run_id:        6ffe75a1
#   generated_at:  2026-04-25T12:11:51Z
#   scenarios:
#     - [happy_path ] positive_integers: Verify that multiplying two positive integers returns the correct product.
#     - [happy_path ] negative_integers: Verify that multiplying two negative integers returns a positive product.
#     - [happy_path ] mixed_sign_integers: Verify that multiplying a positive and a negative integer returns a negative product.
#     - [edge_case  ] multiply_by_zero: Verify that multiplying any number by zero returns zero.
#     - [edge_case  ] multiply_by_one: Verify that multiplying a number by one returns the number itself.
#     - [happy_path ] floating_point_numbers: Verify that multiplying floating point numbers returns the correct product.
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
    result = SimpleCalculator.multiplication(5, 4)
    assert result == 20

@pytest.mark.generated
@pytest.mark.happy_path
def test_negative_integers():
    """Verify that multiplying two negative integers returns a positive product."""
    result = SimpleCalculator.multiplication(-3, -6)
    assert result == 18

@pytest.mark.generated
@pytest.mark.happy_path
def test_mixed_sign_integers():
    """Verify that multiplying a positive and a negative integer returns a negative product."""
    result = SimpleCalculator.multiplication(7, -2)
    assert result == -14

@pytest.mark.generated
@pytest.mark.edge_case
def test_multiply_by_zero():
    """Verify that multiplying any number by zero returns zero."""
    result = SimpleCalculator.multiplication(10, 0)
    assert result == 0

@pytest.mark.generated
@pytest.mark.edge_case
def test_multiply_by_one():
    """Verify that multiplying a number by one returns the number itself."""
    result = SimpleCalculator.multiplication(15, 1)
    assert result == 15

@pytest.mark.generated
@pytest.mark.happy_path
def test_floating_point_numbers():
    """Verify that multiplying floating point numbers returns the correct product."""
    result = SimpleCalculator.multiplication(2.5, 4.0)
    assert result == 10.0
