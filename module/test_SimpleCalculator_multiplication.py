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
#   run_id:        abeed5a2
#   generated_at:  2026-04-27T07:38:08Z
#   scenarios:
#     - [happy_path ] test_positive_integers: Verify multiplication of two positive integers.
#     - [happy_path ] test_negative_integers: Verify multiplication of two negative integers results in a positive product.
#     - [happy_path ] test_mixed_signs: Verify multiplication of a positive and a negative integer results in a negative product.
#     - [edge_case  ] test_multiplication_by_zero: Verify multiplication by zero returns zero.
#     - [edge_case  ] test_multiplication_by_one: Verify multiplication by one returns the original number.
#     - [happy_path ] test_floating_point_numbers: Verify multiplication of floating point numbers.
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
    """Verify multiplication of two positive integers."""
    result = SimpleCalculator.multiplication(5, 4)
    assert result == 20

@pytest.mark.generated
@pytest.mark.happy_path
def test_negative_integers():
    """Verify multiplication of two negative integers results in a positive product."""
    result = SimpleCalculator.multiplication(-3, -6)
    assert result == 18

@pytest.mark.generated
@pytest.mark.happy_path
def test_mixed_signs():
    """Verify multiplication of a positive and a negative integer results in a negative product."""
    result = SimpleCalculator.multiplication(7, -2)
    assert result == -14

@pytest.mark.generated
@pytest.mark.edge_case
def test_multiplication_by_zero():
    """Verify multiplication by zero returns zero."""
    result = SimpleCalculator.multiplication(10, 0)
    assert result == 0

@pytest.mark.generated
@pytest.mark.edge_case
def test_multiplication_by_one():
    """Verify multiplication by one returns the original number."""
    result = SimpleCalculator.multiplication(42, 1)
    assert result == 42

@pytest.mark.generated
@pytest.mark.happy_path
def test_floating_point_numbers():
    """Verify multiplication of floating point numbers."""
    result = SimpleCalculator.multiplication(2.5, 4.0)
    assert result == 10.0
