"""
The function of this file is to tell the Python interpreter that
this directory is a package and involvement of this __init.py_ file in
it makes it a python project.
"""
from flask import Flask, Blueprint
# from flask_migrate import Migrate
from flask_restful import Api
# from flask_sqlalchemy import SQLAlchemy
# from flask_jwt_extended import JWTManager
from app.constants import constant


# db = SQLAlchemy()
# migrate = Migrate()


def create_app(env=None):
    # from config.database import config_by_name
    # from config.auth import AuthConfig

    app = Flask(__name__)

    """
    Create the Blueprint instance for the API versions.
    create instance of blueprint - 
        api_bp = Blueprint('api', __name__)
        api = Api(api_bp)
        
        # Create endpoint of Rest API
        api.add_resource(UserCreate, '/users', endpoint="")
        app.register_blueprint(api_bp, url_prefix = '/api/v1')

    """
    api_bp_v1 = Blueprint('api1', __name__)
    api_v1 = Api(api_bp_v1)

    # app.config.from_object(AuthConfig())
    # JWTManager(app)

    # app.config.from_object(env or "test")
    # db.init_app(app)
    # migrate.init_app(app, db)

    """
    Register the model files to migrate the database.
    """
    # from app.api.domains.ml.v1.models.user import user

    """
    Register the blueprints which we have created.
    e.g.- 
        app.register_blueprint(api_bp_v1, url_prefix = '/api/v1')
        app.register_blueprint(api_bp_v2, url_prefix = '/api/v2')
    
    """
    from app.api.domains.ml.v1.routes import get_routes
    get_routes(api_v1)
    app.register_blueprint(api_bp_v1, url_prefix = constant.url_prefix_version1)

    return app
