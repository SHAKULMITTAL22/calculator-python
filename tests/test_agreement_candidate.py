"""Agreement v1 coverage for every operation and application boundary."""

from io import BytesIO
from unittest.mock import patch

import pytest

from app import app
from calculator_service import CalculatorError, calculate


VALID_CASES = {
    "addition": [({"num1": 2, "num2": 3}, 5), ({"num1": -2, "num2": 3}, 1), ({"num1": 0, "num2": 0}, 0), ({"num1": 1.5, "num2": 2.25}, 3.75)],
    "subtraction": [({"num1": 8, "num2": 3}, 5), ({"num1": 3, "num2": 8}, -5), ({"num1": 7, "num2": 7}, 0), ({"num1": 1.5, "num2": .25}, 1.25), ({"num1": 0, "num2": -4}, 4)],
    "multiplication": [({"num1": 4, "num2": 3}, 12), ({"num1": -4, "num2": 3}, -12), ({"num1": 0, "num2": 99}, 0), ({"num1": 1.5, "num2": 2}, 3)],
    "percentage": [({"value": 200, "percent": 15}, 30), ({"value": 50, "percent": 0}, 0), ({"value": 50, "percent": 100}, 50), ({"value": -80, "percent": 25}, -20), ({"value": 10, "percent": 12.5}, 1.25)],
    "modulus": [({"num1": 10, "num2": 3}, 1), ({"num1": -10, "num2": 3}, 2), ({"num1": 10, "num2": -3}, -2), ({"num1": 3.5, "num2": 2}, 1.5)],
    "division": [({"num1": 10, "num2": 2}, 5), ({"num1": -10, "num2": 2}, -5), ({"num1": 0, "num2": 2}, 0), ({"num1": 1, "num2": 4}, .25)],
    "exponentiation": [({"base": 2, "exponent": 3}, 8), ({"base": 9, "exponent": 0}, 1), ({"base": -2, "exponent": 3}, -8), ({"base": 4, "exponent": .5}, 2)],
    "square": [({"number": 4}, 16), ({"number": -4}, 16), ({"number": 0}, 0), ({"number": 1.5}, 2.25)],
    "cube": [({"number": 3}, 27), ({"number": -3}, -27), ({"number": 0}, 0), ({"number": 1.5}, 3.375)],
    "integer_division": [({"num1": 9, "num2": 2}, 4), ({"num1": -9, "num2": 2}, -5), ({"num1": 0, "num2": 2}, 0), ({"num1": 9.5, "num2": 2}, 4)],
    "absolute_difference": [({"num1": 8, "num2": 3}, 5), ({"num1": 3, "num2": 8}, 5), ({"num1": -3, "num2": -8}, 5), ({"num1": 2.5, "num2": 1}, 1.5)],
}


@pytest.mark.parametrize(
    ("operation", "operands", "expected"),
    [(operation, operands, expected) for operation, cases in VALID_CASES.items() for operands, expected in cases],
)
def test_all_operations_valid_and_boundary_values(operation, operands, expected):
    assert calculate(operation, operands) == pytest.approx(expected)


@pytest.mark.parametrize(
    ("operation", "operands", "message"),
    [
        ("division", {"num1": 1, "num2": 0}, "Cannot divide by zero"),
        ("modulus", {"num1": 1, "num2": 0}, "Cannot perform modulus by zero"),
        ("integer_division", {"num1": 1, "num2": 0}, "Cannot perform integer division by zero"),
    ],
)
def test_zero_divisors(operation, operands, message):
    with pytest.raises(CalculatorError, match=message):
        calculate(operation, operands)


@pytest.mark.parametrize(
    ("operation", "operands", "message"),
    [
        ("missing", {}, "Unknown operation"),
        ("addition", {"num1": 1}, "Missing operand: num2"),
        ("square", {"number": "4"}, "number must be a number"),
        ("square", {"number": True}, "number must be a number"),
        ("addition", {"num1": None, "num2": 2}, "num1 must be a number"),
        ("percentage", {"value": 10, "percent": []}, "percent must be a number"),
    ],
)
def test_service_rejects_malformed_input(operation, operands, message):
    with pytest.raises(CalculatorError, match=message):
        calculate(operation, operands)


@pytest.mark.parametrize(
    ("method", "path", "payload", "status", "fragment"),
    [
        ("get", "/", None, 200, b"Blue Motion"),
        ("get", "/api/operations", None, 200, b"percentage"),
        ("post", "/api/calculate", {"operation": "percentage", "value": 200, "percent": 15}, 200, b'"result":30'),
        ("post", "/api/calculate", None, 400, b"JSON object"),
        ("post", "/api/calculate", [], 400, b"JSON object"),
        ("post", "/api/calculate", {}, 400, b"operation must be a string"),
        ("post", "/api/calculate", {"operation": 1}, 400, b"operation must be a string"),
        ("post", "/api/calculate", {"operation": "unknown"}, 400, b"Unknown operation"),
        ("post", "/api/calculate", {"operation": "addition", "num1": 1}, 400, b"Missing operand"),
        ("post", "/api/calculate", {"operation": "division", "num1": 1, "num2": 0}, 400, b"Cannot divide by zero"),
        ("post", "/api/calculate", {"operation": "addition", "num1": "1", "num2": 2}, 400, b"must be a number"),
    ],
)
def test_http_surfaces(method, path, payload, status, fragment):
    app.config.update(TESTING=True)
    client = app.test_client()
    if method == "get":
        response = client.get(path)
    elif payload is None:
        response = client.post(path, data="not json", content_type="text/plain")
    else:
        response = client.post(path, json=payload)
    assert response.status_code == status
    assert fragment in response.data
    if path == "/":
        assert client.get("/static/calculator.css").content_type.startswith("text/css")
        assert client.get("/static/calculator.js").content_type.startswith("text/javascript")
        assert client.get("/static/missing.txt").status_code == 404
        assert client.get("/api/calculate").status_code == 405
        assert client.get("/missing").status_code == 404

        statuses = []
        environ = {
            "REQUEST_METHOD": "GET",
            "PATH_INFO": "/api/operations",
            "CONTENT_LENGTH": "0",
            "wsgi.input": BytesIO(),
        }
        body = app(environ, lambda value, headers: statuses.append((value, headers)))
        assert statuses[0][0] == "200 OK"
        assert b"absolute_difference" in body[0]

        class Server:
            def __enter__(self):
                return self

            def __exit__(self, *args):
                return None

            def serve_forever(self):
                self.started = True

        server = Server()
        with patch("app.make_server", return_value=server):
            app.run(port=0)
        assert server.started
