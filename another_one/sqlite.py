import random
from datetime import datetime, timedelta
import sqlite3

# :memory helps in making sure the data is not persistent and is only stored in RAM for the duration of the program's execution. This is useful for testing and temporary data storage, as it allows for quick access to data without the need for disk I/O operations. However, it also means that any data stored in the database will be lost once the program terminates or the connection is closed.To make the data persistent one can use name_of_the file.db instead of :memory.
conn = sqlite3.connect(":memory:")
conn.row_factory = sqlite3.Row
# Increases readability and usability of the data retrieved from the database. It allows us to access columns by their names instead of relying on index positions, making the code more intuitive and less error-prone. This is particularly useful when working with complex queries or when the structure of the database may change over time, as it reduces the risk of breaking the code due to changes in column order.
cursor = conn.cursor()
# Cursor is a controller that allows us to execute SQL commands and queries against the database. It acts as an intermediary between the application and the database, enabling us to send SQL statements, retrieve results, and manage transactions.
# conn object manages the connection to the database, allowing us to execute SQL commands, manage transactions, and handle database operations. It provides methods for committing changes, rolling back transactions, and closing the connection when it's no longer needed. The conn object is essential for maintaining a stable and efficient interaction with the database throughout the application's lifecycle.
# --- Create tables --- #
# executescript() method allows us to execute multiple SQL statements in a single call.
cursor.executescript("""
	CREATE TABLE products(
		id INTEGER PRIMARY KEY AUTOINCREMENT,
		name TEXT NOT NULL,
		price REAL NOT NULL,
		stock REAL NOT NULL DEFAULT 0,
		category TEXT
	);

	CREATE TABLE orders(
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	customer_name TEXT NOT NULL,
	order_date TEXT NOT NULL,
	total REAL NOT NULL DEFAULT 0
	);

	CREATE TABLE order_items(
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	order_id INTEGER NOT NULL,
	product_id INTEGER NOT NULL,
	quantity INTEGER NOT NULL,
	unit_price REAL NOT NULL,
	FOREIGN KEY (order_id) REFERENCES orders(id),
	FOREIGN KEY (product_id) REFERENCEs products(id)
	);
""")


# --- Insert sample data --- #
products_data = [
    ("Wireless", 20, 100, "Electronics"),
    ("USB-C ", 10, 120, "Electronics"),
    ("Laptop Stand", 30, 140, "Accessories"),
    ("Webcam", 20, 30, "Accessories"),
    ("Desk Organizer", 35, 80, "Accessories"),
    ("Keyboard Wireless", 10, 50, "Accessories"),
]
# Execute the same SQL statement multiple times with different parameter values. It allows us to efficiently insert multiple rows of data into the database in a single operation, reducing the overhead of executing individual insert statements for each row. This is particularly useful when dealing with large datasets or when performing batch inserts, as it improves performance and minimizes the number of round trips to the database.
cursor.executemany(
    "INSERT INTO products(name,price,stock,category) VALUES (?,?,?,?)",
    products_data
)

# This code simulates a small e-commerce database. It creates random orders, calculates their totals, saves them in a database, and then runs a few SQL queries to display information.

base_date = datetime(2025, 3, 1)
for i in range(10):
    order_date = (base_date + timedelta(days=random.randint(0, 30))
                  ).strftime("%Y-%m-%d")
    customer = random.choice(
        ["Alice Johnson", "Bob Smith", "Carol White", "Dave Brown"])
    cursor.execute(
        "INSERT INTO orders (customer_name, order_date, total) VALUES (?, ?, 0)",
        (customer, order_date)
    )
    order_id = cursor.lastrowid

    # Add 1-3 random items per order
    num_items = random.randint(1, 3)
    order_total = 0
    for _ in range(num_items):
        prod_id = random.randint(1, 6)
        qty = random.randint(1, 5)
        cursor.execute("SELECT price FROM products WHERE id = ?", (prod_id,))
        price = cursor.fetchone()["price"]
        cursor.execute(
            "INSERT INTO order_items (order_id, product_id, quantity, unit_price) VALUES (?, ?, ?, ?)",
            (order_id, prod_id, qty, price)
        )
        order_total += price * qty

    cursor.execute("UPDATE orders SET total = ? WHERE id = ?",
                   (round(order_total, 2), order_id))

conn.commit()
# --- Query data ---
print("=== All Products ===")
for row in cursor.execute("SELECT * FROM products"):
    print(f"  [{row['id']}] {row['name']:20s} | ${row['price']:>7.2f} | Stock: {int(row['stock']):>3d} | {row['category']}")

print("\n=== Recent Orders ===")
for row in cursor.execute("SELECT * FROM orders ORDER BY order_date DESC LIMIT 5"):
    print(
        f"  Order #{row['id']} | {row['customer_name']:15s} | {row['order_date']} | Total: ${row['total']:>7.2f}")

print("\n=== Inventory Value by Category ===")
query = """
    SELECT category, COUNT(*) as num_products,
           SUM(price * stock) as total_value
    FROM products
    GROUP BY category
"""
for row in cursor.execute(query):
    print(
        f"  {row['category']:15s} | {row['num_products']} products | Value: ${row['total_value']:>10,.2f}")
