from typing import Tuple, Union

from flask import request
from werkzeug.exceptions import BadRequest


def get_params(parameters: request.args) -> Tuple[str, Union[str, None]]:
    """Get parameters from the request string."""

    try:
        circle_url = parameters["circle_url"]
    except KeyError:
        raise BadRequest("Error, parameter circle_url was not found.")

    try:
        circle_token = parameters["circle_token"]
        return circle_url, circle_token
    except KeyError:
        return circle_url, None
