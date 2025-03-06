# models/user.py
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from . import db

class User(db.Model):
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password_hash = db.Column(db.String(200), nullable=False)
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    is_admin = db.Column(db.Boolean, default=False)
    loyalty_points = db.Column(db.Integer, default=0)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    # Relationships
    orders = db.relationship('Order', backref='user', lazy=True)
    addresses = db.relationship('Address', backref='user', lazy=True)
    cart = db.relationship('Cart', backref='user', lazy=True, uselist=False)
    
    def __init__(self, email, first_name=None, last_name=None, password=None):
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        if password:
            self.set_password(password)
    
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
    
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    
    def to_dict(self):
        return {
            'id': self.id,
            'email': self.email,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'is_admin': self.is_admin,
            'loyalty_points': self.loyalty_points,
            'created_at': self.created_at.isoformat() if self.created_at else None
        }

class Address(db.Model):
    __tablename__ = 'addresses'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    address_line1 = db.Column(db.String(100), nullable=False)
    address_line2 = db.Column(db.String(100))
    city = db.Column(db.String(50), nullable=False)
    state = db.Column(db.String(50), nullable=False)
    postal_code = db.Column(db.String(20), nullable=False)
    country = db.Column(db.String(50), nullable=False)
    is_default = db.Column(db.Boolean, default=False)
    
    def to_dict(self):
        return {
            'id': self.id,
            'address_line1': self.address_line1,
            'address_line2': self.address_line2,
            'city': self.city,
            'state': self.state,
            'postal_code': self.postal_code,
            'country': self.country,
            'is_default': self.is_default
        }