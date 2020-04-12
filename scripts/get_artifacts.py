import json
import re
from typing import List

import httpx


def get_artifact_list(CircleCI_link: str, circle_token: str) -> List[dict]:
    """Get a list of the locations of all the build artifacts."""

    # Create request url
    url = (
        CircleCI_link[0:20]
        + "/api/v1.1/project/"
        + CircleCI_link[21::]
        + "/latest/artifacts"
    )

    # Request URL
    return httpx.get(url, params={"circle-token": circle_token}).json()
