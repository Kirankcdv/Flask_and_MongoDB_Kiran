
import json
import os
from pathlib import Path

from dotenv import load_dotenv
from flask import Flask, render_template, request, redirect, url_for, jsonify
from pymongo import MongoClient
from pymongo.errors import PyMongoError

BASE_DIR = Path(__file__).resolve().parent
load_dotenv(BASE_DIR / ".env")

app = Flask(__name__)

MONGO_URI = os.getenv("MONGO_URI", "").strip()


def get_collection():
    """Connect to MongoDB when needed."""
    if not MONGO_URI:
        raise RuntimeError("MONGO_URI is missing from the .env file.")

    client = MongoClient(MONGO_URI, serverSelectionTimeoutMS=10000)
    client.admin.command("ping")
    return client, client["flask_assignment"]["submissions"]


@app.route("/api", methods=["GET"])
def api():
    try:
        with (BASE_DIR / "data.json").open("r", encoding="utf-8") as file:
            data = json.load(file)
        return jsonify(data), 200
    except (OSError, json.JSONDecodeError):
        app.logger.exception("Unable to read data.json")
        return jsonify({"error": "Unable to read API data"}), 500


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        return render_template("index.html", error=None)

    name = request.form.get("name", "").strip()
    email = request.form.get("email", "").strip()
    message = request.form.get("message", "").strip()

    if not name or not email or not message:
        return render_template(
            "index.html", error="Please fill in all fields."
        ), 400

    client = None
    try:
        client, collection = get_collection()
        collection.insert_one({
            "name": name,
            "email": email,
            "message": message
        })
        return redirect(url_for("success"), code=303)

    except (PyMongoError, RuntimeError) as error:
        app.logger.error(
            "MongoDB submission failed: %s: %s",
            type(error).__name__, error
        )
        return render_template(
            "index.html",
            error=f"Database submission failed ({type(error).__name__}). "
                  "Check the VS Code terminal for details."
        ), 500

    finally:
        if client is not None:
            client.close()


@app.route("/success", methods=["GET"])
def success():
    return render_template("success.html")


if __name__ == "__main__":
    app.run(debug=True)
