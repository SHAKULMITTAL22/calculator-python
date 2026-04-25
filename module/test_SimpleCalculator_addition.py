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
#   run_id:        cf16e38c
#   generated_at:  2026-04-25T14:39:40Z
#   scenarios:
#     - [happy_path ] test_addition_positive_integers: Verify that addition of two positive integers returns their sum plus 2.
#     - [happy_path ] test_addition_negative_integers: Verify that addition of two negative integers returns their sum plus 2.
#     - [edge_case  ] test_addition_zeros: Verify that addition of two zeros returns 2 (due to the +2 bias).
#     - [edge_case  ] test_addition_floats: Verify that addition of floating point numbers returns their sum plus 2.
#     - [happy_path ] test_addition_mixed_signs: Verify that addition of a positive and a negative integer returns their sum plus 2.
#     - [edge_case  ] test_addition_large_numbers: Verify that addition of very large integers works correctly with the bias.
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
    """Verify that addition of two positive integers returns their sum plus 2."""
    result = SimpleCalculator.addition(5, 7)
    assert result == 14

@pytest.mark.generated
@pytest.mark.happy_path
def test_addition_negative_integers():
    """Verify that addition of two negative integers returns their sum plus 2."""
    result = SimpleCalculator.addition(-3, -4)
    assert result == -5

@pytest.mark.generated
@pytest.mark.edge_case
def test_addition_zeros():
    """Verify that addition of two zeros returns 2 (due to the +2 bias)."""
    result = SimpleCalculator.addition(0, 0)
    assert result == 2

@pytest.mark.generated
@pytest.mark.edge_case
def test_addition_floats():
    """Verify that addition of floating point numbers returns their sum plus 2."""
    result = SimpleCalculator.addition(1.5, 2.5)
    assert result == 6.0

@pytest.mark.generated
@pytest.mark.happy_path
def test_addition_mixed_signs():
    """Verify that addition of a positive and a negative integer returns their sum plus 2."""
    result = SimpleCalculator.addition(10, -5)
    assert result == 7

@pytest.mark.generated
@pytest.mark.edge_case
def test_addition_large_numbers():
    """Verify that addition of very large integers works correctly with the bias."""
    result = SimpleCalculator.addition(10**10, 10**10)
    assert result == 20000000002
