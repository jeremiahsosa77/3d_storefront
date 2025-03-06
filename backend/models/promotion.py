# models/promotion.py
from datetime import datetime
from . import db

class Promotion(db.Model):
    __tablename__ = 'promotions'
    
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(50), unique=True, nullable=False)
    description = db.Column(db.Text)
    discount_percent = db.Column(db.Float)  # Percent off (0-100)
    discount_amount = db.Column(db.Float)   # Fixed amount off
    start_date = db.Column(db.DateTime, nullable=False)
    end_date = db.Column(db.DateTime, nullable=False)
    is_active = db.Column(db.Boolean, default=True)
    
    def to_dict(self):
        return {
            'id': self.id,
            'code': self.code,
            'description': self.description,
            'discount_percent': self.discount_percent,
            'discount_amount': self.discount_amount,
            'start_date': self.start_date.isoformat() if self.start_date else None,
            'end_date': self.end_date.isoformat() if self.end_date else None,
            'is_active': self.is_active
        }
    
    @property
    def is_valid(self):
        now = datetime.utcnow()
        return (
            self.is_active and 
            self.start_date <= now <= self.end_date
        )
    
    def apply_discount(self, subtotal):
        if not self.is_valid:
            return subtotal
        
        if self.discount_amount:
            return max(0, subtotal - self.discount_amount)
        
        if self.discount_percent:
            discount = subtotal * (self.discount_percent / 100)
            return subtotal - discount
        
        return subtotal