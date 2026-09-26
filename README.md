# QuantumToken SDK

Official Python & Node.js SDK / examples for [QuantumToken (奇物匣)](https://trade.pianam.cn/) — a developer-first AI capability and open API platform.

## What is QuantumToken?

- One account, multiple apps, each app gets a long-lived `X-API-Key`.
- Unified credit wallet: **1 CNY = 100 credits**. AI chat is billed per model tier.
- Simple REST endpoints for quota query and per-call deduction.

Landing (EN): https://trade.pianam.cn/landing/en/  
Landing (ZH): https://trade.pianam.cn/landing/  
OpenAPI schema: https://trade.pianam.cn/openapi.json  
Swagger UI: https://trade.pianam.cn/docs

## Quick start

Get your `X-API-Key` from https://trade.pianam.cn → Apps → Create App.

### Python

```bash
pip install requests
python python/examples/query_balance.py
python python/examples/chat.py      # AI chat
python python/examples/extract.py   # web extraction
```

### Node.js

```bash
cd node
npm install
node examples/query_balance.js
node examples/chat.js      # AI chat
node examples/extract.js   # web extraction
```

## Core endpoints

| Endpoint | Method | Auth | Description |
|---|---|---|---|
| `/api/v1/open/quota` | GET | `X-API-Key` | Query remaining credits |
| `/api/v1/open/quota/consume` | POST | `X-API-Key` | Deduct credits once |
| `/api/v1/open/chat/completions` | POST | `X-API-Key` | **AI chat (OpenAI compatible)** |
| `/api/v1/open/extract` | POST | `X-API-Key` | **Scraper AI extraction** |

## AI chat (OpenAI compatible)

Point the official `openai` SDK at QuantumToken by changing `base_url`, or use the built-in helper:

```python
from quantoken import QuantumTokenClient

client = QuantumTokenClient(api_key="YOUR_KEY")
resp = client.chat(
    messages=[{"role": "user", "content": "Explain quantum computing in one sentence"}],
    model="qwen-flash",   # 1 credit
)
print(resp["choices"][0]["message"]["content"])
```

With the official OpenAI SDK:

```python
from openai import OpenAI
client = OpenAI(api_key="YOUR_KEY", base_url="https://trade.pianam.cn/api/v1/open")
resp = client.chat.completions.create(
    model="qwen-flash",
    messages=[{"role": "user", "content": "Hello"}],
)
```

Model tiers (credits/call): `qwen-flash` = 1, `qwen-turbo` = 2, `qwen-plus` = 5.
Credits are pre-charged and auto-refunded if the upstream call fails; `request_id` provides idempotent retries. Streaming is not supported yet.

## Scraper AI extraction

Turn a scraped page into clean structured JSON. The API strips scripts/styles/navigation, then extracts exactly the fields you ask for:

```python
from quantoken import QuantumTokenClient

client = QuantumTokenClient(api_key="YOUR_KEY")

# from raw HTML (or pass url= / text=)
resp = client.extract(
    html="<html>...scraped page...</html>",
    fields={"title": "product name", "price": "price, digits only", "sku": "item code"},
)
print(resp["data"])        # {"title": ..., "price": ..., "sku": ...}
print(resp["remaining"])   # credits left

# or ask a question about the page
resp = client.extract(url="https://example.com", question="What is this page about?")
print(resp["data"]["answer"])
```

`fields` accepts a list (`["title","price"]`), object (`{"price":"digits only"}`), or comma string; values may come back as arrays. Missing fields return `null`. Billed at the same model tiers as chat, with pre-charge and auto-refund on failure.

## Usage example

```python
from quantoken import QuantumTokenClient

client = QuantumTokenClient(api_key="YOUR_KEY", base_url="https://trade.pianam.cn")
print(client.balance())
print(client.consume(amount=1, idempotency_key="demo-001"))
```

## Business contact

- Email: biz@pianam.cn
