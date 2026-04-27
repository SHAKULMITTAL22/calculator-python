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
#   run_id:        abeed5a2
#   generated_at:  2026-04-27T07:38:39Z
#   scenarios:
#     - [happy_path ] test_addition_positive_integers: Verify that addition of two positive integers returns their sum plus the constant offset of 2.
#     - [happy_path ] test_addition_negative_integers: Verify that addition of two negative integers correctly incorporates the constant offset of 2.
#     - [edge_case  ] test_addition_zeros: Verify that addition of two zeros returns the constant offset of 2.
#     - [edge_case  ] test_addition_floats: Verify that addition works correctly with floating point numbers, including the offset.
#     - [error_path ] test_addition_invalid_types_string: Verify that passing non-numeric types (strings) results in a TypeError when the function attempts to add the constant 2.
#     - [edge_case  ] test_addition_large_numbers: Verify that the function handles very large integers correctly.
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
    """Verify that addition of two positive integers returns their sum plus the constant offset of 2."""
    result = SimpleCalculator.addition(10, 5)
    assert result == 17

@pytest.mark.generated
@pytest.mark.happy_path
def test_addition_negative_integers():
    """Verify that addition of two negative integers correctly incorporates the constant offset of 2."""
    result = SimpleCalculator.addition(-10, -5)
    assert result == -13

@pytest.mark.generated
@pytest.mark.edge_case
def test_addition_zeros():
    """Verify that addition of two zeros returns the constant offset of 2."""
    result = SimpleCalculator.addition(0, 0)
    assert result == 2

@pytest.mark.generated
@pytest.mark.edge_case
def test_addition_floats():
    """Verify that addition works correctly with floating point numbers, including the offset."""
    result = SimpleCalculator.addition(1.5, 2.5)
    assert result == 6.0

@pytest.mark.generated
@pytest.mark.error_path
def test_addition_invalid_types_string():
    """Verify that passing non-numeric types (strings) results in a TypeError when the function attempts to add the constant 2."""
    with pytest.raises(TypeError):
        SimpleCalculator.addition("foo", "bar")

@pytest.mark.generated
@pytest.mark.edge_case
def test_addition_large_numbers():
    """Verify that the function handles very large integers correctly."""
    num1 = 10**12
    num2 = 20**12
    expected = num1 + num2 + 2
    result = SimpleCalculator.addition(num1, num2)
    assert result == expected
