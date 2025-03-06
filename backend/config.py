# config.py - Configuration settings for Flask application
import os
from datetime import timedelta

class Config:
    # Flask settings
    SECRET_KEY = os.environ.get('SECRET_KEY', 'dev-secret-key')
    DEBUG = False
    TESTING = False
    
    # Database settings
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', 'postgresql://postgres:password@localhost:5432/nsynthic_db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    # JWT settings
    JWT_SECRET_KEY = os.environ.get('JWT_SECRET_KEY', 'jwt-secret-key')
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(hours=1)
    JWT_REFRESH_TOKEN_EXPIRES = timedelta(days=30)
    
    # Email settings
    MAIL_SERVER = os.environ.get('MAIL_SERVER', 'smtp.gmail.com')
    MAIL_PORT = int(os.environ.get('MAIL_PORT', 587))
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS', 'True').lower() in ['true', 'yes', '1']
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    MAIL_DEFAULT_SENDER = os.environ.get('MAIL_DEFAULT_SENDER', 'noreply@nsynthic.com')
    
    # File upload settings
    UPLOAD_FOLDER = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static/uploads')
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16MB max upload size

class DevelopmentConfig(Config):
    DEBUG = True
    
class TestingConfig(Config):
    TESTING = True
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'
    
class ProductionConfig(Config):
    DEBUG = False
    
    # Use stronger security settings in production
    SESSION_COOKIE_SECURE = True
    REMEMBER_COOKIE_SECURE = True
    SESSION_COOKIE_HTTPONLY = True
    REMEMBER_COOKIE_HTTPONLY = True
    
    # Make sure to set these environment variables in production
    SECRET_KEY = os.environ.get('SECRET_KEY')
    JWT_SECRET_KEY = os.environ.get('JWT_SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')

# Map environment names to config objects
config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}