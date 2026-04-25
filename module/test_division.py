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
#   run_id:        6ffe75a1
#   generated_at:  2026-04-25T12:12:12Z
#   scenarios:
#     - [happy_path ] zero_numerator: Verify that dividing zero by a non-zero number returns 0.0.
#     - [happy_path ] repeating_decimal: Verify that division resulting in a repeating decimal is handled correctly.
#     - [error_path ] type_error_string_input: Verify that passing a string as the first argument raises a TypeError.
#     - [edge_case  ] infinity_result: Verify that division resulting in a value exceeding float capacity returns infinity.
#     - [edge_case  ] nan_input: Verify that passing NaN as an input returns NaN.
#     - [edge_case  ] float_zero_denominator: Verify that division by float zero (0.0) is handled the same as integer zero.
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
def test_zero_numerator():
    """Verify that dividing zero by a non-zero number returns 0.0."""
    result = division(0, 5)
    assert result == 0.0

@pytest.mark.generated
@pytest.mark.happy_path
def test_repeating_decimal():
    """Verify that division resulting in a repeating decimal is handled correctly."""
    result = division(1, 3)
    assert result == pytest.approx(0.3333333333333333)

@pytest.mark.generated
@pytest.mark.error_path
def test_type_error_string_input():
    """Verify that passing a string as the first argument raises a TypeError."""
    with pytest.raises(TypeError):
        division("10", 2)

@pytest.mark.generated
@pytest.mark.edge_case
def test_infinity_result():
    """Verify that division resulting in a value exceeding float capacity returns infinity."""
    result = division(1e308, 0.01)
    assert result == float('inf')

@pytest.mark.generated
@pytest.mark.edge_case
def test_nan_input():
    """Verify that passing NaN as an input returns NaN."""
    result = division(float('nan'), 1)
    assert math.isnan(result)

@pytest.mark.generated
@pytest.mark.edge_case
def test_float_zero_denominator():
    """Verify that division by float zero (0.0) is handled the same as integer zero."""
    result = division(10, 0.0)
    assert result == "Cannot divide by zero"
