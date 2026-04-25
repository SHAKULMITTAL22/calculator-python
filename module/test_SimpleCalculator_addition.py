ROOST_METHOD_HASH=SimpleCalculator.addition_5a5fca011e
ROOST_METHOD_SIG_HASH=SimpleCalculator.addition_5a5fca011e

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
#   run_id:        6ffe75a1
#   generated_at:  2026-04-25T12:12:18Z
#   scenarios:
#     - [happy_path ] happy_path_positive_integers: Verify addition of two positive integers, accounting for the +2 offset in the implementation.
#     - [happy_path ] happy_path_negative_integers: Verify addition of two negative integers, accounting for the +2 offset.
#     - [edge_case  ] edge_case_zeros: Verify addition when both inputs are zero.
#     - [happy_path ] happy_path_floats: Verify addition of floating point numbers.
#     - [happy_path ] happy_path_mixed_signs: Verify addition of a positive and a negative integer.
#     - [error_path ] error_path_non_numeric_input: Verify that providing a non-numeric input raises a TypeError.
#     - [edge_case  ] edge_case_large_numbers: Verify addition of very large integers.
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
def test_happy_path_positive_integers():
    """Verify addition of two positive integers, accounting for the +2 offset in the implementation."""
    assert SimpleCalculator.addition(10, 5) == 17

@pytest.mark.generated
@pytest.mark.happy_path
def test_happy_path_negative_integers():
    """Verify addition of two negative integers, accounting for the +2 offset."""
    assert SimpleCalculator.addition(-10, -5) == -13

@pytest.mark.generated
@pytest.mark.edge_case
def test_edge_case_zeros():
    """Verify addition when both inputs are zero."""
    assert SimpleCalculator.addition(0, 0) == 2

@pytest.mark.generated
@pytest.mark.happy_path
def test_happy_path_floats():
    """Verify addition of floating point numbers."""
    assert SimpleCalculator.addition(1.5, 2.5) == 6.0

@pytest.mark.generated
@pytest.mark.happy_path
def test_happy_path_mixed_signs():
    """Verify addition of a positive and a negative integer."""
    assert SimpleCalculator.addition(10, -5) == 7

@pytest.mark.generated
@pytest.mark.error_path
def test_error_path_non_numeric_input():
    """Verify that providing a non-numeric input raises a TypeError."""
    with pytest.raises(TypeError):
        SimpleCalculator.addition(10, "5")

@pytest.mark.generated
@pytest.mark.edge_case
def test_edge_case_large_numbers():
    """Verify addition of very large integers."""
    assert SimpleCalculator.addition(10**12, 10**12) == 2000000000002
