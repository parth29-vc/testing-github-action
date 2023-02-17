from marshmallow import ValidationError
from app.messages.en.validation import ErrorMessage

# Custom validator
def must_not_be_blank(data):
    if not data:
        raise ValidationError(ErrorMessage.not_be_null)
