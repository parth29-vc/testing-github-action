"""
Register the routes of APIs
"""
from app.api.domains.ml.v1.views import classification


def initialize_urls(api):
    """
    Create the enpoints for the Rest APIs.
    """
    api.add_resource(classification.ImageClassification, '/classify', endpoint="image_classification")

