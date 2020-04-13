from flask import Flask, jsonify, request
from artifact_getter.scripts import get_artifacts

app = Flask(__name__)

@app.route("/")
def main():
    return jsonify(dict(message="Basic server"))


@app.route("/get_all_artifacts", methods=["GET"])
def get_all_artifacts():

    try:
        circle_url = request.args["circle_url"]
        circle_token = request.args["circle_token"]

        return jsonify(get_artifacts.get_all(circle_url, circle_token))
    
    except KeyError:
        return jsonify({"error": "Pass the parameters 'circle_url' and 'circle_token'"})


# EXAMPLE REQUEST
# http://localhost:5000/get_coverage_report?circle_url=https://circleci.com/gh/uijl/wtdpy&circle_token=4
# http://localhost:5000/get_coverage_report?circle_url=https://circleci.com/gh/uijl/wtdpy&circle_token=4&output=str

@app.route("/get_coverage_report", methods=["GET"])
def get_coverage_report():

    try:
        circle_url = request.args["circle_url"]
        circle_token = request.args["circle_token"]
    
    except KeyError:
        return jsonify({"error": "Pass the parameters 'circle_url' and 'circle_token'"})

    if "output" in request.args:
        output = request.args["output"]
    else:
        output = "str"

    response = get_artifacts.get_all(circle_url, circle_token)

    for item in response:
        if "tmp/artifacts/index.html" in item["path"]:
            if output == "str":
                return item["url"]
            elif output == "json":
                return jsonify({"coverage_report": item["url"]})



@app.route("/get_coverage_badge", methods=["GET"])
def get_coverage_badge():

    try:
        circle_url = request.args["circle_url"]
        circle_token = request.args["circle_token"]
    
    except KeyError:
        return jsonify({"error": "Pass the parameters 'circle_url' and 'circle_token'"})

    if "output" in request.args:
        output = request.args["output"]
    else:
        output = "str"

    response = get_artifacts.get_all(circle_url, circle_token)

    for item in response:
        if "tmp/artifacts/coverage.svg" in item["path"]:
            if output == "str":
                return item["url"]
            elif output == "json":
                return jsonify({"coverage_report": item["url"]})
