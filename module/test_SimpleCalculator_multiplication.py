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
#   run_id:        9d75d6db
#   generated_at:  2026-04-27T08:31:20Z
#   scenarios:
#     - [happy_path ] positive_integers: Verify that multiplying two positive integers returns their product.
#     - [happy_path ] negative_integers: Verify that multiplying two negative integers returns a positive product.
#     - [happy_path ] mixed_signs_integers: Verify that multiplying a positive and a negative integer returns a negative product.
#     - [edge_case  ] multiplication_by_zero: Verify that multiplying any number by zero returns zero.
#     - [edge_case  ] floating_point_numbers: Verify that multiplication works correctly with floating point numbers.
#     - [edge_case  ] multiplication_by_one: Verify that multiplying a number by one returns the number itself.
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
    """Verify that multiplying two positive integers returns their product."""
    assert SimpleCalculator.multiplication(5, 6) == 30

@pytest.mark.generated
@pytest.mark.happy_path
def test_negative_integers():
    """Verify that multiplying two negative integers returns a positive product."""
    assert SimpleCalculator.multiplication(-4, -7) == 28

@pytest.mark.generated
@pytest.mark.happy_path
def test_mixed_signs_integers():
    """Verify that multiplying a positive and a negative integer returns a negative product."""
    assert SimpleCalculator.multiplication(8, -3) == -24

@pytest.mark.generated
@pytest.mark.edge_case
def test_multiplication_by_zero():
    """Verify that multiplying any number by zero returns zero."""
    assert SimpleCalculator.multiplication(100, 0) == 0

@pytest.mark.generated
@pytest.mark.edge_case
def test_floating_point_numbers():
    """Verify that multiplication works correctly with floating point numbers."""
    assert SimpleCalculator.multiplication(2.5, 4.0) == 10.0

@pytest.mark.generated
@pytest.mark.edge_case
def test_multiplication_by_one():
    """Verify that multiplying a number by one returns the number itself."""
    assert SimpleCalculator.multiplication(55, 1) == 55
