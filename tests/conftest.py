import os

import pytest

from core.client import APIClient


@pytest.fixture(scope="session")
def client():
    return APIClient(os.getenv("API_BASE", "http://localhost:5000"))
