from flask import request, jsonify
from ..services.article_service import ArticleService
from ..models.article import Article
from ..utils.response import Response

class ArticleController:
    @staticmethod
    def get_articles():
        """Handle GET request to fetch all articles."""
        try:
            articles = ArticleService.get_all_articles()
            if articles:
                return Response.success("Articles retrieved successfully", 
                                         [{'id': article.id, 'title': article.title} for article in articles])
            else:
                return Response.error("No articles found", 404)
        except Exception as e:
            return Response.error(f"An error occurred: {str(e)}")

    @staticmethod
    def get_article(article_id):
        """Handle GET request to fetch a single article by ID."""
        try:
            article = ArticleService.get_article_by_id(article_id)
            if article:
                return Response.success("Article retrieved successfully", {
                    'id': article.id,
                    'title': article.title,
                    'content': article.content,
                    'category': article.category.name  # Assuming the category relationship exists
                })
            else:
                return Response.error("Article not found", 404)
        except Exception as e:
            return Response.error(f"An error occurred: {str(e)}")

    @staticmethod
    def create_article():
        """Handle POST request to create a new article."""
        data = request.get_json()
        try:
            title = data.get('title')
            content = data.get('content')
            category_id = data.get('category_id')

            if not title or not content or not category_id:
                return Response.error("Missing required fields: title, content, or category_id", 400)

            # Call the service to create the article
            article = ArticleService.create_article(title, content, category_id)

            return Response.success("Article created successfully", {
                'id': article.id,
                'title': article.title
            })
        except Exception as e:
            return Response.error(f"An error occurred: {str(e)}", 500)

    @staticmethod
    def update_article(article_id):
        """Handle PUT request to update an existing article."""
        data = request.get_json()
        try:
            title = data.get('title')
            content = data.get('content')
            category_id = data.get('category_id')

            # Validate the data
            if not title or not content or not category_id:
                return Response.error("Missing required fields: title, content, or category_id", 400)

            # Update the article
            article = ArticleService.update_article(article_id, title, content, category_id)
            if article:
                return Response.success("Article updated successfully", {
                    'id': article.id,
                    'title': article.title
                })
            else:
                return Response.error("Article not found", 404)

        except Exception as e:
            return Response.error(f"An error occurred: {str(e)}", 500)

    @staticmethod
    def delete_article(article_id):
        """Handle DELETE request to remove an article."""
        try:
            success = ArticleService.delete_article(article_id)
            if success:
                return Response.success("Article deleted successfully")
            else:
                return Response.error("Article not found", 404)
        except Exception as e:
            return Response.error(f"An error occurred: {str(e)}", 500)
