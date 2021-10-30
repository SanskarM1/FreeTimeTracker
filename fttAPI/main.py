#Flask helps build API - allows website to access database
from flask import Flask
app = Flask(__name__)

@app.route("/",methods = ["GET"])
def hello_world():
    return "bye World"

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80)