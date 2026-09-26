# -*- coding: utf-8 -*-
"""AI chat example (OpenAI compatible). Docs: https://trade.pianam.cn/docs"""
from quantoken import QuantumTokenClient

client = QuantumTokenClient(api_key="YOUR_API_KEY")

resp = client.chat(
    model="qwen-flash",  # tiers: qwen-flash=1, qwen-turbo=2, qwen-plus=5 credits
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "用一句话解释什么是向量数据库"},
    ],
    request_id="demo-chat-001",  # idempotent: retries won't double-charge
)

print(resp["choices"][0]["message"]["content"])
print("remaining credits:", resp.get("remaining"))

# You can also use the official OpenAI SDK directly:
# from openai import OpenAI
# client = OpenAI(api_key="YOUR_API_KEY",
#                 base_url="https://trade.pianam.cn/api/v1/open")
# print(client.chat.completions.create(
#     model="qwen-flash",
#     messages=[{"role": "user", "content": "hello"}],
# ).choices[0].message.content)
