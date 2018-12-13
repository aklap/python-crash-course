# class User:
#     """Base class for User."""
#     def __init__(self, name, age, location, login_attempts):
#         """Initialize instance of User."""
#         self.name = name
#         self.age = age
#         self.location = location
#         self.login_attempts = login_attempts

#     def describe_user(self):
#         """Print each attribute of the User instance."""
#         print('User summary:\n' + self.name.title() + ' ' + str(self.age) + ' ' + self.location.title())

#     def greet_user(self):
#         """Greet user."""
#         print('Hello, ' + self.name + '!\n')

#     def increment_login_attempts(self):
#         """Increment login_attempts attribute."""
#         self.login_attempts += 1

#     def reset_login_attempts(self):
#         """Resets login_attempts to 0."""
#         self.login_attempts = 0
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
            'can ban user'
        ]

    def show_privileges(self):
        """Show Admin privileges."""
        for privilege in self.privileges:
            print(privilege)