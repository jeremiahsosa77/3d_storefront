# models/order.py
from datetime import datetime
from . import db

class Order(db.Model):
    __tablename__ = 'orders'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    status = db.Column(db.String(20), default='pending')  # pending, processing, shipped, delivered, cancelled
    total = db.Column(db.Float, nullable=False)
    shipping_address_id = db.Column(db.Integer, db.ForeignKey('addresses.id'))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    # Relationships
    order_items = db.relationship('OrderItem', backref='order', lazy=True, cascade='all, delete-orphan')
    shipping_address = db.relationship('Address')
    
    def to_dict(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'status': self.status,
            'total': self.total,
            'created_at': self.created_at.isoformat() if self.created_at else None,
            'items': [item.to_dict() for item in self.order_items]
        }

class OrderItem(db.Model):
    __tablename__ = 'order_items'
    
    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey('orders.id'), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'), nullable=False)
    quantity = db.Column(db.Integer, default=1)
    price = db.Column(db.Float, nullable=False)  # Price at time of purchase
    
    def to_dict(self):
        return {
            'id': self.id,
            'product_id': self.product_id,
            'product_name': self.product.name if self.product else None,
            'quantity': self.quantity,
            'price': self.price,
            'subtotal': self.price * self.quantity
        }