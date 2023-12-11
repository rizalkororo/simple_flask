
import os
from flask import Flask, jsonify, make_response
from dotenv import load_dotenv

# load .env variables
load_dotenv()

app = Flask(__name__)


@app.route("/")
def home():
    return "<p>Index page</p>"


@app.route("/users")
def users():
    all_users = [
        {
            "name": "Ali",
            "age": 20,
            "email": "aliakbar@gmail.com"
        },
        {
            "name": "Ikram",
            "age": 18,
            "email": "ikram@gmail.com"
        },
        {
            "name": "Umar",
            "age": 45,
            "email": "umarmachtub@gmail.com"
        }
    ]
    return make_response(jsonify({"users": all_users}))


if __name__ == "__main__":
    app.run(debug=os.environ.get("DEBUG"), host=os.environ.get(
        "HOST"), port=os.environ.get('PORT'))
