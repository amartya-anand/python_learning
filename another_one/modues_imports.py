import json
from datetime import datetime, timedelta
from collections import Counter

# # --- JSON Serialize product catalog --- #

# catalog = [
#     {"sku": "SKU001", "Name": "USB-Hub", "Stock": 120, "Price": 25},
#     {"sku": "SKU002", "Name": "Mouse", "Stock": 100, "Price": 45},
#     {"sku": "SKU003", "Name": "Wireless Mouse", "Stock": 140, "Price": 50}

# ]

# json_catalog = json.dumps(catalog, indent=2)
# print("=== Catalog as JSON ===")
# print(json_catalog)

# # Pars JSON back to Python

# parsed = json.loads(json_catalog)
# print(f"\nParsed back : {len(parsed)} products, first = {parsed[0]["Name"]}")
# # print(parsed)


# --- Order dates --- #

order_date = datetime(2026, 4, 16, 13, 00)
delivery_date = order_date + timedelta(days=5)
print(f"Order placed: {order_date.strftime('%Y-%m-%d %H:%M')}")
print(f"Expected delivery : {delivery_date.strftime('%B-%d, %Y')}")
print(f"Days until delivery: {(delivery_date - order_date).days}")
