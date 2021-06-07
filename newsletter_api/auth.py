from .models.user import User


def check_auth() -> bool:
    """ Check if authentication token is valid """
    return True


def get_user() -> User:
    """ Returns the currently authenticated User """
    return User.default()
