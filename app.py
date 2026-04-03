from flask import Flask, render_template, request, jsonify, session, redirect
from pymongo import MongoClient
from bson import ObjectId
import os
import certifi

app = Flask(__name__)
# 1. CRITICAL: This allows the "Automatic ID" to be stored in the browser session
app.secret_key = os.urandom(24)

# 2. Connection Settings
MONGO_URI = "mongodb+srv://sana_nazar:sana_nazar@shop.cb76vbq.mongodb.net/?appName=shop"
ca = certifi.where()
client = MongoClient(MONGO_URI, tlsCAFile=ca)
db = client["shopping_db"]

# Collections
products_col = db["products"]
users_col    = db["users"]
carts_col    = db["cart"]

@app.route("/")
def index():
    query = request.args.get("q", "")
    category = request.args.get("category", "")
    
    # Filter logic for the Search Bar and Category Chips
    filter_query = {}
    if query: filter_query["name"] = {"$regex": query, "$options": "i"}
    if category: filter_query["category"] = category
    
    products = []
    for p in products_col.find(filter_query):
        p["_id"] = str(p["_id"])
        products.append(p)
        
    categories = products_col.distinct("category")
    return render_template("index.html", products=products, 
                           categories=categories, 
                           active_category=category, 
                           query=query, 
                           user_name=session.get("user_name"))

# 3. Registration (Automatic Login)
@app.route("/register", methods=["POST"])
def register():
    data = request.get_json()
    if users_col.find_one({"email": data['email']}):
        return jsonify({"error": "Email already exists"}), 400
    
    user = users_col.insert_one(data)
    # Store ID automatically so we don't need popups later
    session["user_id"] = str(user.inserted_id)
    session["user_name"] = data['name']
    return jsonify({"message": "Account created successfully!"})
# 4. Login Route (Matches the Freshly design)
@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')
    
    # Check if this email and password exist in your MongoDB 'users' collection
    user = users_col.find_one({"email": email, "password": password})
    
    if user:
        # Store the ID and Name in the session so the cart works automatically
        session["user_id"] = str(user["_id"])
        session["user_name"] = user["name"]
        return jsonify({"message": "Welcome back!"}), 200
    else:
        # If no user found, return an error so the modal can show it
        return jsonify({"error": "Invalid email or password"}), 401

# 4. Add to Cart (Uses the Session ID)
@app.route("/add_to_cart", methods=["POST"])
def add_to_cart():
    user_id = session.get("user_id")
    if not user_id:
        return jsonify({"error": "Please log in or register first."}), 401
    
    product_id = request.get_json().get("product_id")
    
    # Update the user's cart document in MongoDB
    carts_col.update_one(
        {"user_id": ObjectId(user_id)},
        {"$addToSet": {"items": ObjectId(product_id)}},
        upsert=True
    )
    return jsonify({"message": "Added to your Bag!"})

@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")

@app.route("/cart")
def view_cart():
    user_id = session.get("user_id")
    if not user_id:
        return redirect("/") # Send them back home if not logged in

    # 1. Find the cart for this user
    user_cart = carts_col.find_one({"user_id": ObjectId(user_id)})
    
    cart_items = []
    total_price = 0

    if user_cart and "items" in user_cart:
        # 2. Loop through IDs and get full product details
        for prod_id in user_cart["items"]:
            product = products_col.find_one({"_id": prod_id})
            if product:
                product["_id"] = str(product["_id"])
                cart_items.append(product)
                total_price += product["price"]

    return render_template("cart.html", items=cart_items, total=total_price)

@app.route("/checkout", methods=["POST"])
def checkout():
    user_id = session.get("user_id")
    if user_id:
        # Clear the cart after "buying"
        carts_col.delete_one({"user_id": ObjectId(user_id)})
        return jsonify({"message": "Success! Your organic order is on the way. 🌿"})
    return jsonify({"error": "Unauthorized"}), 401

if __name__ == "__main__":
    app.run(debug=True)