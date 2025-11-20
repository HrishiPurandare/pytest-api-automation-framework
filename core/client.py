import requests
from typing import Dict

class APIClient:
    def __init__(self, base_url: str, token: str = None):
        self.base = base_url
        self.token = token

    def _headers(self):
        hdr = {"Content-Type": "application/json"}
        if self.token:
            hdr["Authorization"] = f"Bearer {self.token}"
        return hdr

    def get(self, path: str, params: Dict = None):
        return requests.get(f"{self.base}{path}", headers=self._headers(), params=params)

    def post(self, path: str, json: Dict = None):
        return requests.post(f"{self.base}{path}", headers=self._headers(), json=json)
