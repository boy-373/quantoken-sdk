"""QuantumToken Python SDK."""
import requests
from typing import Optional


class QuantumTokenClient:
    def __init__(self, api_key: str, base_url: str = "https://trade.pianam.cn"):
        if not api_key:
            raise ValueError("api_key is required")
        self.api_key = api_key
        self.base_url = base_url.rstrip("/")
        self.session = requests.Session()
        self.session.headers.update({
            "X-API-Key": api_key,
            "Content-Type": "application/json",
            "Accept": "application/json",
        })

    def _url(self, path: str) -> str:
        return f"{self.base_url}{path}"

    def balance(self) -> dict:
        """GET /api/v1/open/quota"""
        r = self.session.get(self._url("/api/v1/open/quota"))
        r.raise_for_status()
        return r.json()

    def consume(self, amount: int = 1, idempotency_key: Optional[str] = None) -> dict:
        """POST /api/v1/open/quota/consume"""
        payload = {"amount": amount}
        if idempotency_key:
            payload["idempotency_key"] = idempotency_key
        r = self.session.post(self._url("/api/v1/open/quota/consume"), json=payload)
        r.raise_for_status()
        return r.json()

    def openapi_schema(self) -> dict:
        """Fetch the OpenAPI 3.1 schema."""
        r = self.session.get(self._url("/openapi.json"))
        r.raise_for_status()
        return r.json()
