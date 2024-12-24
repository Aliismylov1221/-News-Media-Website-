from flask import Flask
from app.controllers.article_controller import article_controller
from app.controllers.user_controller import user_controller
from app.controllers.category_controller import category_controller

def register_api_routes(app):
    """
    Registers all API routes to the Flask app by attaching blueprints.
    This function ensures that all the API controllers (articles, users, categories) are mapped correctly.
    """
    # Register routes for articles (with prefix '/api/articles')
    app.register_blueprint(article_controller, url_prefix='/api/articles')

    # Register routes for users (with prefix '/api/users')
    app.register_blueprint(user_controller, url_prefix='/api/users')

    # Register routes for categories (with prefix '/api/categories')
    app.register_blueprint(category_controller, url_prefix='/api/categories')

