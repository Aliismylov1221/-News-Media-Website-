from app.models.user import User

class UserService:
    @staticmethod
    def get_user_by_id(user_id):
        """Retrieve a user by ID."""
        user = User.get_user_by_id(user_id)
        if user:
            return User.to_dict(user)
        return None

    @staticmethod
    def create_user(username, email, password):
        """Create a new user."""
        # Add password hashing here if needed, such as with werkzeug.security
        user = User.create_user(username, email, password)
        return User.to_dict(user), 201

    @staticmethod
    def update_user(user_id, username=None, email=None, password=None):
        """Update a user's details."""
        user = User.update_user(user_id, username, email, password)
        if user:
            return User.to_dict(user)
        return {"error": "User not found"}, 404

    @staticmethod
    def delete_user(user_id):
        """Delete a user."""
        result = User.delete_user(user_id)
        if result:
            return {"message": "User deleted successfully"}
        return {"error": "User not found"}, 404
