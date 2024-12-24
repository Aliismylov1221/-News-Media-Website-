from datetime import datetime
from ..database.database import db

class Article(db.Model):
    __tablename__ = 'articles'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(255), nullable=False)
    content = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, onupdate=datetime.utcnow)
    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    # Define relationships
    category = db.relationship('Category', backref='articles', lazy=True)
    user = db.relationship('User', backref='articles', lazy=True)

    def __init__(self, title, content, category_id, user_id):
        self.title = title
        self.content = content
        self.category_id = category_id
        self.user_id = user_id

    def __repr__(self):
        return f'<Article {self.title}>'

    @staticmethod
    def to_dict(article):
        """Convert the Article object to a dictionary."""
        return {
            'id': article.id,
            'title': article.title,
            'content': article.content,
            'created_at': article.created_at,
            'updated_at': article.updated_at,
            'category_id': article.category_id,
            'user_id': article.user_id
        }

    @staticmethod
    def get_article_by_id(article_id):
        """Get an article by its ID."""
        return Article.query.get(article_id)

    @staticmethod
    def get_all_articles():
        """Get all articles."""
        return Article.query.all()

    @staticmethod
    def create_article(title, content, category_id, user_id):
        """Create a new article."""
        article = Article(title=title, content=content, category_id=category_id, user_id=user_id)
        db.session.add(article)
        db.session.commit()
        return article

    @staticmethod
    def update_article(article_id, title, content, category_id):
        """Update an existing article."""
        article = Article.query.get(article_id)
        if article:
            article.title = title
            article.content = content
            article.category_id = category_id
            db.session.commit()
            return article
        return None

    @staticmethod
    def delete_article(article_id):
        """Delete an article."""
        article = Article.query.get(article_id)
        if article:
            db.session.delete(article)
            db.session.commit()
            return True
        return False
