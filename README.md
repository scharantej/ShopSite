## **Flask Application Design**

## **Problem:** Build an e-commerce website.

## **HTML Files**

- **home.html:** This will be the homepage of the website, displaying featured products and categories.
- **product.html:** This will showcase the details of a specific product, allowing users to add it to their cart.
- **cart.html:** This will display the user's shopping cart, allowing them to view and edit its contents.
- **checkout.html:** This will handle the checkout process, collecting customer information and payment details.

## **Routes**

- **GET /:** Main page route, serves the `home.html` file.
- **GET /product/:product_id:** Product details page route, serves the `product.html` file.
- **POST /add_to_cart:** Route for adding items to the cart, updates the cart content and redirects to the cart page.
- **GET /cart:** Cart page route, serves the `cart.html` file.
- **GET /checkout:** Checkout page route, serves the `checkout.html` file.
- **POST /place_order:** Route for placing an order, processes payment details and saves the order.
- **GET /order_history:** Order history page route, displays previously placed orders.