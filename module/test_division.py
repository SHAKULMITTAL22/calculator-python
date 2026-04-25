ROOST_METHOD_HASH=division_641e53a5f9
ROOST_METHOD_SIG_HASH=division_641e53a5f9

"""Auto-generated unit tests for `calc.division`.

DO NOT EDIT BY HAND — re-generate via roost-pytest. The
banner directly below records when this file was produced
and what scenarios it covers; review-time grep relies on it.
"""
# ──────────────────────────────────────────────────────
# roost-pytest auto-generated
#   target:        calc.division
#   source:        calc.py:29-33
#   parser:        python_ast_parser_v2 0.1.0
#   model:         gemini/gemini-3-flash-preview
#   run_id:        a9ed4208
#   generated_at:  2026-04-25T13:30:49Z
#   scenarios:
#     - [happy_path ] zero_numerator: Verify that dividing zero by a non-zero number returns 0.0.
#     - [happy_path ] repeating_decimal: Verify that division resulting in a repeating decimal is handled correctly with standard float precision.
#     - [edge_case  ] overflow_to_infinity: Verify that division resulting in a value exceeding float capacity returns infinity.
#     - [error_path ] type_error_string: Verify that passing a string as an argument raises a TypeError.
#     - [error_path ] type_error_none: Verify that passing None as an argument raises a TypeError.
#
# Regenerate with:
#   roost-pytest unit \
#     --repo <repo> --out <tests-dir> --out-report <report>.json \
#     --targets calc.division
# ──────────────────────────────────────────────────────

import pytest
from calc import division

class TestDivision:
    @pytest.mark.generated
    @pytest.mark.happy_path
    def test_zero_numerator(self):
        """Verify that dividing zero by a non-zero number returns 0.0."""
        assert division(0, 10) == 0.0

    @pytest.mark.generated
    @pytest.mark.happy_path
    def test_repeating_decimal(self):
        """Verify that division resulting in a repeating decimal is handled correctly with standard float precision."""
        assert division(1, 3) == pytest.approx(0.3333333333333333)

    @pytest.mark.generated
    @pytest.mark.edge_case
    def test_overflow_to_infinity(self):
        """Verify that division resulting in a value exceeding float capacity returns infinity."""
        assert division(1e308, 0.01) == float('inf')

    @pytest.mark.generated
    @pytest.mark.error_path
    def test_type_error_string(self):
        """Verify that passing a string as an argument raises a TypeError."""
        with pytest.raises(TypeError):
            division("10", 2)

    @pytest.mark.generated
    @pytest.mark.error_path
    def test_type_error_none(self):
        """Verify that passing None as an argument raises a TypeError."""
        with pytest.raises(TypeError):
            division(10, None)
