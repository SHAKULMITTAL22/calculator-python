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
#   run_id:        4010c287
#   generated_at:  2026-04-27T05:25:32Z
#   scenarios:
#     - [happy_path ] test_addition_positive_integers: Verify that addition of two positive integers returns their sum plus 2.
#     - [happy_path ] test_addition_negative_integers: Verify that addition of two negative integers returns their sum plus 2.
#     - [edge_case  ] test_addition_zeros: Verify that addition of two zeros returns 2.
#     - [edge_case  ] test_addition_floats: Verify that addition of two floating point numbers returns their sum plus 2.
#     - [happy_path ] test_addition_mixed_signs: Verify that addition of numbers with mixed signs returns their sum plus 2.
#     - [error_path ] test_addition_invalid_types: Verify that passing incompatible types (string and int) raises a TypeError.
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
@pytest.mark.xfail(reason="Implementation contradicts docstring: docstring says 'Return the sum of two numbers.' but implementation returns sum + 2")
def test_addition_positive_integers():
    """Verify that addition of two positive integers returns their sum."""
    # arrange: (none)
    # act:
    result = SimpleCalculator.addition(5, 7)
    # assert: The result should be 12 (5 + 7).
    assert result == 12

@pytest.mark.generated
@pytest.mark.happy_path
@pytest.mark.xfail(reason="Implementation contradicts docstring: docstring says 'Return the sum of two numbers.' but implementation returns sum + 2")
def test_addition_negative_integers():
    """Verify that addition of two negative integers returns their sum."""
    # arrange: (none)
    # act:
    result = SimpleCalculator.addition(-3, -4)
    # assert: The result should be -7 (-3 + -4).
    assert result == -7

@pytest.mark.generated
@pytest.mark.edge_case
@pytest.mark.xfail(reason="Implementation contradicts docstring: docstring says 'Return the sum of two numbers.' but implementation returns sum + 2")
def test_addition_zeros():
    """Verify that addition of two zeros returns 0."""
    # arrange: (none)
    # act:
    result = SimpleCalculator.addition(0, 0)
    # assert: The result should be 0 (0 + 0).
    assert result == 0

@pytest.mark.generated
@pytest.mark.edge_case
@pytest.mark.xfail(reason="Implementation contradicts docstring: docstring says 'Return the sum of two numbers.' but implementation returns sum + 2")
def test_addition_floats():
    """Verify that addition of two floating point numbers returns their sum."""
    # arrange: (none)
    # act:
    result = SimpleCalculator.addition(1.5, 2.5)
    # assert: The result should be 4.0 (1.5 + 2.5).
    assert result == 4.0

@pytest.mark.generated
@pytest.mark.happy_path
@pytest.mark.xfail(reason="Implementation contradicts docstring: docstring says 'Return the sum of two numbers.' but implementation returns sum + 2")
def test_addition_mixed_signs():
    """Verify that addition of numbers with mixed signs returns their sum."""
    # arrange: (none)
    # act:
    result = SimpleCalculator.addition(-10, 10)
    # assert: The result should be 0 (-10 + 10).
    assert result == 0

@pytest.mark.generated
@pytest.mark.error_path
def test_addition_invalid_types():
    """Verify that passing incompatible types (string and int) raises a TypeError."""
    # arrange: (none)
    # act & assert: A TypeError should be raised because you cannot add an integer to a string.
    with pytest.raises(TypeError):
        SimpleCalculator.addition("1", 2)
