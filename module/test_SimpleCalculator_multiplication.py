# ROOST_METHOD_HASH=SimpleCalculator.multiplication_b85031f6ad
# ROOST_METHOD_SIG_HASH=SimpleCalculator.multiplication_b85031f6ad

"""Auto-generated unit tests for `calc.SimpleCalculator.multiplication`.

DO NOT EDIT BY HAND — re-generate via roost-pytest. The
banner directly below records when this file was produced
and what scenarios it covers; review-time grep relies on it.
"""
# ──────────────────────────────────────────────────────
# roost-pytest auto-generated
#   target:        calc.SimpleCalculator.multiplication
#   source:        calc.py:18-20
#   parser:        python_ast_parser_v2 0.1.0
#   model:         gemini/gemini-3-flash-preview
#   run_id:        65c7fe6f
#   generated_at:  2026-04-27T08:58:31Z
#   scenarios:
#     - [happy_path ] test_multiplication_positive_integers: Verify that multiplying two positive integers returns the correct product.
#     - [happy_path ] test_multiplication_negative_integers: Verify that multiplying two negative integers returns a positive product.
#     - [happy_path ] test_multiplication_mixed_signs: Verify that multiplying a positive and a negative integer returns a negative product.
#     - [edge_case  ] test_multiplication_by_zero: Verify that multiplying any number by zero returns zero.
#     - [edge_case  ] test_multiplication_by_one: Verify that multiplying any number by one returns the number itself.
#     - [happy_path ] test_multiplication_floats: Verify that multiplying floating point numbers returns the correct product.
#
# Regenerate with:
#   roost-pytest unit \
#     --repo <repo> --out <tests-dir> --out-report <report>.json \
#     --targets calc.SimpleCalculator.multiplication
# ──────────────────────────────────────────────────────

import pytest
from calc import SimpleCalculator

class Test_SimpleCalculatorMultiplication:
    @pytest.mark.generated
    @pytest.mark.happy_path
    def test_multiplication_positive_integers(self):
        """Verify that multiplying two positive integers returns the correct product."""
        assert SimpleCalculator.multiplication(10, 5) == 50

    @pytest.mark.generated
    @pytest.mark.happy_path
    def test_multiplication_negative_integers(self):
        """Verify that multiplying two negative integers returns a positive product."""
        assert SimpleCalculator.multiplication(-4, -3) == 12

    @pytest.mark.generated
    @pytest.mark.happy_path
    def test_multiplication_mixed_signs(self):
        """Verify that multiplying a positive and a negative integer returns a negative product."""
        assert SimpleCalculator.multiplication(6, -7) == -42

    @pytest.mark.generated
    @pytest.mark.edge_case
    def test_multiplication_by_zero(self):
        """Verify that multiplying any number by zero returns zero."""
        assert SimpleCalculator.multiplication(100, 0) == 0

    @pytest.mark.generated
    @pytest.mark.edge_case
    def test_multiplication_by_one(self):
        """Verify that multiplying any number by one returns the number itself."""
        assert SimpleCalculator.multiplication(123, 1) == 123

    @pytest.mark.generated
    @pytest.mark.happy_path
    def test_multiplication_floats(self):
        """Verify that multiplying floating point numbers returns the correct product."""
        assert SimpleCalculator.multiplication(0.5, 2.0) == 1.0
