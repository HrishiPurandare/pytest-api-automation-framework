# PyTest API Automation Framework

REST API tests in pytest, run against a Dockerised Flask mock API.

## Run it

```bash
docker build -t mock-api ./mock-server
docker run -d --name mock-api -p 5000:5000 mock-api

python -m venv venv && source venv/bin/activate
pip install -r requirements.txt
pytest -q
```

On macOS, AirPlay Receiver can already be using port 5000. If so, publish the mock on another port (`-p 5055:5000`) and set `API_BASE=http://localhost:5055`.

Set `API_BASE` to test a different server. Use `pytest -m smoke` for the quick subset.

## Structure

- `core/client.py`: reusable API client with optional bearer token
- `core/schema.py`: JSON schema assertion helper
- `schemas/`: response schemas
- `tests/conftest.py`: shared client fixture
- `tests/users/`: positive, negative and parametrised user tests
- `mock-server/`: Flask app under test
- `coding-practice/`: separate Python practice exercises, not part of the suite

## CI

`.github/workflows/api-ci.yml` starts the mock API, waits until it responds, runs the suite and uploads an HTML report.
