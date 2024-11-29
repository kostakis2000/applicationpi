from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory storage for products
products = []

# POST endpoint to create a new product
@app.route('/products', methods=['POST'])
def create_product():
    data = request.get_json()
    if not data or 'name' not in data or 'description' not in data or 'price' not in data:
        return jsonify({"error": "Invalid input"}), 400
    
    product = {
        "id": len(products) + 1,
        "name": data['name'],
        "description": data['description'],
        "price": data['price']
    }
    products.append(product)
    return jsonify(product), 201

# GET endpoint to retrieve all products
@app.route('/products', methods=['GET'])
def get_products():
    return jsonify(products), 200

if __name__ == '__main__':
    app.run(debug=True)
