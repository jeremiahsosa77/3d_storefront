# models/__init__.py
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# Import models after db is defined to avoid circular imports
from .user import User
from .product import Product, Category
from .order import Order, OrderItem
from .cart import Cart, CartItem
from .promotion import Promotion