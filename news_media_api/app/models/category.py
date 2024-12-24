from ..database.database import db

class Category(db.Model):
    __tablename__ = 'categories'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False, unique=True)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f'<Category {self.name}>'

    @staticmethod
    def to_dict(category):
        """Convert the Category object to a dictionary."""
        return {
            'id': category.id,
            'name': category.name
        }

    @staticmethod
    def get_category_by_id(category_id):
        """Get a category by its ID."""
        return Category.query.get(category_id)

    @staticmethod
    def get_all_categories():
        """Get all categories."""
        return Category.query.all()

    @staticmethod
    def create_category(name):
        """Create a new category."""
        category = Category(name=name)
        db.session.add(category)
        db.session.commit()
        return category

    @staticmethod
    def update_category(category_id, name):
        """Update an existing category."""
        category = Category.query.get(category_id)
        if category:
            category.name = name
            db.session.commit()
            return category
        return None

    @staticmethod
    def delete_category(category_id):
        """Delete a category."""
        category = Category.query.get(category_id)
        if category:
            db.session.delete(category)
            db.session.commit()
            return True
        return False
