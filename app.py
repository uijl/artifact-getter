from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello, world!"

@app.route("/json")
def json():
    return jsonify(dict(message="Hello, world!"))

@app.route("/parameters")
def params():

    return request.args["arg1"] + request.args["arg2"]

if __name__ == "__main__":
    app.run(debug = True)