from app.models.category import Category

class CategoryService:
    @staticmethod
    def get_all_categories():
        """Retrieve all categories."""
        categories = Category.get_all_categories()
        return [Category.to_dict(category) for category in categories]

    @staticmethod
    def get_category_by_id(category_id):
        """Retrieve a single category by its ID."""
        category = Category.get_category_by_id(category_id)
        if category:
            return Category.to_dict(category)
        return None

    @staticmethod
    def create_category(name):
        """Create a new category."""
        category = Category.create_category(name)
        return Category.to_dict(category), 201

    @staticmethod
    def update_category(category_id, name):
        """Update an existing category."""
        category = Category.update_category(category_id, name)
        if category:
            return Category.to_dict(category)
        return {"error": "Category not found"}, 404

    @staticmethod
    def delete_category(category_id):
        """Delete a category."""
        result = Category.delete_category(category_id)
        if result:
            return {"message": "Category deleted successfully"}
        return {"error": "Category not found"}, 404
