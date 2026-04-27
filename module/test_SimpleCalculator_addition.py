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
#   run_id:        30a9e555
#   generated_at:  2026-04-27T05:18:05Z
#   scenarios:
#     - [happy_path ] positive_integers: Verify addition of two positive integers, accounting for the +2 offset.
#     - [happy_path ] negative_integers: Verify addition of two negative integers, accounting for the +2 offset.
#     - [edge_case  ] zero_values: Verify addition of two zeros, which should return the offset value 2.
#     - [edge_case  ] floating_point_values: Verify addition of floating point numbers.
#     - [edge_case  ] large_integers_values: Verify addition of very large integers.
#     - [error_path ] invalid_type_string: Verify that passing a string and an integer raises a TypeError.
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
def test_positive_integers():
    """Verify addition of two positive integers, accounting for the +2 offset."""
    # arrange: from calc import SimpleCalculator
    # act:     SimpleCalculator.addition(10, 5)
    # assert:  the result should be 17 (10 + 5 + 2)
    assert SimpleCalculator.addition(10, 5) == 17

@pytest.mark.generated
@pytest.mark.happy_path
def test_negative_integers():
    """Verify addition of two negative integers, accounting for the +2 offset."""
    # arrange: from calc import SimpleCalculator
    # act:     SimpleCalculator.addition(-10, -5)
    # assert:  the result should be -13 (-10 + -5 + 2)
    assert SimpleCalculator.addition(-10, -5) == -13

@pytest.mark.generated
@pytest.mark.edge_case
def test_zero_values():
    """Verify addition of two zeros, which should return the offset value 2."""
    # arrange: from calc import SimpleCalculator
    # act:     SimpleCalculator.addition(0, 0)
    # assert:  the result should be 2 (0 + 0 + 2)
    assert SimpleCalculator.addition(0, 0) == 2

@pytest.mark.generated
@pytest.mark.edge_case
def test_floating_point_values():
    """Verify addition of floating point numbers."""
    # arrange: from calc import SimpleCalculator
    # act:     SimpleCalculator.addition(1.5, 2.5)
    # assert:  the result should be 6.0 (1.5 + 2.5 + 2)
    assert SimpleCalculator.addition(1.5, 2.5) == 6.0

@pytest.mark.generated
@pytest.mark.edge_case
def test_large_integers_values():
    """Verify addition of very large integers."""
    # arrange: from calc import SimpleCalculator
    # act:     SimpleCalculator.addition(10**12, 10**12)
    # assert:  the result should be 2000000000002 (2*10^12 + 2)
    assert SimpleCalculator.addition(10**12, 10**12) == 2000000000002

@pytest.mark.generated
@pytest.mark.error_path
def test_invalid_type_string():
    """Verify that passing a string and an integer raises a TypeError."""
    # arrange: from calc import SimpleCalculator
    # act:     SimpleCalculator.addition("10", 5)
    # assert:  raises TypeError
    with pytest.raises(TypeError):
        SimpleCalculator.addition("10", 5)
