import json
from typing import List

import httpx


def get_all(CircleCI_link: str, circle_token: str) -> List[dict]:
    """Get a list of the locations of all the build artifacts."""

    if CircleCI_link[-1] == "/":
        CircleCI_link = CircleCI_link[:-1]

    # Create request url
    url = (
        CircleCI_link[0:20]
        + "/api/v1.1/project/"
        + CircleCI_link[21::]
        + "/latest/artifacts"
    )

    # Request URL
    return httpx.get(url, params={"circle-token": circle_token}).json()
