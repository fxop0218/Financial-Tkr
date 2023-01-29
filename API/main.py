import pandas as pd
from dotenv import load_dotenv
from flask_migrate import Migrate
from flask import (
    Flask,
    render_template,
    request,
    redirect,
    url_for,
    jsonify,
    make_response,
)
from models import users, expenses
from database import db

app = Flask(__name__)

# DB configuration

USER_DB = "postgres"
PASS_DB = "admin"
URL_DB = "localhost"
NAME_DB = "financial"
FULL_URL_DB = f"postgresql://{USER_DB}:{PASS_DB}@{URL_DB}/{NAME_DB}"

app.config["SQLALCHEMY_DATABASE_URI"] = FULL_URL_DB
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# If separate the classes in other files need this
db.init_app(app)

# Configurate flask-migrate

migrate = Migrate()
migrate.init_app(app, db)

# Configuration of flask-wtf
app.config["SECRET_KEY"] = "SECRET_KEY"  # Change in production service


@app.route("/test", methods=["GET"])
def info():
    if request.method == "GET":
        data = {"Message": "test"}
    return jsonify(data)


if __name__ == "__main__":
    load_dotenv()
    app.run(debug=True, port=5000, host="0.0.0.0")
