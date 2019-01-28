from user import User


class Admin(User):
    """Base class for Admin."""
    def __init__(self):
        """Initialize instance of Admin."""
        self.privileges = Privileges()


class Privileges:
    """Base class for privileges."""
    def __init__(self):
        """Initialize instance of Privilege."""
        self.privileges = [
            'can add post',
            'can delete post',
            'can ban user',
        ]

    def show_privileges(self):
        """Show Admin privileges."""
        for privilege in self.privileges:
            print(privilege)
