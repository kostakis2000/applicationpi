import requests

BASE_URL = "http://127.0.0.1:5000/products"

# Function to add a product
def add_product(name, description, price):
    payload = {
        "name": name,
        "description": description,
        "price": price
    }
    response = requests.post(BASE_URL, json=payload)
    if response.status_code == 201:
        print("Product added:", response.json())
    else:
        print("Failed to add product:", response.json())

# Function to retrieve all products
def get_products():
    response = requests.get(BASE_URL)
    if response.status_code == 200:
        print("Products:", response.json())
    else:
        print("Failed to fetch products:", response.json())

if __name__ == "__main__":
    # Example usage: Add products and retrieve the list
    add_product("Laptop", "A high-performance laptop", 1500.0)
    add_product("Phone", "A latest-gen smartphone", 800.0)
    get_products()
