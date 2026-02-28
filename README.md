# Mini Marketplace API

A RESTful API for a Mini Marketplace system built with Django and Django REST Framework.

## Project Overview

This project simulates a simplified e-commerce backend where users can:
- Register and authenticate with JWT
- Browse and list products by category
- Add items to shopping cart
- Place orders

## Tech Stack

- **Python** - Programming language
- **Django** - Web framework
- **Django REST Framework** - API framework
- **JWT Authentication** - User authentication
- **SQLite** - Database (development)

## Project Structure

```
mini_marketplace/
├── config/              # Django project settings
├── mini_marketplace/    # Main marketplace app
├── manage.py           # Django management script
├── db.sqlite3          # SQLite database
└── venv/              # Virtual environment
```

## Setup Instructions

### Prerequisites
- Python 3.8+
- pip

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/matan-workneh7/mini_marketplace.git
   cd mini_marketplace
   ```

2. **Create and activate virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install django djangorestframework djangorestframework-simplejwt
   ```

4. **Run database migrations**
   ```bash
   python manage.py migrate
   ```

5. **Start the development server**
   ```bash
   python manage.py runserver
   ```

6. **Access the API**
   - API Base URL: http://127.0.0.1:8000/api/
   - Admin Panel: http://127.0.0.1:8000/admin/

## API Endpoints (Planned)

### Authentication
- `POST /api/auth/register/` - User registration
- `POST /api/auth/login/` - User login (JWT)

### Categories
- `GET /api/categories/` - List all categories
- `POST /api/categories/` - Create category (auth required)
- `GET /api/categories/<id>/` - Get category details

### Products
- `GET /api/products/` - List all products
- `POST /api/products/` - Create product (auth required)
- `GET /api/products/<id>/` - Get product details
- `PUT /api/products/<id>/` - Update product (owner only)
- `DELETE /api/products/<id>/` - Delete product (owner only)

### Cart
- `GET /api/cart/` - View user's cart (auth required)
- `POST /api/cart/add/` - Add item to cart (auth required)
- `PUT /api/cart/update/` - Update cart item quantity (auth required)
- `DELETE /api/cart/remove/` - Remove item from cart (auth required)

### Orders
- `POST /api/orders/checkout/` - Create order from cart (auth required)
- `GET /api/orders/` - List user's orders (auth required)
- `GET /api/orders/<id>/` - Get order details (auth required)

## Current Status

### ✅ Completed
- Django project setup
- Virtual environment configuration
- DRF and JWT installation
- Database setup
- Basic project structure

### 🚧 In Progress
- Category model implementation
- Product model implementation
- Authentication system

### 📋 Planned
- Cart system
- Order system
- Advanced features (filtering, pagination)

## Development Notes

- Built as a capstone project for backend development
- Focuses on RESTful API design and Django best practices
- Implements proper authentication and authorization
- Uses clean, modular architecture

## Author

Matan Workneh - Backend Development Capstone Project

## License

This project is for educational purposes as part of a backend development capstone.
