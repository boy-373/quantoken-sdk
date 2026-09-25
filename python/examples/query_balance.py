import os
from quantoken import QuantumTokenClient

API_KEY = os.environ.get("QUANTOKEN_API_KEY", "YOUR_KEY_HERE")
client = QuantumTokenClient(api_key=API_KEY)

print("=== balance ===")
print(client.balance())
