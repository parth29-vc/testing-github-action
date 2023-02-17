""" These views are Python functions that takes http requests and returns http response.
"""
from flask import request
from flask_restful import Resource
from app.constants import constant
from marshmallow import ValidationError
from app.api.domains.ml.v1.services.classification import ImageClassificationService
from app.helpers.cores.standard_response import Response
from app.api.domains.ml.v1.schemas.classification import ImageClassificationSchema
from app.messages.en.validation import ErrorMessage


class ImageClassification(Resource):
    """ This class provides the methods of API request.
    """

    def post(self):
        """ This function is used to create the user into the database.
        """
        # Validate the request data
        req_data = request.get_json()

        try:
            data = ImageClassificationSchema().load(req_data)

        except ValidationError as err:
            response = Response(ErrorMessage.status_error,
                                constant.STATUS_NULL,
                                err.messages).make
            return response, constant.STATUS_CODE_422

        # Call the service to create the user
        response, status = ImageClassificationService().classify_image(data)

        return response, status
