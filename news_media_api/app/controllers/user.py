from ..database.database import db

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(100), nullable=False, unique=True)
    email = db.Column(db.String(120), nullable=False, unique=True)
    password = db.Column(db.String(200), nullable=False)

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password

    def __repr__(self):
        return f'<User {self.username}>'

    @staticmethod
    def to_dict(user):
        """Convert the User object to a dictionary."""
        return {
            'id': user.id,
            'username': user.username,
            'email': user.email
        }

    @staticmethod
    def get_user_by_id(user_id):
        """Get a user by their ID."""
        return User.query.get(user_id)

    @staticmethod
    def create_user(username, email, password):
        """Create a new user."""
        user = User(username=username, email=email, password=password)
        db.session.add(user)
        db.session.commit()
        return user

    @staticmethod
    def update_user(user_id, username=None, email=None, password=None):
        """Update user details."""
        user = User.query.get(user_id)
        if user:
            if username:
                user.username = username
            if email:
                user.email = email
            if password:
                user.password = password
            db.session.commit()
            return user
        return None

    @staticmethod
    def delete_user(user_id):
        """Delete a user."""
        user = User.query.get(user_id)
        if user:
            db.session.delete(user)
            db.session.commit()
            return True
        return False
