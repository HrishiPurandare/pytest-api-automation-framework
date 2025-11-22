# tests/users/test_create_user.py
import os
import pytest
from core.client import APIClient

BASE = os.getenv("API_BASE", "http://localhost:5000")

@pytest.fixture(scope="module")
def client():
    return APIClient(BASE)

def test_create_user_201(client):
    payload = {"name": "Auto Created", "email": "auto.created@example.com"}
    resp = client.post("/users", json=payload)
    assert resp.status_code == 201
    data = resp.json()
    assert data["name"] == payload["name"]
    assert "id" in data

def test_get_new_user(client):
    # create then fetch
    payload = {"name": "Second User", "email": "second@example.com"}
    create = client.post("/users", json=payload)
    data = create.json()
    uid = data["id"]
    get_resp = client.get(f"/users/{uid}")
    assert get_resp.status_code == 200
    assert get_resp.json()["email"] == payload["email"]
