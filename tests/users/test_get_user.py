# tests/users/test_get_user.py
import os
import pytest
from core.client import APIClient

BASE = os.getenv("API_BASE", "http://localhost:5000")

@pytest.fixture(scope="module")
def client():
    return APIClient(BASE)

def test_get_user_200(client):
    resp = client.get("/users/1")
    assert resp.status_code == 200
    data = resp.json()
    assert "id" in data and data["id"] == 1
    assert "name" in data
