
# Import necessary modules
from flask import Flask, render_template, request, redirect, url_for
import os

# Create a Flask app
app = Flask(__name__)

# Define the main page route
@app.route('/')
def home():
    return render_template('home.html')

# Define the product details page route
@app.route('/product/<product_id>')
def product(product_id):
    return render_template('product.html', product_id=product_id)

# Define the add to cart route
@app.route('/add_to_cart', methods=['POST'])
def add_to_cart():
    product_id = request.form.get('product_id')
    quantity = request.form.get('quantity')
    # Add the product to the cart
    cart[product_id] = quantity
    return redirect(url_for('cart'))

# Define the cart page route
@app.route('/cart')
def cart():
    return render_template('cart.html', cart=cart)

# Define the checkout page route
@app.route('/checkout')
def checkout():
    return render_template('checkout.html')

# Define the place order route
@app.route('/place_order', methods=['POST'])
def place_order():
    # Process the payment details
    # Save the order
    return redirect(url_for('order_history'))

# Define the order history page route
@app.route('/order_history')
def order_history():
    return render_template('order_history.html')

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
