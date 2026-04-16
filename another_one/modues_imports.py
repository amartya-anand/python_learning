import json
from datetime import datetime, timedelta
from collections import Counter

# --- JSON Serialize product catalog --- #

catalog = [
    {"sku": "SKU001", "Name": "USB-Hub", "Stock": 120, "Price": 25},
    {"sku": "SKU002", "Name": "Mouse", "Stock": 100, "Price": 45},
    {"sku": "SKU003", "Name": "Wireless Mouse", "Stock": 140, "Price": 50}

]

json_catalog = json.dumps(catalog, indent=2)
print("=== Catalog as JSON ===")
print(json_catalog)
