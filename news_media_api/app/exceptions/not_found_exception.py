from flask import Blueprint, request, jsonify
from app.services.article_service import ArticleService
from app.utils.exceptions.not_found_exception import NotFoundException
from app.utils.response import error_response

# Initialize blueprint for articles
article_controller = Blueprint('article_controller', __name__)

@article_controller.route('/<int:article_id>', methods=['GET'])
def get_article(article_id):
    """Retrieve a specific article by ID."""
    try:
        article = ArticleService.get_article_by_id(article_id)
        if not article:
            raise NotFoundException(message="Article not found")

        return jsonify(article), 200
    except NotFoundException as e:
        # Handle the exception and return a standardized error response
        return error_response(message=e.message, status_code=e.status_code)
    except Exception as e:
        # Catch all other exceptions
        return error_response(message=str(e), status_code=500)
