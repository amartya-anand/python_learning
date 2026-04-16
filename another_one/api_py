import requests

url = "https://dummyjson.com/products?limit=5"
response = requests.get(url)

print(f"Status code : {response.status_code}")
print(f"Content type : {response.headers.get('Content-type')}\n")

if response.status_code == 200:
    data = response.json()
    products = data["products"]

    print(f"=== Fetched === {len(products)} Products from Dummy JSON ===\n")
    for p in products:
        print(f" {p["title"]}")
        print(
            f" Price : ${p["price"]:.2f} | Rating : {p["rating"]} | Category : {p["category"]}")
        print()
else:
    print(f"Error: {response.status_code}")

# --- Error Handling --- #

print(f"=== Handling a bad request ===")
bad_response = requests.get("https://dummyjson.com/products/99999")
print(f"Status : {bad_response.status_code}")
if bad_response.status_code != 200:
    print(
        f"Error response: {bad_response.json().get("message", "Unknown error")}")
