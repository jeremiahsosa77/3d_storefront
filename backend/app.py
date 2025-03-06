from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from config import Config

# Initialize extensions
db = SQLAlchemy()
migrate = Migrate()
jwt = JWTManager()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    
    # Initialize extensions with app
    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)
    CORS(app)
    
    # Register blueprints
    from routes.auth import auth_bp
    from routes.products import products_bp
    from routes.orders import orders_bp
    from routes.admin import admin_bp
    
    app.register_blueprint(auth_bp, url_prefix='/api/auth')
    app.register_blueprint(products_bp, url_prefix='/api/products')
    app.register_blueprint(orders_bp, url_prefix='/api/orders')
    app.register_blueprint(admin_bp, url_prefix='/api/admin')
    
    return app