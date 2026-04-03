import os
from dotenv import load_dotenv
from flask import Flask, render_template, request, redirect, url_for, session, jsonify
from pymongo import MongoClient
from bson.objectid import ObjectId  # MISSING: Needed for MongoDB IDs
import certifi

# 1. Load the secret variables
load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY", "fallback-secret-key-123")

# 2. Secure MongoDB Connection
MONGO_URI = os.getenv("MONGO_URI")
client = MongoClient(MONGO_URI, tlsCAFile=certifi.where())
db = client["shopping_db"]

# MISSING: Define your collections so the code knows where to look
products_col = db["products"]
users_col = db["users"]
carts_col = db["carts"]

# --- Your Routes ---

@app.route("/")
def index():
    query = request.args.get("q", "")
    category = request.args.get("category", "")
    
    filter_query = {}
    if query: 
        filter_query["name"] = {"$regex": query, "$options": "i"}
    if category: 
        filter_query["category"] = category
    
    products = []
    # FIXED: Actually calling the collection here
    for p in products_col.find(filter_query):
        p["_id"] = str(p["_id"])
        products.append(p)
        
    categories = products_col.distinct("category")
    return render_template("index.html", 
                           products=products, 
                           categories=categories, 
                           active_category=category, 
                           query=query, 
                           user_name=session.get("user_name"))

@app.route("/register", methods=["POST"])
def register():
    data = request.get_json()
    if users_col.find_one({"email": data['email']}):
        return jsonify({"error": "Email already exists"}), 400
    
    user = users_col.insert_one(data)
    session["user_id"] = str(user.inserted_id)
    session["user_name"] = data['name']
    return jsonify({"message": "Account created successfully!"})

@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')
    
    user = users_col.find_one({"email": email, "password": password})
    
    if user:
        session["user_id"] = str(user["_id"])
        session["user_name"] = user["name"]
        return jsonify({"message": "Welcome back!"}), 200
    else:
        return jsonify({"error": "Invalid email or password"}), 401

@app.route("/add_to_cart", methods=["POST"])
def add_to_cart():
    user_id = session.get("user_id")
    if not user_id:
        return jsonify({"error": "Please log in or register first."}), 401
    
    data = request.get_json()
    product_id = data.get("product_id")
    
    # FIXED: Added ObjectId conversion to ensure MongoDB finds the right records
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
        return redirect("/") 

    user_cart = carts_col.find_one({"user_id": ObjectId(user_id)})
    
    cart_items = []
    total_price = 0

    if user_cart and "items" in user_cart:
        for prod_id in user_cart["items"]:
            product = products_col.find_one({"_id": prod_id})
            if product:
                product["_id"] = str(product["_id"])
                cart_items.append(product)
                total_price += product.get("price", 0)

    return render_template("cart.html", items=cart_items, total=total_price)

@app.route("/checkout", methods=["POST"])
def checkout():
    user_id = session.get("user_id")
    if user_id:
        carts_col.delete_one({"user_id": ObjectId(user_id)})
        return jsonify({"message": "Success! Your organic order is on the way. 🌿"})
    return jsonify({"error": "Unauthorized"}), 401

if __name__ == "__main__":
    app.run(debug=True)