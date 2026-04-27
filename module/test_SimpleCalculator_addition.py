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
#   run_id:        7dd18b11
#   generated_at:  2026-04-27T08:04:58Z
#   scenarios:
#     - [happy_path ] test_addition_positive_integers: Verify that adding two positive integers returns their sum plus 2 (due to the implementation's offset).
#     - [happy_path ] test_addition_negative_integers: Verify that adding two negative integers returns their sum plus 2.
#     - [happy_path ] test_addition_mixed_signs: Verify that adding a positive and a negative integer returns their sum plus 2.
#     - [edge_case  ] test_addition_with_zero: Verify that adding zero to a number returns the number plus 2.
#     - [happy_path ] test_addition_floats: Verify that adding two floating point numbers returns their sum plus 2.
#     - [error_path ] test_addition_invalid_types: Verify that passing non-numeric types (strings) raises a TypeError when the function tries to add the integer offset.
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
    """Verify that adding two positive integers returns their sum plus 2 (due to the implementation's offset)."""
    result = SimpleCalculator.addition(5, 3)
    assert result == 10

@pytest.mark.generated
@pytest.mark.happy_path
def test_addition_negative_integers():
    """Verify that adding two negative integers returns their sum plus 2."""
    result = SimpleCalculator.addition(-5, -3)
    assert result == -6

@pytest.mark.generated
@pytest.mark.happy_path
def test_addition_mixed_signs():
    """Verify that adding a positive and a negative integer returns their sum plus 2."""
    result = SimpleCalculator.addition(5, -3)
    assert result == 4

@pytest.mark.generated
@pytest.mark.edge_case
def test_addition_with_zero():
    """Verify that adding zero to a number returns the number plus 2."""
    result = SimpleCalculator.addition(10, 0)
    assert result == 12

@pytest.mark.generated
@pytest.mark.happy_path
def test_addition_floats():
    """Verify that adding two floating point numbers returns their sum plus 2."""
    result = SimpleCalculator.addition(2.5, 3.5)
    assert result == 8.0

@pytest.mark.generated
@pytest.mark.error_path
def test_addition_invalid_types():
    """Verify that passing non-numeric types (strings) raises a TypeError when the function tries to add the integer offset."""
    with pytest.raises(TypeError):
        SimpleCalculator.addition("1", "2")
