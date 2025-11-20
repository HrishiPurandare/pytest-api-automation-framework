# PyTest API Automation Framework

Purpose:
- Demonstrates professional API testing: JWT, schema validation, markers, CI, and reporting.

Quickstart:
1. Create virtualenv: `python -m venv venv && source venv/bin/activate`
2. Install: `pip install -r requirements.txt`
3. Run: `pytest -q --maxfail=1`

Structure:
- core: client, auth, schema validator
- tests: grouped by domain (users, payments)
- schemas: JSON schemas for responses
- .github/workflows/api-ci.yml for CI
