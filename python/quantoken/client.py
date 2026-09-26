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


    def chat(
        self,
        messages: list,
        model: str = "qwen-flash",
        max_tokens: int = 512,
        temperature: Optional[float] = None,
        top_p: Optional[float] = None,
        stop=None,
        request_id: Optional[str] = None,
    ) -> dict:
        """POST /api/v1/open/chat/completions (OpenAI compatible).

        Returns a standard OpenAI Chat Completion dict.
        Tiers (credits/call): qwen-flash=1, qwen-turbo=2, qwen-plus=5.
        """
        payload: dict = {"model": model, "messages": messages, "max_tokens": max_tokens}
        if temperature is not None:
            payload["temperature"] = temperature
        if top_p is not None:
            payload["top_p"] = top_p
        if stop is not None:
            payload["stop"] = stop
        if request_id is not None:
            payload["request_id"] = request_id
        r = self.session.post(self._url("/api/v1/open/chat/completions"), json=payload)
        r.raise_for_status()
        return r.json()

    def extract(
        self,
        html: Optional[str] = None,
        text: Optional[str] = None,
        url: Optional[str] = None,
        fields=None,
        question: Optional[str] = None,
        model: str = "qwen-flash",
        max_tokens: int = 1024,
        request_id: Optional[str] = None,
    ) -> dict:
        """POST /api/v1/open/extract - scraper AI extraction.

        Provide one of html/text/url and one of fields/question.
        fields may be a list ["title","price"], dict {"price":"digits only"},
        or comma string. Returns {"code":0,"data":{...},"remaining":...}.
        """
        payload: dict = {"model": model, "max_tokens": max_tokens}
        if html is not None:
            payload["html"] = html
        if text is not None:
            payload["text"] = text
        if url is not None:
            payload["url"] = url
        if fields is not None:
            payload["fields"] = fields
        if question is not None:
            payload["question"] = question
        if request_id is not None:
            payload["request_id"] = request_id
        r = self.session.post(self._url("/api/v1/open/extract"), json=payload)
        r.raise_for_status()
        return r.json()

    def openapi_schema(self) -> dict:
        """Fetch the OpenAPI 3.1 schema."""
        r = self.session.get(self._url("/openapi.json"))
        r.raise_for_status()
        return r.json()
