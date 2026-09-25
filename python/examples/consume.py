import os
from quantoken import QuantumTokenClient

API_KEY = os.environ.get("QUANTOKEN_API_KEY", "YOUR_KEY_HERE")
client = QuantumTokenClient(api_key=API_KEY)

print("=== consume once ===")
print(client.consume(amount=1, idempotency_key="demo-001"))
