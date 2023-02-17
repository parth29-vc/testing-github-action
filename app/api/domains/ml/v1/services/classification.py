""" It has a logic of User's CRUD functionality.
"""
import os
import pathlib
from app.constants import constant
from app.helpers.cores.standard_response import Response
from app.messages.en.validation import ErrorMessage, InfoMessage
from app.ml_backend.inference import run_inference


class BaseService:
    def __init__(self):
        pass

class ImageClassificationService(BaseService):
    def __init__(self):
        pass

    def classify_image(self, data: dict):
        """This function is used to create the user or
            for the registration process.

        Args:
            data (dict): It has the user's data.

        """
        try:
            output = run_inference(data['image_path'])

            response = Response(InfoMessage.status_success,
                                output,
                                InfoMessage.classification_success).make, \
                                constant.STATUS_CODE_200
            try:
                path = pathlib.Path(data['image_path'])
                # path.unlink()  # For removing image after inference
                
            except OSError as err:
                print("Error: %s - %s." % (err.filename, err.strerror))
        except:
            response = Response(ErrorMessage.status_error,
                                constant.STATUS_NULL,
                                ErrorMessage.classification_error).make, \
                                constant.STATUS_CODE_500

        return response