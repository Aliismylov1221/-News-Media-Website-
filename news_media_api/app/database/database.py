from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os

# Initialize the database object
db = SQLAlchemy()

# Initialize the migration object
migrate = Migrate()

def create_app():
    """Factory function to create the Flask application instance."""
    app = Flask(__name__)

    # Set up the database URI (you can replace with your own database URI)
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///site.db')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Disable modification tracking for performance
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'your-secret-key')  # Secret key for sessions

    # Initialize the database and migration tool
    db.init_app(app)
    migrate.init_app(app, db)

    # Register blueprints (if using blueprints)
    from app.controllers.article_controller import article_controller
    from app.controllers.user_controller import user_controller
    from app.controllers.category_controller import category_controller

    app.register_blueprint(article_controller)
    app.register_blueprint(user_controller)
    app.register_blueprint(category_controller)

    return app
