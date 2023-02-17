from marshmallow import fields, Schema
from app.api.domains.ml.v1.schemas import must_not_be_blank

    
class ImageClassificationSchema(Schema):
    """
    This is the schema for the create user to serialize and Deserialize
    the data.
    """
    image_path = fields.Str(required=True, validate=must_not_be_blank)
