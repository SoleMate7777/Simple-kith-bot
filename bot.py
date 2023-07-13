import requests
import time
# import pyfiglet module
import pyfiglet

result = pyfiglet.figlet_format("YEAR UP BOT")
print(result)



# Define the product link

product_link = input("Enter the product link: ")
# Define the size of the product
size = input("Enter the size of the product: ")
# Define the number of products
number_of_products = int(input("Enter the number of products: "))
# Define the name
name = input("Enter your name: ")
# Define the address info
address_info = {
    "address": input("Enter your address: "),
    "city": input("Enter your city: "),
    "state": input("Enter your state: "),
    "zip code": input("Enter your zip code: ")
}
# Define the credit card info
credit_card_info = {
    "card number": input("Enter your credit card number: "),
    "expiration date": input("Enter your credit card expiration date: "),
    "cvv": input("Enter your credit card CVV: ")
}
# Create a session with the KITH website
session = requests.Session()
# Set the headers for the session
session.headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:97.0) Gecko/20100101 Firefox/97.0",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "gzip, deflate, br",
    "Referer": "https://kith.com/products/nike-air-jordan-1-retro-high-og-dark-mocha",
    "DNT": "1",
    "Connection": "keep-alive",
    "Upgrade-Insecure-Requests": "1"
}
# Get the product page from the KITH website
product_page = session.get(product_link)
# Check if the product is in stock
if product_page.status_code == 200:
    # The product is in stock, so proceed to checkout
    # Get the product price
    product_price = product_page.json()["price"]
    # Create the cart
    cart = session.post("https://kith.com/cart", json={"items": [{"product_id": product_page.json()["id"], "quantity": number_of_products}]})
    # Get the cart ID
    cart_id = cart.json()["id"]
    # Checkout the cart
    checkout = session.post("https://kith.com/checkout", json={"cart_id": cart_id})
    # Get the checkout token
    checkout_token = checkout.json()["token"]
    # Submit the checkout form
    submit_checkout = session.post("https://kith.com/checkout/submit", json={"token": checkout_token, "name": name, "email": "john.doe@example.com", "address": address_info, "payment_method": {"type": "credit_card", "card_number": credit_card_info["card number"], "expiration_date": credit_card_info["expiration date"], "cvv": credit_card_info["cvv"]}})
    # Check the status of the checkout
    if submit_checkout.status_code == 200:
        # The checkout was successful, so print a message
        print("Checkout successful!")
    else:
        # The checkout failed, so print a message
        print("Checkout failed!")
else:
    # The product is out of stock, so print a message
    print("Product is out of stock!")