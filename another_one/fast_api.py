import threading
import time
import uvicorn
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional

app = FastAPI(title="ShopSmart Product API")

products_db = [
    {"id": 1, "Name": "USB-Hub", "Price": 45,
        "Stock": 50, "Category": "Electronics"},
    {"id": 2, "Name": "Monitor", "Price": 50,
        "Stock": 40, "Category": "Electronics"},
    {"id": 3, "Name": "Laptop stand", "Price": 15,
        "Stock": 20, "Category": "Accessories"},
]

next_id = 4


class ProductCreate(BaseModel):
    name: str
    price: float
    stock: int
    category: str


class ProductUpdate(BaseModel):
    name: Optional[str] = None
    price: Optional[float] = None
    stock: Optional[int] = None
    category: Optional[str] = None


@app.get("/")
def root():
    return {"message": "Welcome to ShopSmart Product API"}


@app.get("/products")
def list_products():
    return {"products": products_db, "count": len(products_db)}


@app.get("/products/{product_id}")
def get_product_id(product_id: int):
    for p in products_db:
        if p["id"] == product_id:
            return p
    raise HTTPException(status_code=404, detail="Product not found")


@app.post("/products", status_code=201)
def create_product(product: ProductCreate):
    global next_id
    new_product = {"id": next_id, **product.model_dump()}
    products_db.append(new_product)
    next_id += 1
    return new_product


@app.delete("/products/{product_id}")
def delete_product(product_id: int):
    for i, p in enumerate(products_db):
        if p["id"] == product_id:
            products_db.pop(i)
            return {"message": f"Product {product_id} deleted"}
    raise HTTPException(status_code=404, detail="Product not found")


# Use uvicorn.Server instead of uvicorn.run inside thread
config = uvicorn.Config(app=app, host="127.0.0.1", port=8000, log_level="info")
server = uvicorn.Server(config)

thread = threading.Thread(target=server.run, daemon=True)
thread.start()
time.sleep(2)

print("FastAPI server running on http://127.0.0.1:8000")
