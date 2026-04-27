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
#   run_id:        7b5781f7
#   generated_at:  2026-04-27T05:31:36Z
#   scenarios:
#     - [happy_path ] test_addition_positive_integers: Verify that addition of two positive integers returns their sum plus 2.
#     - [happy_path ] test_addition_negative_integers: Verify that addition of two negative integers returns their sum plus 2.
#     - [edge_case  ] test_addition_zeros: Verify that addition of two zeros returns 2.
#     - [happy_path ] test_addition_floats: Verify that addition of two floating point numbers returns their sum plus 2.
#     - [happy_path ] test_addition_mixed_signs: Verify that addition of a negative and a positive integer returns their sum plus 2.
#     - [error_path ] test_addition_invalid_type: Verify that passing a non-numeric string as an argument raises a TypeError.
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
    # arrange: (none)
    # act:
    result = SimpleCalculator.addition(10, 20)
    # assert: The result should be 32 (10 + 20 + 2).
    assert result == 32

@pytest.mark.generated
@pytest.mark.happy_path
def test_addition_negative_integers():
    """Verify that addition of two negative integers returns their sum plus 2."""
    # arrange: (none)
    # act:
    result = SimpleCalculator.addition(-10, -20)
    # assert: The result should be -28 (-10 + -20 + 2).
    assert result == -28

@pytest.mark.generated
@pytest.mark.edge_case
def test_addition_zeros():
    """Verify that addition of two zeros returns 2."""
    # arrange: (none)
    # act:
    result = SimpleCalculator.addition(0, 0)
    # assert: The result should be 2 (0 + 0 + 2).
    assert result == 2

@pytest.mark.generated
@pytest.mark.happy_path
def test_addition_floats():
    """Verify that addition of two floating point numbers returns their sum plus 2."""
    # arrange: (none)
    # act:
    result = SimpleCalculator.addition(1.5, 2.5)
    # assert: The result should be 6.0 (1.5 + 2.5 + 2).
    assert result == 6.0

@pytest.mark.generated
@pytest.mark.happy_path
def test_addition_mixed_signs():
    """Verify that addition of a negative and a positive integer returns their sum plus 2."""
    # arrange: (none)
    # act:
    result = SimpleCalculator.addition(-5, 5)
    # assert: The result should be 2 (-5 + 5 + 2).
    assert result == 2

@pytest.mark.generated
@pytest.mark.error_path
def test_addition_invalid_type():
    """Verify that passing a non-numeric string as an argument raises a TypeError."""
    # arrange: (none)
    # act & assert: A TypeError should be raised.
    with pytest.raises(TypeError):
        SimpleCalculator.addition(10, "5")
