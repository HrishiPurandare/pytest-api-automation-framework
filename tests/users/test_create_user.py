import pytest

from core.schema import assert_matches_schema


@pytest.mark.smoke
def test_create_user_returns_201_and_valid_body(client):
    payload = {"name": "Auto Created", "email": "auto.created@example.com"}
    resp = client.post("/users", json=payload)
    assert resp.status_code == 201
    body = resp.json()
    assert_matches_schema(body, "user")
    assert body["name"] == payload["name"]
    assert body["email"] == payload["email"]


@pytest.mark.regression
@pytest.mark.parametrize(
    "name, email",
    [
        ("Second User", "second@example.com"),
        ("Name With Spaces", "spaces@example.com"),
        ("Ünïcode Üser", "unicode@example.com"),
    ],
)
def test_created_user_can_be_fetched(client, name, email):
    created = client.post("/users", json={"name": name, "email": email}).json()
    fetched = client.get(f"/users/{created['id']}")
    assert fetched.status_code == 200
    assert fetched.json() == {"id": created["id"], "name": name, "email": email}
