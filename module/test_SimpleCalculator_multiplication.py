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
#   run_id:        cb0b96ef
#   generated_at:  2026-04-27T09:10:48Z
#   scenarios:
#     - [happy_path ] positive_integers: Verify that multiplying two positive integers returns the correct product.
#     - [happy_path ] negative_integers: Verify that multiplying two negative integers returns a positive product.
#     - [happy_path ] mixed_signs_integers: Verify that multiplying a positive and a negative integer returns a negative product.
#     - [edge_case  ] multiplication_by_zero: Verify that multiplying any number by zero returns zero.
#     - [edge_case  ] multiplication_by_one: Verify that multiplying any number by one returns the number itself.
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
    result = SimpleCalculator.multiplication(10, 5)
    assert result == 50

@pytest.mark.generated
@pytest.mark.happy_path
def test_negative_integers():
    """Verify that multiplying two negative integers returns a positive product."""
    result = SimpleCalculator.multiplication(-4, -8)
    assert result == 32

@pytest.mark.generated
@pytest.mark.happy_path
def test_mixed_signs_integers():
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
    """Verify that multiplying any number by one returns the number itself."""
    result = SimpleCalculator.multiplication(1, 99)
    assert result == 99

@pytest.mark.generated
@pytest.mark.happy_path
def test_floating_point_numbers():
    """Verify that multiplying floating point numbers returns the correct product."""
    result = SimpleCalculator.multiplication(0.5, 2.0)
    assert result == 1.0
