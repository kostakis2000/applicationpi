# Simple REST API for Product Management

This project demonstrates a REST API built using Python with Flask and a client script to interact with the API.

## Setup Instructions

### 1. Prerequisites
- Python 3.8 or later
- pip (Python package installer)

### 2. Install Dependencies
1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd product_api
### 3 Set up a virtual environment (optional):
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

### 4 Install the required libraries:
pip install -r requirements.txt

### 5 Run the API Server

python app.py
### 6 Interact with the API

Add products:
curl -X POST -H "Content-Type: application/json" \
-d '{"name":"Tablet","description":"A lightweight tablet","price":600.0}' \
http://127.0.0.1:5000/products


retrieve all product: 
curl http://127.0.0.1:5000/products


