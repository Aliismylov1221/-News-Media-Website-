import os

class Config:
    """Base config class."""
    SECRET_KEY = os.getenv('SECRET_KEY', 'your-secret-key-here')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevelopmentConfig(Config):
    """Development specific configurations."""
    SQLALCHEMY_DATABASE_URI = os.getenv('DEV_DATABASE_URL', 'sqlite:///dev.db')

class TestingConfig(Config):
    """Testing specific configurations."""
    SQLALCHEMY_DATABASE_URI = os.getenv('TEST_DATABASE_URL', 'sqlite:///test.db')
    TESTING = True

class ProductionConfig(Config):
    """Production specific configurations."""
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'sqlite:///prod.db')
    DEBUG = False
