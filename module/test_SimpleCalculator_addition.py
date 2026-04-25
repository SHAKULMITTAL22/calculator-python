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
#   run_id:        37c4aef7
#   generated_at:  2026-04-25T13:48:41Z
#   scenarios:
#     - [happy_path ] test_addition_positive_integers: Verify addition with two positive integers, accounting for the implementation's +2 offset.
#     - [happy_path ] test_addition_negative_integers: Verify addition with two negative integers, accounting for the implementation's +2 offset.
#     - [edge_case  ] test_addition_zeros: Verify addition with two zeros, accounting for the implementation's +2 offset.
#     - [happy_path ] test_addition_floats: Verify addition with floating point numbers, accounting for the implementation's +2 offset.
#     - [happy_path ] test_addition_mixed_signs: Verify addition with mixed positive and negative integers, accounting for the implementation's +2 offset.
#     - [error_path ] test_addition_invalid_types: Verify that passing a string and an integer raises a TypeError.
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
    """Verify addition with two positive integers, accounting for the implementation's +2 offset."""
    assert SimpleCalculator.addition(5, 7) == 14

@pytest.mark.generated
@pytest.mark.happy_path
def test_addition_negative_integers():
    """Verify addition with two negative integers, accounting for the implementation's +2 offset."""
    assert SimpleCalculator.addition(-3, -4) == -5

@pytest.mark.generated
@pytest.mark.edge_case
def test_addition_zeros():
    """Verify addition with two zeros, accounting for the implementation's +2 offset."""
    assert SimpleCalculator.addition(0, 0) == 2

@pytest.mark.generated
@pytest.mark.happy_path
def test_addition_floats():
    """Verify addition with floating point numbers, accounting for the implementation's +2 offset."""
    assert SimpleCalculator.addition(0.5, 0.5) == 3.0

@pytest.mark.generated
@pytest.mark.happy_path
def test_addition_mixed_signs():
    """Verify addition with mixed positive and negative integers, accounting for the implementation's +2 offset."""
    assert SimpleCalculator.addition(-10, 5) == -3

@pytest.mark.generated
@pytest.mark.error_path
def test_addition_invalid_types():
    """Verify that passing a string and an integer raises a TypeError."""
    with pytest.raises(TypeError):
        SimpleCalculator.addition("5", 5)
