ROOST_METHOD_HASH=AdvancedCalculator.exponentiation_e4ad67523b
ROOST_METHOD_SIG_HASH=AdvancedCalculator.exponentiation_e4ad67523b

"""Auto-generated unit tests for `calc_advance.AdvancedCalculator.exponentiation`.

DO NOT EDIT BY HAND — re-generate via roost-pytest. The
banner directly below records when this file was produced
and what scenarios it covers; review-time grep relies on it.
"""
# ──────────────────────────────────────────────────────
# roost-pytest auto-generated
#   target:        calc_advance.AdvancedCalculator.exponentiation
#   source:        calc_advance.py:10-12
#   parser:        python_ast_parser_v2 0.1.0
#   model:         gemini/gemini-3-flash-preview
#   run_id:        a9ed4208
#   generated_at:  2026-04-25T13:31:46Z
#   scenarios:
#     - [happy_path ] positive_integers: Test exponentiation with positive integers.
#     - [edge_case  ] negative_exponent: Test exponentiation with a negative exponent.
#     - [edge_case  ] zero_base_zero_exponent: Test exponentiation with zero base and zero exponent.
#     - [error_path ] zero_base_negative_exponent: Test exponentiation with zero base and negative exponent.
#     - [edge_case  ] fractional_exponent: Test exponentiation with a fractional exponent (root).
#     - [edge_case  ] negative_base_complex_result: Test exponentiation with a negative base and fractional exponent resulting in a complex number.
#
# Regenerate with:
#   roost-pytest unit \
#     --repo <repo> --out <tests-dir> --out-report <report>.json \
#     --targets calc_advance.AdvancedCalculator.exponentiation
# ──────────────────────────────────────────────────────

import pytest
import cmath
from calc_advance import AdvancedCalculator

@pytest.mark.generated
@pytest.mark.happy_path
def test_positive_integers():
    """Test exponentiation with positive integers."""
    assert AdvancedCalculator.exponentiation(2, 3) == 8

@pytest.mark.generated
@pytest.mark.edge_case
def test_negative_exponent():
    """Test exponentiation with a negative exponent."""
    assert AdvancedCalculator.exponentiation(5, -1) == 0.2

@pytest.mark.generated
@pytest.mark.edge_case
def test_zero_base_zero_exponent():
    """Test exponentiation with zero base and zero exponent."""
    assert AdvancedCalculator.exponentiation(0, 0) == 1

@pytest.mark.generated
@pytest.mark.error_path
def test_zero_base_negative_exponent():
    """Test exponentiation with zero base and negative exponent."""
    with pytest.raises(ZeroDivisionError):
        AdvancedCalculator.exponentiation(0, -2)

@pytest.mark.generated
@pytest.mark.edge_case
def test_fractional_exponent():
    """Test exponentiation with a fractional exponent (root)."""
    assert AdvancedCalculator.exponentiation(16, 0.25) == 2.0

@pytest.mark.generated
@pytest.mark.edge_case
def test_negative_base_complex_result():
    """Test exponentiation with a negative base and fractional exponent resulting in a complex number."""
    result = AdvancedCalculator.exponentiation(-9, 0.5)
    assert isinstance(result, complex)
    # (-9)**0.5 is (1.8369701987210297e-16+3j)
    assert cmath.isclose(result, 3j, abs_tol=1e-9)
