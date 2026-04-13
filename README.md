# 🍔 FoodExpress - Online Food Ordering System

FoodExpress is a full-stack web application built using Django that allows users to browse restaurants, add items to cart, and place orders with secure online payment integration.

---

## 🚀 Features

- 🔐 User Authentication (Signup / Login / Logout)
- 🏠 Address Management (Add, Edit, Delete)
- 🍽️ Browse Restaurants & Food Items
- 🛒 Add to Cart Functionality
- 💳 Secure Payment Integration (Razorpay)
- 📦 Order Placement & Order History
- 📱 Fully Responsive Design

---

## 🛠️ Tech Stack

- **Backend:** Django (Python)
- **Frontend:** HTML, CSS, Tailwind CSS
- **Database:** SQLite
- **Payment Gateway:** Razorpay

---

## 📂 Project Structure

foodexpress/
|
│── Screenshots
├── accounts/ # User authentication & profile
├── restaurants/ # Restaurant & food items
├── orders/ # Order management
├── templates/ # HTML templates
├── static/ # CSS, JS files
├── media/ # Uploaded images
├── db.sqlite3 # Database (ignored in production)
├── manage.py


---

## ⚙️ Installation & Setup

### 1️⃣ Clone the repository
```bash
git clone https://github.com/your-username/food-express-django.git
2️⃣ Navigate to project
cd food-express-django
3️⃣ Create virtual environment (optional but recommended)
python -m venv venv
venv\Scripts\activate   # Windows
4️⃣ Install dependencies
pip install -r requirements.txt
5️⃣ Apply migrations
python manage.py migrate
6️⃣ Run the server
python manage.py runserver
7️⃣ Open in browser
http://127.0.0.1:8000/
💳 Payment Integration
Integrated with Razorpay

food-express-django/
│
├── screenshots/
│   ├── home.png
│   ├── naidu_menu.png
│   ├── kfc_menu.png
│   ├── dominos_menu.png
│   ├── profile.png

👉 Rename images properly (important for professionalism)

✅ Step 2: Add Screenshots in README.md

Paste this inside your README 👇

## 📸 Screenshots

### 🏠 Home Page
![Home Page](screenshots/home.png)

### 🍽️ Naidu Hotel Menu
![Naidu Menu](screenshots/naidu_menu.png)

### 🍗 KFC Menu
![KFC Menu](screenshots/kfc_menu.png)

### 🍕 Dominos Menu
![Dominos Menu](screenshots/dominos_menu.png)

### 👤 User Profile & Orders
![Profile](screenshots/profile.png)


👨‍💻 Author

Harsha V

📧 Email: harshavnaidu7@gmail.com
🔗 LinkedIn: https://linkedin.com/in/harsha-v-naidu/
💻 GitHub: https://github.com/harshanaidu6




