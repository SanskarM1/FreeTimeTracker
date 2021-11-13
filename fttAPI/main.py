# Flask helps build API - allows website to access database
from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/", methods=["GET"])
def hello_world():
    return "bye World"


@app.route("/query", methods=["GET"])
def query():
    number = request.args.get("number")
    return number + "1"


@app.route("/somethining", methods=["GET"])
def somethining():
    body = request.json
    if body is None:
        return "No json provided"
    number = body.get("num", 0)
    text = body.get("text", "no text provided")
    value = {
        "newtext": text + text,
        "newnumber": number + 5
    }
    return jsonify(value)

@app.route("/createuser", methods=["POST"])
def post():
    body = request.json
    if body is None:
        return "Error: NO USER PROVIDED"
    user = body.get("username", None)
    password = body.get("password", None)

    if user is None or password is None:
        return "Error: INCOMPLETE CREDENTIALS"

    #TODO Create user in database

    return "SUCCESS: USER CREATED"



if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80)
