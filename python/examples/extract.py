# -*- coding: utf-8 -*-
"""Web extraction example. Docs: https://trade.pianam.cn/docs"""
from quantoken import QuantumTokenClient

client = QuantumTokenClient(api_key="YOUR_API_KEY")

# 1) Extract structured fields from a URL
resp = client.extract(
    url="https://example.com",
    fields={"title": "page title", "desc": "one-sentence summary"},
    request_id="demo-extract-001",
)
print(resp["data"])

# 2) Extract from raw HTML / text
resp = client.extract(
    html="<html><body><h1>iPhone 16</h1><p>价格 5999 元</p></body></html>",
    fields={"product": "product name", "price": "price, digits only"},
)
print(resp["data"])

# 3) Ask a question about a page
resp = client.extract(url="https://example.com", question="这个页面主要讲什么？")
print(resp["data"]["answer"])
print("remaining credits:", resp.get("remaining"))
