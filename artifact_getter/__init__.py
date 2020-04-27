from flask import Flask, jsonify, request, redirect
from artifact_getter.scripts import get_artifacts, get_params

app = Flask(__name__)


@app.route("/")
def main() -> None:
    return jsonify(dict(message="Basic server"))


@app.route("/get_all_artifacts", methods=["GET"])
def get_all_artifacts() -> list:
    """Return a json with all CircleCI build artifacts."""

    circle_url, circle_token = get_params.get_params(request.args)

    if circle_token:
        return jsonify(get_artifacts.get_all(circle_url, circle_token))
    else:
        return jsonify(get_artifacts.get_all(circle_url))


@app.route("/get_coverage_report", methods=["GET"])
def get_coverage_report() -> None:
    """Redirect to the coverage report."""

    circle_url, circle_token = get_params.get_params(request.args)

    if circle_token:
        response = get_artifacts.get_all(circle_url, circle_token)
    else:
        response = get_artifacts.get_all(circle_url)

    # Check if the location of the report is passed
    try:
        coverage_location = request.args["coverage_location"]
    except KeyError:
        coverage_location = None

    # Check if name of the report is passed
    try:
        coverage_name = request.args["coverage_name"]
    except KeyError:
        coverage_name = None

    for item in response:
        if coverage_location and coverage_name:
            if coverage_location in item["path"] and coverage_name in item["path"]:
                return redirect(item["url"])
        elif coverage_location:
            if coverage_location in item["path"] and "index.html" in item["path"]:
                return redirect(item["url"])
        elif coverage_name:
            if coverage_name in item["path"]:
                return redirect(item["url"])
        else:
            if "tmp/artifacts/index.html" in item["path"]:
                return redirect(item["url"])


@app.route("/get_coverage_badge", methods=["GET"])
def get_coverage_badge() -> None:
    """Redirect to the coverage badge"""

    circle_url, circle_token = get_params.get_params(request.args)

    if circle_token:
        response = get_artifacts.get_all(circle_url, circle_token)
    else:
        response = get_artifacts.get_all(circle_url)

    # Check if the location of the report is passed
    try:
        badge_location = request.args["badge_location"]
    except KeyError:
        badge_location = None

    # Check if name of the report is passed
    try:
        badge_name = request.args["badge_name"]
    except KeyError:
        badge_name = None

    for item in response:
        if badge_location and badge_name:
            if badge_location in item["path"] and badge_name in item["path"]:
                return redirect(item["url"])
        elif badge_location:
            if badge_location in item["path"] and "coverage.svg" in item["path"]:
                return redirect(item["url"])
        elif badge_name:
            if badge_name in item["path"]:
                return redirect(item["url"])
        else:
            if "tmp/artifacts/coverage.svg" in item["path"]:
                return redirect(item["url"])
