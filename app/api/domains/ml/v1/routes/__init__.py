# Register the API routes
from app.api.domains.ml.v1.routes import classification

def get_routes(api):
    """
    Include all the routes from different routes file.
    """
    classification.initialize_urls(api)