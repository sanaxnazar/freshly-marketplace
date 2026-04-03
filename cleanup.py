from pymongo import MongoClient
import certifi

client = MongoClient("mongodb+srv://sana_nazar:sana_nazar@shop.cb76vbq.mongodb.net/", tlsCAFile=certifi.where())
db = client["shopping_db"]

# 1. DELETE EVERYTHING
db["products"].delete_many({})
print("🗑️ Database swiped clean!")

# 2. RUN YOUR SEED SCRIPT IMMEDIATELY AFTER
# (Copy-paste your latest seed_db.py logic here or just run seed_db.py)