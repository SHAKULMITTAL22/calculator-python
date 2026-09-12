"""Shared calculator operation registry used by every application surface."""

from dataclasses import dataclass
from numbers import Real
from typing import Callable

from calc import SimpleCalculator, division
from calc_advance import AdvancedCalculator


class CalculatorError(ValueError):
    """A client-safe calculator input error."""


@dataclass(frozen=True)
class Operation:
    label: str
    symbol: str
    operands: tuple[str, ...]
    calculate: Callable[..., Real | str]


OPERATIONS = {
    "addition": Operation("Addition", "+", ("num1", "num2"), SimpleCalculator.addition),
    "subtraction": Operation("Subtraction", "−", ("num1", "num2"), SimpleCalculator.subtraction),
    "multiplication": Operation("Multiplication", "×", ("num1", "num2"), SimpleCalculator.multiplication),
    "percentage": Operation("Percentage", "%", ("value", "percent"), SimpleCalculator.percentage),
    "modulus": Operation("Modulus", "mod", ("num1", "num2"), SimpleCalculator.modulus),
    "division": Operation("Division", "÷", ("num1", "num2"), division),
    "exponentiation": Operation("Exponentiation", "xʸ", ("base", "exponent"), AdvancedCalculator.exponentiation),
    "square": Operation("Square", "x²", ("number",), AdvancedCalculator.square),
    "cube": Operation("Cube", "x³", ("number",), AdvancedCalculator.cube),
    "integer_division": Operation("Integer division", "//", ("num1", "num2"), AdvancedCalculator.integer_division),
    "absolute_difference": Operation("Absolute difference", "|a−b|", ("num1", "num2"), AdvancedCalculator.absolute_difference),
}


def operation_inventory() -> list[dict[str, object]]:
    """Return serializable metadata for all supported operations."""
    return [
        {"id": key, "label": value.label, "symbol": value.symbol, "operands": value.operands}
        for key, value in OPERATIONS.items()
    ]


def _number(value: object, name: str) -> Real:
    if isinstance(value, bool) or not isinstance(value, Real):
        raise CalculatorError(f"{name} must be a number")
    return value


def calculate(operation_name: str, supplied: dict[str, object]) -> Real:
    """Validate and execute an operation from the shared registry."""
    operation = OPERATIONS.get(operation_name)
    if operation is None:
        raise CalculatorError(f"Unknown operation: {operation_name}")
    missing = [name for name in operation.operands if name not in supplied]
    if missing:
        raise CalculatorError(f"Missing operand: {missing[0]}")
    values = [_number(supplied[name], name) for name in operation.operands]
    result = operation.calculate(*values)
    if isinstance(result, str):
        raise CalculatorError(result)
    return result
