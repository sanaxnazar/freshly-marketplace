from pymongo import MongoClient
import certifi

MONGO_URI = "mongodb+srv://sana_nazar:sana_nazar@shop.cb76vbq.mongodb.net/?appName=shop"
client = MongoClient(MONGO_URI, tlsCAFile=certifi.where())
db = client["shopping_db"]

products = [
    # --- FRUITS ---
    {"name": "Organic Bananas", "price": 0.99, "original_price": 1.50, "unit": "kg", "category": "Fruits", "badge": "Organic", "image_url": "https://images.pexels.com/photos/6848574/pexels-photo-6848574.jpeg?auto=compress&cs=tinysrgb&w=600"},
    {"name": "Red Gala Apples", "price": 2.49, "original_price": 3.20, "unit": "kg", "category": "Fruits", "badge": "Best Seller", "image_url": "https://images.pexels.com/photos/102104/pexels-photo-102104.jpeg?auto=compress&cs=tinysrgb&w=600"},
    {"name": "Avocado Bundle", "price": 4.50, "original_price": 5.99, "unit": "3 pcs", "category": "Fruits", "badge": "Popular", "image_url": "https://images.pexels.com/photos/557659/pexels-photo-557659.jpeg?auto=compress&cs=tinysrgb&w=600"},
    {"name": "Fresh Strawberries", "price": 3.50, "original_price": 4.50, "unit": "250g", "category": "Fruits", "badge": "Sweet", "image_url": "https://images.pexels.com/photos/31020869/pexels-photo-31020869.jpeg?auto=compress&cs=tinysrgb&w=600"},
    {"name": "Juicy Oranges", "price": 3.99, "original_price": 4.99, "unit": "kg", "category": "Fruits", "badge": "Vitamin C", "image_url": "https://images.pexels.com/photos/32853430/pexels-photo-32853430.jpeg?auto=compress&cs=tinysrgb&w=600"},

    # --- VEGETABLES ---
    {"name": "Fresh Broccoli", "price": 1.80, "original_price": 2.50, "unit": "head", "category": "Vegetables", "badge": "Fresh", "image_url": "https://images.pexels.com/photos/47347/broccoli-vegetable-food-healthy-47347.jpeg?auto=compress&cs=tinysrgb&w=600"},
    {"name": "Cherry Tomatoes", "price": 2.99, "original_price": 3.99, "unit": "250g", "category": "Vegetables", "badge": "Organic", "image_url": "https://images.pexels.com/photos/533342/pexels-photo-533342.jpeg?auto=compress&cs=tinysrgb&w=600"},
    {"name": "Orange Carrots", "price": 1.20, "original_price": 1.80, "unit": "kg", "category": "Vegetables", "badge": "Crunchy", "image_url": "https://images.pexels.com/photos/143133/pexels-photo-143133.jpeg?auto=compress&cs=tinysrgb&w=600"},
    {"name": "Bell Peppers", "price": 2.50, "original_price": 3.50, "unit": "3 pcs", "category": "Vegetables", "badge": "Mixed", "image_url": "https://images.pexels.com/photos/1434254/pexels-photo-1434254.jpeg?auto=compress&cs=tinysrgb&w=600"},

    # --- DAIRY ---
    {"name": "Whole Milk (1L)", "price": 1.50, "original_price": 1.99, "unit": "bottle", "category": "Dairy", "badge": "Essential", "image_url": "https://images.pexels.com/photos/248412/pexels-photo-248412.jpeg?auto=compress&cs=tinysrgb&w=600"},
    {"name": "Free-Range Eggs", "price": 4.99, "original_price": 5.50, "unit": "12ct", "category": "Dairy", "badge": "Organic", "image_url": "https://images.pexels.com/photos/162712/egg-white-food-protein-162712.jpeg?auto=compress&cs=tinysrgb&w=600"},
    {"name": "Greek Yogurt", "price": 5.20, "original_price": 6.50, "unit": "500g", "category": "Dairy", "badge": "High Protein", "image_url": "https://images.pexels.com/photos/4109944/pexels-photo-4109944.jpeg?auto=compress&cs=tinysrgb&w=600"},
    {"name": "Cheddar Cheese", "price": 6.00, "original_price": 7.20, "unit": "200g", "category": "Dairy", "badge": "Aged", "image_url": "https://images.pexels.com/photos/821365/pexels-photo-821365.jpeg?auto=compress&cs=tinysrgb&w=600"},

    # --- BAKERY & SNACKS ---
    {"name": "Sourdough Bread", "price": 5.50, "original_price": 6.50, "unit": "loaf", "category": "Bakery", "badge": "Fresh", "image_url": "https://images.pexels.com/photos/1775043/pexels-photo-1775043.jpeg?auto=compress&cs=tinysrgb&w=600"},
    {"name": "Blueberry Muffins", "price": 4.50, "original_price": 5.50, "unit": "4 units", "category": "Bakery", "badge": "New", "image_url": "https://images.pexels.com/photos/2014693/pexels-photo-2014693.jpeg?auto=compress&cs=tinysrgb&w=600"},
    {"name": "Roasted Almonds", "price": 8.50, "original_price": 9.99, "unit": "250g", "category": "Snacks", "badge": "Healthy", "image_url": "https://images.pexels.com/photos/3939170/pexels-photo-3939170.jpeg?auto=compress&cs=tinysrgb&w=600"},
    {"name": "Dark Chocolate", "price": 3.00, "original_price": 4.00, "unit": "bar", "category": "Snacks", "badge": "70% Cocoa", "image_url": "https://images.pexels.com/photos/4113340/pexels-photo-4113340.jpeg?auto=compress&cs=tinysrgb&w=600"},
    {"name": "Sea Salt Crisps", "price": 2.99, "original_price": 3.50, "unit": "150g", "category": "Snacks", "badge": "Classic", "image_url": "https://images.pexels.com/photos/3434523/pexels-photo-3434523.jpeg?auto=compress&cs=tinysrgb&w=600"}
]

db["products"].delete_many({})
db["products"].insert_many(products)
print(f"✅ Successfully loaded {len(products)} Pexels-style items!")