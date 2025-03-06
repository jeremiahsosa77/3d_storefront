# models/cart.py
from datetime import datetime
from . import db

class Cart(db.Model):
    __tablename__ = 'carts'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    # Relationships
    cart_items = db.relationship('CartItem', backref='cart', lazy=True, cascade='all, delete-orphan')
    
    def to_dict(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'created_at': self.created_at.isoformat() if self.created_at else None,
            'items': [item.to_dict() for item in self.cart_items]
        }
    
    @property
    def total(self):
        return sum(item.subtotal for item in self.cart_items)

class CartItem(db.Model):
    __tablename__ = 'cart_items'
    
    id = db.Column(db.Integer, primary_key=True)
    cart_id = db.Column(db.Integer, db.ForeignKey('carts.id'), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'), nullable=False)
    quantity = db.Column(db.Integer, default=1)
    added_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    def to_dict(self):
        return {
            'id': self.id,
            'product_id': self.product_id,
            'product': self.product.to_dict() if self.product else None,
            'quantity': self.quantity,
            'added_at': self.added_at.isoformat() if self.added_at else None,
            'subtotal': self.subtotal
        }
    
    @property
    def subtotal(self):
        if not self.product:
            return 0
        return self.product.price * self.quantity