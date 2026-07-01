import sqlite3

# :memory helps in making sure the data is not persistent and is only stored in RAM for the duration of the program's execution. This is useful for testing and temporary data storage, as it allows for quick access to data without the need for disk I/O operations. However, it also means that any data stored in the database will be lost once the program terminates or the connection is closed.To make the data persistent one can use name_of_the file.db instead of :memory.
conn = sqlite3.connect(":memory:")
conn.row_factory = sqlite.Row  # Increases readability and usability of the data retrieved from the database. It allows us to access columns by their names instead of relying on index positions, making the code more intuitive and less error-prone. This is particularly useful when working with complex queries or when the structure of the database may change over time, as it reduces the risk of breaking the code due to changes in column order.
cursor = conn.cursor()  # Cursor is a controller that allows us to execute SQL commands and queries against the database. It acts as an intermediary between the application and the database, enabling us to send SQL statements, retrieve results, and manage transactions.
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
	FOREIGN KEY (product_id) REFERENCE products(id)
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
