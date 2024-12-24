from flask import request, jsonify
from ..services.user_service import UserService
from ..utils.response import Response
from ..models.user import User

class UserController:
    @staticmethod
    def register_user():
        """Handle POST request to register a new user."""
        data = request.get_json()
        try:
            username = data.get('username')
            email = data.get('email')
            password = data.get('password')

            if not username or not email or not password:
                return Response.error("Missing required fields: username, email, or password", 400)

            # Create a new user using the UserService
            user = UserService.create_user(username, email, password)
            return Response.success("User registered successfully", {
                'id': user.id,
                'username': user.username,
                'email': user.email
            })
        except Exception as e:
            return Response.error(f"An error occurred: {str(e)}", 500)

    @staticmethod
    def get_user(user_id):
        """Handle GET request to retrieve user details by ID."""
        try:
            user = UserService.get_user_by_id(user_id)
            if user:
                return Response.success("User details retrieved successfully", {
                    'id': user.id,
                    'username': user.username,
                    'email': user.email
                })
            else:
                return Response.error("User not found", 404)
        except Exception as e:
            return Response.error(f"An error occurred: {str(e)}", 500)

    @staticmethod
    def update_user(user_id):
        """Handle PUT request to update user details."""
        data = request.get_json()
        try:
            username = data.get('username')
            email = data.get('email')
            password = data.get('password')

            if not username and not email and not password:
                return Response.error("No data provided to update", 400)

            user = UserService.update_user(user_id, username, email, password)
            if user:
                return Response.success("User updated successfully", {
                    'id': user.id,
                    'username': user.username,
                    'email': user.email
                })
            else:
                return Response.error("User not found", 404)
        except Exception as e:
            return Response.error(f"An error occurred: {str(e)}", 500)

    @staticmethod
    def delete_user(user_id):
        """Handle DELETE request to remove a user."""
        try:
            success = UserService.delete_user(user_id)
            if success:
                return Response.success("User deleted successfully")
            else:
                return Response.error("User not found", 404)
        except Exception as e:
            return Response.error(f"An error occurred: {str(e)}", 500)
