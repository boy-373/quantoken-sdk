# QuantumToken SDK

Official Python & Node.js SDK / examples for [QuantumToken (奇物匣)](https://trade.pianam.cn/landing/) — a developer-first AI capability and open API platform.

## What is QuantumToken?

- One account, multiple apps, each app gets a long-lived `X-API-Key`.
- Unified credit wallet: **1 CNY = 100 credits = 100 API calls** (default tier).
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
```

### Node.js

```bash
cd node
npm install
node examples/query_balance.js
```

## Core endpoints

| Endpoint | Method | Auth | Description |
|---|---|---|---|
| `/api/v1/open/quota` | GET | `X-API-Key` | Query remaining credits |
| `/api/v1/open/quota/consume` | POST | `X-API-Key` | Deduct credits once |

## Usage example

```python
from quantoken import QuantumTokenClient

client = QuantumTokenClient(api_key="YOUR_KEY", base_url="https://trade.pianam.cn")
print(client.balance())
print(client.consume(amount=1, idempotency_key="demo-001"))
```

## Business contact

- Email: biz@pianam.cn
