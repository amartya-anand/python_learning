import threading
import time
import sqlite3
import uvicorn
import requests
import json
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional

# --- Setup SQLite DB ---
DB_PATH = "shopsmart_api.db"

# Helper function


def get_db():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    conn = get_db()
    conn.executescript("""
        DROP TABLE IF EXISTS api_products;
        CREATE TABLE api_products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            price REAL NOT NULL,
            stock INTEGER NOT NULL DEFAULT 0,
            category TEXT NOT NULL
        );
        INSERT INTO api_products (name, price, stock, category) VALUES
            ('Wireless Mouse', 29.99, 150, 'electronics'),
            ('USB-C Hub', 49.99, 75, 'electronics'),
            ('Laptop Stand', 89.99, 30, 'accessories'),
            ('Webcam HD', 69.99, 60, 'electronics');
    """)
    conn.commit()
    conn.close()


init_db()
