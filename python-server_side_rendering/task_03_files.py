from flask import Flask, render_template, request
import json
import csv
import os

app = Flask(__name__)

def read_json_products(filepath):
    try:
        with open(filepath, 'r') as f:
            data = json.load(f)
        return [dict(p) for p in data]
    except Exception:
        return None

def read_csv_products(filepath):
    try:
        with open(filepath, newline='') as f:
            reader = csv.DictReader(f)
            data = []
            for row in reader:
                # Convert fields for consistency
                try:
                    row['id'] = int(row['id'])
                except Exception:
                    row['id'] = row['id']
                try:
                    row['price'] = float(row['price'])
                except Exception:
                    row['price'] = row['price']
                data.append(row)
        return data
    except Exception:
        return None

@app.route('/products')
def display_products():
    source = request.args.get('source')
    id_param = request.args.get('id')
    error_msg = None
    products = []

    if source == 'json':
        products = read_json_products('products.json')
    elif source == 'csv':
        products = read_csv_products('products.csv')
    else:
        error_msg = "Wrong source"
        return render_template("product_display.html", error=error_msg, products=None)

    if products is None:
        error_msg = f"Could not read {source} data."
        return render_template("product_display.html", error=error_msg, products=None)

    # Filter by ID if provided
    if id_param:
        try:
            id_value = int(id_param)
        except Exception:
            error_msg = "Invalid id parameter."
            return render_template("product_display.html", error=error_msg, products=None)
        filtered = [prod for prod in products if int(prod.get('id', -1)) == id_value]
        if not filtered:
            error_msg = "Product not found"
            return render_template("product_display.html", error=error_msg, products=None)
        else:
            products = filtered

    return render_template("product_display.html", error=None, products=products)

if __name__ == "__main__":
    app.run(debug=True, port=5000)
