"""Dependency-free WSGI API and static frontend for the calculator service."""

from dataclasses import dataclass
from html import escape
import json
from pathlib import Path
from typing import Any
from wsgiref.simple_server import make_server

from calculator_service import CalculatorError, calculate, operation_inventory

ROOT = Path(__file__).parent


@dataclass(frozen=True)
class Response:
    data: bytes
    status_code: int = 200
    content_type: str = "application/json; charset=utf-8"

    def wsgi_status(self) -> str:
        labels = {200: "OK", 400: "Bad Request", 404: "Not Found", 405: "Method Not Allowed"}
        return f"{self.status_code} {labels[self.status_code]}"


def json_response(body: dict[str, Any], status: int = 200) -> Response:
    return Response(json.dumps(body, separators=(",", ":")).encode(), status)


def render_index() -> Response:
    buttons = []
    for index, operation in enumerate(operation_inventory()):
        selected = " selected" if index == 0 else ""
        checked = "true" if index == 0 else "false"
        metadata = escape(json.dumps(operation, separators=(",", ":")), quote=True)
        buttons.append(
            f'<button class="operation{selected}" role="radio" aria-checked="{checked}" '
            f'data-operation="{metadata}"><span aria-hidden="true">'
            f'{escape(str(operation["symbol"]))}</span>{escape(str(operation["label"]))}</button>'
        )
    template = (ROOT / "templates" / "index.html").read_text(encoding="utf-8")
    page = template.replace("<!-- OPERATIONS -->", "\n".join(buttons))
    return Response(page.encode(), content_type="text/html; charset=utf-8")


def calculate_response(payload: object) -> Response:
    if not isinstance(payload, dict):
        return json_response({"error": "Request body must be a JSON object"}, 400)
    operation = payload.get("operation")
    if not isinstance(operation, str):
        return json_response({"error": "operation must be a string"}, 400)
    try:
        result = calculate(operation, payload)
    except CalculatorError as error:
        return json_response({"error": str(error)}, 400)
    return json_response({"operation": operation, "result": result})


def static_response(path: str) -> Response:
    filename = path.removeprefix("/static/")
    if filename not in {"calculator.css", "calculator.js"}:
        return Response(b"Not found", 404, "text/plain; charset=utf-8")
    content_type = "text/css" if filename.endswith(".css") else "text/javascript"
    return Response((ROOT / "static" / filename).read_bytes(), content_type=f"{content_type}; charset=utf-8")


def dispatch(method: str, path: str, body: bytes = b"") -> Response:
    if method == "GET" and path == "/":
        return render_index()
    if method == "GET" and path == "/api/operations":
        return json_response({"operations": operation_inventory()})
    if method == "GET" and path.startswith("/static/"):
        return static_response(path)
    if path == "/api/calculate" and method != "POST":
        return Response(b"Method not allowed", 405, "text/plain; charset=utf-8")
    if method == "POST" and path == "/api/calculate":
        try:
            payload = json.loads(body)
        except (json.JSONDecodeError, UnicodeDecodeError):
            payload = None
        return calculate_response(payload)
    return Response(b"Not found", 404, "text/plain; charset=utf-8")


class TestClient:
    def get(self, path: str) -> Response:
        return dispatch("GET", path)

    def post(self, path: str, json: object = None, data: str | bytes = b"", **_: object) -> Response:
        if json is not None:
            body = globals()["json"].dumps(json).encode()
        else:
            body = data.encode() if isinstance(data, str) else data
        return dispatch("POST", path, body)


class CalculatorApplication:
    def __init__(self) -> None:
        self.config: dict[str, object] = {}

    def test_client(self) -> TestClient:
        return TestClient()

    def __call__(self, environ: dict[str, Any], start_response: Any) -> list[bytes]:
        length = int(environ.get("CONTENT_LENGTH") or 0)
        body = environ["wsgi.input"].read(length)
        response = dispatch(environ["REQUEST_METHOD"], environ.get("PATH_INFO", "/"), body)
        headers = [("Content-Type", response.content_type), ("Content-Length", str(len(response.data)))]
        start_response(response.wsgi_status(), headers)
        return [response.data]

    def run(self, host: str = "127.0.0.1", port: int = 5000) -> None:
        print(f"Calculator running on http://{host}:{port}", flush=True)
        with make_server(host, port, self) as server:
            server.serve_forever()


app = CalculatorApplication()


if __name__ == "__main__":  # pragma: no cover - exercised by startup validation
    app.run()
