

# 🛒 QuickCommerceAPI

**QuickCommerceAPI** is a scalable, production-ready Django REST Framework-based eCommerce API platform for managing products, users, orders, payments, notifications, and reports with modular app architecture.

## 🚀 Features

- 🧑‍💼 JWT-based User Authentication & Roles
- 📦 Product Catalog & Inventory Management
- 🛍️ Cart, Orders, and Invoicing
- 💳 Payments Integration Ready (e.g., Razorpay, Stripe)
- 📊 Sales & Report Generation
- 🔔 Notifications (Email/SMS/PWA-ready)
- 🧾 Clean Modular Code (apps/users, apps/products, etc.)
- 🐳 Docker & PostgreSQL Ready for Production

## 📂 Project Structure

quickecommerceAPI/
├── apps/
│   ├── users/
│   ├── products/
│   ├── orders/
│   ├── payments/
│   ├── reports/
│   ├── notifications/
├── config/
│   ├── settings/
│   ├── urls.py
│   ├── asgi.py
│   ├── wsgi.py
├── manage.py


## 🔧 Installation Guide

### 1. Clone the Repo

```bash
git clone https://github.com/your-username/QuickCommerceAPI.git
cd QuickCommerceAPI

2. Create Virtual Environment

python -m venv env
source env/bin/activate  # On Windows use `env\Scripts\activate`
3. Install Dependencies

pip install -r requirements.txt
4. Setup Environment Variables
Create a .env file inside the config/ or project root:

DEBUG=True
SECRET_KEY=your_secret_key
DATABASE_URL=postgres://user:pass@localhost:5432/quickecommerce
ALLOWED_HOSTS=127.0.0.1,localhost
5. Apply Migrations

python manage.py migrate
6. Create Superuser

python manage.py createsuperuser
7. Run the Server

python manage.py runserver
8. API Access
Visit: http://127.0.0.1:8000/api/

🐳 Docker Deployment (Optional)
Build & Run

docker-compose up --build
📫 Contact
Author: Manish Sharma
📧 Email: manis.shr@gmail.com



### ✅ `LICENSE` (MIT License)

```text
MIT License

Copyright (c) 2025 Manish Sharma

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

