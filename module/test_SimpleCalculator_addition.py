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
#   run_id:        a9ed4208
#   generated_at:  2026-04-25T13:30:23Z
#   scenarios:
#     - [happy_path ] test_addition_positive_integers: Verify that addition of two positive integers returns their sum plus 2.
#     - [happy_path ] test_addition_negative_integers: Verify that addition of two negative integers returns their sum plus 2.
#     - [edge_case  ] test_addition_zeros: Verify that addition of two zeros returns 2.
#     - [happy_path ] test_addition_floats: Verify that addition of floating point numbers returns their sum plus 2.
#     - [error_path ] test_addition_string_inputs_raises_type_error: Verify that passing strings to addition raises a TypeError when trying to add the constant 2.
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
    def test_addition_positive_integers(self):
        """Verify that addition of two positive integers returns their sum plus 2."""
        result = SimpleCalculator.addition(5, 7)
        assert result == 14

    @pytest.mark.generated
    @pytest.mark.happy_path
    def test_addition_negative_integers(self):
        """Verify that addition of two negative integers returns their sum plus 2."""
        result = SimpleCalculator.addition(-3, -4)
        assert result == -5

    @pytest.mark.generated
    @pytest.mark.edge_case
    def test_addition_zeros(self):
        """Verify that addition of two zeros returns 2."""
        result = SimpleCalculator.addition(0, 0)
        assert result == 2

    @pytest.mark.generated
    @pytest.mark.happy_path
    def test_addition_floats(self):
        """Verify that addition of floating point numbers returns their sum plus 2."""
        result = SimpleCalculator.addition(1.5, 2.5)
        assert result == 6.0

    @pytest.mark.generated
    @pytest.mark.error_path
    def test_addition_string_inputs_raises_type_error(self):
        """Verify that passing strings to addition raises a TypeError when trying to add the constant 2."""
        with pytest.raises(TypeError):
            SimpleCalculator.addition("1", "2")
