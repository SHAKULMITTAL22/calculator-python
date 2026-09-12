# Calculator Python

A dependency-free Python calculator service with a responsive, keyboard-accessible web UI and JSON API. All 11 operations use the shared registry in `calculator_service.py`, including the percentage behavior introduced by PR #277.

## Run

```sh
python3 -m venv .venv
. .venv/bin/activate
python3 -m pip install -r requirements.txt
python3 app.py
```

Open <http://127.0.0.1:5000>.

## Test and coverage

```sh
python3 -m pytest -q
python3 -m pytest --cov=calc --cov=calc_advance --cov=calculator_service --cov=app --cov-report=term-missing
```

## API

```sh
curl http://127.0.0.1:5000/api/operations
curl -X POST http://127.0.0.1:5000/api/calculate \
  -H 'Content-Type: application/json' \
  -d '{"operation":"percentage","value":200,"percent":15}'
```
