import pandas as pd
import ast
from flask import Flask
from flask_restful import Resource, Api, reqparse
import models
from database import engine, SessionLocal, Base

models.Base.metadata.create_all(bind=engine)

# Initialize api
if __name__ == "__main__":
    app = Flask(__name__)
    app.run(debug=True)
    api = Api(app)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
def test1():
    return {"message": "1"}


@app.get("/test123")
def test():
    return {"message": "Hello world"}
