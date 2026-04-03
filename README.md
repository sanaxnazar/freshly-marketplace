**🌿 Freshly Marketplace**

Freshly Marketplace is a full-stack e-commerce web application built for the modern grocery shopping experience. It connects users with fresh, organic produce through a clean, responsive interface.

**🚀 Live Demo:** https://freshly-marketplace.onrender.com/

**✨ Features**

Dynamic Product Catalog: Real-time rendering of grocery items (Fruits, Vegetables, Dairy) sourced from MongoDB Atlas.

Green Theme Branding: A custom-designed UI focused on an organic, "fresh" aesthetic.

Secure Database Integration: Uses Environment Variables for secure connection to cloud databases.

Responsive Design: Fully optimized for both desktop and mobile browsing.

Search Functionality: Quickly find specific fresh picks across categories.

**🛠️ Tech Stack**

Frontend: HTML5, CSS3 (Custom Flexbox/Grid Layouts)

Backend: Python 🐍 + Flask

Database: MongoDB Atlas (NoSQL)

Deployment: Render (Cloud Hosting)

Security: python-dotenv for API keys and certifi for SSL Handshake.

**🚀 Local Setup Instructions**

If you want to run this project locally, follow these steps:

**Clone the repository:**

Bash

git clone https://github.com/sanaxnazar/freshly-marketplace.git

cd freshly-marketplace

Create a Virtual Environment:

Bash

python -m venv venv

source venv/bin/activate  # On Windows: venv\Scripts\activate

Install Dependencies:

Bash

pip install -r requirements.txt

Set up Environment Variables:

Create a .env file and add your MongoDB connection:

Code snippet

MONGO_URI=your_mongodb_atlas_uri_here

SECRET_KEY=your_secret_key
Run the App:

Bash
python app.py
View at http://127.0.0.1:5000

📂 Project Structure

Plaintext

├── app.py              # Main Flask Application

├── seed_db.py          # Script to populate MongoDB with initial data

├── requirements.txt     # List of Python dependencies

├── vercel.json         # Deployment configuration

├── static/

│   ├── css/            # Stylesheets

│   └── images/         # Product and branding assets
└── templates/
    └── index.html      # Main frontend template

**👤 Author**

Sana Nazar

GitHub: @sanaxnazar

