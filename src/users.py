"""User classes and factory for the document management system."""


class User:
    """
    Base class shared by all user types.
    """

    def __init__(self, name):
        self.name = name

    def get_role(self):
        """
        Return the user's role.
        """
        return self.__class__.__name__

    def __str__(self):
        """
        Return a readable description of the user."""
        return f"{self.name} ({self.get_role()})"


class Admin(User):
    """
    Represents an administrator.
    """
    pass


class Editor(User):
    """
    Represents a user who can edit documents."""
    pass


class Viewer(User):
    """
    Represents a user who can view documents.
    """
    pass


def create_user(type, name):
    """
    Create and return a user based on their role.
    """

    user_types = {
        "admin": Admin,
        "editor": Editor,
        "viewer": Viewer,
    }

    role = type.strip().lower()

    if role not in user_types:
        raise ValueError(f"Unknown user type: {type}")

    if not name or not name.strip():
        raise ValueError("User name cannot be empty")

    return user_types[role](name.strip())