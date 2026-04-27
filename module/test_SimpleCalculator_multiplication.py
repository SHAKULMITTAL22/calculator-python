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
#   run_id:        7dd18b11
#   generated_at:  2026-04-27T08:04:50Z
#   scenarios:
#     - [happy_path ] positive_integers: Verify multiplication of two positive integers.
#     - [happy_path ] negative_integers: Verify multiplication of two negative integers results in a positive product.
#     - [happy_path ] mixed_signs: Verify multiplication of a positive and a negative integer results in a negative product.
#     - [edge_case  ] multiplication_by_zero: Verify that multiplying any number by zero results in zero.
#     - [happy_path ] floating_point: Verify multiplication with floating point numbers.
#     - [edge_case  ] large_numbers: Verify multiplication of large integers.
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
    result = SimpleCalculator.multiplication(5, 6)
    assert result == 30

@pytest.mark.generated
@pytest.mark.happy_path
def test_negative_integers():
    """Verify multiplication of two negative integers results in a positive product."""
    result = SimpleCalculator.multiplication(-4, -7)
    assert result == 28

@pytest.mark.generated
@pytest.mark.happy_path
def test_mixed_signs():
    """Verify multiplication of a positive and a negative integer results in a negative product."""
    result = SimpleCalculator.multiplication(8, -3)
    assert result == -24

@pytest.mark.generated
@pytest.mark.edge_case
def test_multiplication_by_zero():
    """Verify that multiplying any number by zero results in zero."""
    result = SimpleCalculator.multiplication(123, 0)
    assert result == 0

@pytest.mark.generated
@pytest.mark.happy_path
def test_floating_point():
    """Verify multiplication with floating point numbers."""
    result = SimpleCalculator.multiplication(2.5, 4.0)
    assert result == 10.0

@pytest.mark.generated
@pytest.mark.edge_case
def test_large_numbers():
    """Verify multiplication of large integers."""
    result = SimpleCalculator.multiplication(10**6, 10**6)
    assert result == 10**12
