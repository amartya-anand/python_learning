catalog = [
    {"sku": "PRO1", "name": "Mouse", "price": 250.99, "stock": 25},
    {"sku": "PRO2", "name": "Wireless Mouse", "price": 450, "stock": 30},
    {"sku": "PRO3", "name": "CPU", "price": 2250.99, "stock": 20},
    {"sku": "PRO4", "name": "Monitor", "price": 1250.34, "stock": 40}
]


def calculate_discount(price, discount_pct):
    """Calculate the discounted price"""
    # price = float(price)
    discounted_amount = price * (discount_pct / 100)
    return round(price - discounted_amount)


def get_products_in_stock(catalog, min_stock=0):
    """Return products with stock above min_stock"""
    return [p for p in catalog if p["stock"] > min_stock]


def catalog_value(catalog):
    """Calculate the value of entire inventory"""
    total = 0
    for product in catalog:
        total = total + product["price"] * product["stock"]
    return round(total, 2)

# Printing the data in tabular form


for p in catalog:
    sale_price = calculate_discount(p["price"], 10)  # 10% off
    print(f"{p["name"]:20s} | Price: ${p["price"]:>7.2f} | Sale: ${sale_price:>7.2f} | Stock: {p["stock"]}")

print(f"\nTotal Inventory Value: ${catalog_value(catalog):.2f}")

well_stocked = get_products_in_stock(catalog, min_stock=25)
print(f"Products with 50+ units: {[p["name"] for p in well_stocked]}")
