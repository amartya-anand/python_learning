class Product:
    """Represents a product in the ShopSmart catalog"""

    def __init__(self, sku, name, price, stock):
        self.sku = sku
        self.name = name
        self.price = price
        self.stock = stock

    def apply_discount(self, pct):
        """Return the discounted price"""
        return round(self.price * (1 - pct/100), 2)

    def is_available(self):
        """Check if available"""
        return self.stock > 0

    def sell(self, qty):
        """Reduce stock by qty if availabe"""
        if qty > self.stock:
            print(
                f"Insufficient stock for {self.name}! Available quantity is {self.stock}")
            return False
        self.stock -= qty
        print(f"Sold {qty}x{self.name}. Remaining stock: {self.stock}")
        return True

    def __str__(self):
        return f"[{self.sku}{self.name} - ${self.price:.2f}({self.stock} in stock)"


class Customer:
    """Represents a customer"""

    def __init__(self, customer_id, name, email, is_loyalty_member=False):
        self.customer_id = customer_id
        self.name = name
        self.email = email
        self.is_loyalty_member = is_loyalty_member
        self.purchase_history = []

    def apply_loyalty_discount(self, price):
        """Loyalty members get a special discount"""
        if self.is_loyalty_member:
            return round(price * 0.95, 2)
        return price

    def add_purchase(self, product_name, amount):
        self.purchase_history.append(
            {"product": product_name, "amount": amount})

    def total_spent(self):
        return sum(p["amount"] for p in self.purchase_history)

    def __str__(self):
        status = "Loyalty member" if self.is_loyalty_member else "Regular"
        return f"Customer({self.name},{self.email},{status})"


# ---- Demo  ----
mouse = Product("SKU001", "Wireless Mouse", 29.99, 150)
hub = Product("SKU002", "USB-C", 49.99, 75)

alice = Customer("C001", "Amartya Anand", "abc@qwe", is_loyalty_member=True)
bob = Customer("C002", "Dev", "dev.abc")

print(" === Products ===")
print(mouse)
print(hub)

print("\n===Customer===")
print(alice)
print(bob)

print(f"\n=== Alice buys a mouse ===")
original = mouse.price
loyalty_price = alice.apply_loyalty_discount(original)
print(f"Original: ${original:.2f} -> Loyalty price: ${loyalty_price:.2f}")
mouse.sell(1)
alice.add_purchase(mouse.name, loyalty_price)

print(f"\n=== Bob tries to buy 100 hubs ===")
hub.sell(100)
