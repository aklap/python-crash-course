class User:
    """Base class for User."""
    def __init__(self, name, age, location, login_attempts):
        """Initialize instance of User."""
        self.name = name
        self.age = age
        self.location = location
        self.login_attempts = login_attempts

    def describe_user(self):
        """Print each attribute of the User instance."""
        msg = 'User summary:\n'
        msg += self.name.title() + ' '
        msg += str(self.age) + ' '
        msg += self.location.title()
        print(msg)

    def greet_user(self):
        """Greet user."""
        print('Hello, ' + self.name + '!\n')

    def increment_login_attempts(self):
        """Increment login_attempts attribute."""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """Resets login_attempts to 0."""
        self.login_attempts = 0
