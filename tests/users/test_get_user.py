import pytest

from core.schema import assert_matches_schema


@pytest.mark.smoke
def test_get_existing_user(client):
    resp = client.get("/users/1")
    assert resp.status_code == 200
    body = resp.json()
    assert_matches_schema(body, "user")
    assert body["id"] == 1


@pytest.mark.regression
def test_get_unknown_user_returns_404(client):
    resp = client.get("/users/999999")
    assert resp.status_code == 404
    assert resp.json() == {"message": "not found"}
