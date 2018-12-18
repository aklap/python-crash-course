import json
import constant


def get_stored_username():
    """Get the username if it is available."""
    try:
        with open(constant.FILENAME) as f:
            username = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return username


def get_new_username():
    """Get name from user."""
    username = input('What is your name?\n')

    with open(constant.FILENAME, 'w') as f:
        json.dump(username, f)

    return username


def check_username(username):
    """Check name of user, return boolean val."""
    is_name = input('Is ' + username + ' your username, (y/n)?\n')

    return is_name.lower() == 'y'


def greet_user():
    """Greet user by name."""
    username = get_stored_username()

    if username and check_username(username):
        return 'Welcome back, ' + username + '!'
    else:
        username = get_new_username()
        return 'We\'ll remember you when you come back ' + username + '!'

print(greet_user())
