# ROOST_METHOD_HASH=division_641e53a5f9
# ROOST_METHOD_SIG_HASH=division_641e53a5f9

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
#   run_id:        cf16e38c
#   generated_at:  2026-04-25T14:38:59Z
#   scenarios:
#     - [happy_path ] zero_dividend: Verify that dividing zero by a non-zero number returns 0.0.
#     - [happy_path ] repeating_decimal: Verify that division resulting in a repeating decimal is handled with standard float precision.
#     - [edge_case  ] infinity_dividend: Verify that dividing infinity by a finite number returns infinity.
#     - [edge_case  ] infinity_divisor: Verify that dividing a finite number by infinity returns 0.0.
#     - [edge_case  ] inf_divided_by_inf: Verify that dividing infinity by infinity returns NaN.
#     - [edge_case  ] nan_input: Verify that division involving NaN as an input returns NaN.
#
# Regenerate with:
#   roost-pytest unit \
#     --repo <repo> --out <tests-dir> --out-report <report>.json \
#     --targets calc.division
# ──────────────────────────────────────────────────────

import pytest
import math
from calc import division

@pytest.mark.generated
@pytest.mark.happy_path
def test_zero_dividend():
    """Verify that dividing zero by a non-zero number returns 0.0."""
    result = division(0, 5)
    assert result == 0.0

@pytest.mark.generated
@pytest.mark.happy_path
def test_repeating_decimal():
    """Verify that division resulting in a repeating decimal is handled with standard float precision."""
    result = division(1, 3)
    assert result == pytest.approx(0.3333333333333333)

@pytest.mark.generated
@pytest.mark.edge_case
def test_infinity_dividend():
    """Verify that dividing infinity by a finite number returns infinity."""
    result = division(float('inf'), 2)
    assert result == float('inf')

@pytest.mark.generated
@pytest.mark.edge_case
def test_infinity_divisor():
    """Verify that dividing a finite number by infinity returns 0.0."""
    result = division(10, float('inf'))
    assert result == 0.0

@pytest.mark.generated
@pytest.mark.edge_case
def test_inf_divided_by_inf():
    """Verify that dividing infinity by infinity returns NaN."""
    result = division(float('inf'), float('inf'))
    assert math.isnan(result)

@pytest.mark.generated
@pytest.mark.edge_case
def test_nan_input():
    """Verify that division involving NaN as an input returns NaN."""
    result = division(float('nan'), 5)
    assert math.isnan(result)
