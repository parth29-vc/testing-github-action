"""
Add the validation messages releated to the authentication
"""


class ErrorMessage:
    # Error messages for authentication
    failed = 'These credentials do not match our records.'
    password = 'The provided password is incorrect.'
    throttle = 'Too many login attempts. Please try again in :seconds seconds.'
    inactive_account = "Please activate your account."


class InfoMessage:
    # Informative messages for authentication
    login_successfully = 'You are logged in successfully.'
