import json
from typing import List

import httpx


def get_all(CircleCI_link: str, circle_token: str = None) -> List[dict]:
    """Get a list of the locations of all the build artifacts."""

    # Check if the link ends witha forward slash and remove it
    if CircleCI_link[-1] == "/":
        CircleCI_link = CircleCI_link[:-1]

    # Remove basic string
    if "https" in CircleCI_link:
        CircleCI_link = CircleCI_link.replace("https://circleci.com/", "")
    elif "http" in CircleCI_link:
        CircleCI_link = CircleCI_link.replace("http://circleci.com/", "")

    # Create request url
    url = "https://circleci.com/api/v1.1/project/" + CircleCI_link + "/latest/artifacts"

    # Check if token is provided and request url
    if circle_token:
        return httpx.get(url, params={"circle-token": circle_token}).json()

    # Else try to fetch the package information
    else:
        request = httpx.get(url).json()
        if request == {"message": "Project not found"}:
            return json.dumps(
                {
                    "error": "Project cannot be reached because no circle_token is provided"
                }
            )
        else:
            return request