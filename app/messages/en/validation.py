"""
Note: Add the Error messages releated to the common validation.
"""


class ErrorMessage:
    # Error messages for validations.
    status_error = "Error"
    fail = "Fail!"
    classification_error = "Something went wrong into database."
    username = "Please provide the username."
    email = "Please provide the email address."
    password = "Please provide the password."
    not_be_null = "Must not be Null value."
    invalid_email = "Please provide a valid email address."
    email_exist = "This email ID already exist."
    email_or_username_exist = 'User already exists with same ' \
        'email ID or username.'
    user_not_exist = 'We can not find a user with that id.'
    must_be_alphabates = 'It must be have alphabates.'


class InfoMessage:
    # Informative messages for validations.
    status_success = 'Success'
    classification_success = 'Image has been successfully classified'
    
