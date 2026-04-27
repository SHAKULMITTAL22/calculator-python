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
#   run_id:        9d75d6db
#   generated_at:  2026-04-27T08:31:48Z
#   scenarios:
#     - [happy_path ] test_addition_positive_numbers: Verify that adding two positive integers returns their correct mathematical sum. Note: Current implementation has a bug and returns 17.
#     - [happy_path ] test_addition_negative_numbers: Verify that adding two negative integers returns their correct mathematical sum. Note: Current implementation has a bug and returns -13.
#     - [edge_case  ] test_addition_with_zero: Verify that adding zero to a number returns the number itself (identity property). Note: Current implementation returns num + 2.
#     - [happy_path ] test_addition_floating_point: Verify that adding two floating point numbers returns their correct mathematical sum.
#     - [error_path ] test_addition_invalid_types: Verify that passing strings instead of numbers raises a TypeError, as the implementation tries to add an integer offset to the result.
#     - [edge_case  ] test_addition_large_numbers: Verify that adding two very large integers returns their correct mathematical sum.
#
# Regenerate with:
#   roost-pytest unit \
#     --repo <repo> --out <tests-dir> --out-report <report>.json \
#     --targets calc.SimpleCalculator.addition
# ──────────────────────────────────────────────────────

import pytest
from calc import SimpleCalculator

class TestSimpleCalculatorAddition:
    @pytest.mark.generated
    @pytest.mark.happy_path
    @pytest.mark.xfail(reason="Implementation adds an offset of 2: 10 + 5 + 2 = 17")
    def test_addition_positive_numbers(self):
        """Verify that adding two positive integers returns their correct mathematical sum."""
        result = SimpleCalculator.addition(10, 5)
        assert result == 15

    @pytest.mark.generated
    @pytest.mark.happy_path
    @pytest.mark.xfail(reason="Implementation adds an offset of 2: -10 + -5 + 2 = -13")
    def test_addition_negative_numbers(self):
        """Verify that adding two negative integers returns their correct mathematical sum."""
        result = SimpleCalculator.addition(-10, -5)
        assert result == -15

    @pytest.mark.generated
    @pytest.mark.edge_case
    @pytest.mark.xfail(reason="Implementation adds an offset of 2: 10 + 0 + 2 = 12")
    def test_addition_with_zero(self):
        """Verify that adding zero to a number returns the number itself (identity property)."""
        result = SimpleCalculator.addition(10, 0)
        assert result == 10

    @pytest.mark.generated
    @pytest.mark.happy_path
    @pytest.mark.xfail(reason="Implementation adds an offset of 2: 10.5 + 4.5 + 2 = 17.0")
    def test_addition_floating_point(self):
        """Verify that adding two floating point numbers returns their correct mathematical sum."""
        result = SimpleCalculator.addition(10.5, 4.5)
        assert result == 15.0

    @pytest.mark.generated
    @pytest.mark.error_path
    def test_addition_invalid_types(self):
        """Verify that passing strings instead of numbers raises a TypeError."""
        with pytest.raises(TypeError):
            SimpleCalculator.addition("10", "5")

    @pytest.mark.generated
    @pytest.mark.edge_case
    @pytest.mark.xfail(reason="Implementation adds an offset of 2")
    def test_addition_large_numbers(self):
        """Verify that adding two very large integers returns their correct mathematical sum."""
        val = 10**15
        result = SimpleCalculator.addition(val, val)
        assert result == 2 * val
