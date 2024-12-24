from app.models.article import Article
from app.models.category import Category
from app.models.user import User

class ArticleService:
    @staticmethod
    def get_all_articles():
        """Retrieve all articles."""
        articles = Article.get_all_articles()
        return [Article.to_dict(article) for article in articles]

    @staticmethod
    def get_article_by_id(article_id):
        """Retrieve a single article by its ID."""
        article = Article.get_article_by_id(article_id)
        if article:
            return Article.to_dict(article)
        return None

    @staticmethod
    def create_article(title, content, category_id, user_id):
        """Create a new article."""
        category = Category.query.get(category_id)
        user = User.query.get(user_id)

        if not category:
            return {"error": "Category not found"}, 404
        if not user:
            return {"error": "User not found"}, 404

        article = Article.create_article(title, content, category_id, user_id)
        return Article.to_dict(article), 201

    @staticmethod
    def update_article(article_id, title, content, category_id):
        """Update an existing article."""
        category = Category.query.get(category_id)
        if not category:
            return {"error": "Category not found"}, 404

        article = Article.update_article(article_id, title, content, category_id)
        if article:
            return Article.to_dict(article)
        return {"error": "Article not found"}, 404

    @staticmethod
    def delete_article(article_id):
        """Delete an article."""
        result = Article.delete_article(article_id)
        if result:
            return {"message": "Article deleted successfully"}
        return {"error": "Article not found"}, 404
