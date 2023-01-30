import os
import sys
import psycopg2
import importlib.util
from psycopg2 import OperationalError

spec = importlib.util.spec_from_file_location("databse", "API/database.py")
foo = importlib.util.module_from_spec(spec)
spec.loader.exec_module(foo)

USER_DB = "postgres"
PASS_DB = "admin"
URL_DB = "localhost"
NAME_DB = "financial"
FULL_URL_DB = f"postgresql://{USER_DB}:{PASS_DB}@{URL_DB}/{NAME_DB}"

try:
    connection = psycopg2.connect(
        host=URL_DB, dbname=NAME_DB, user=USER_DB, password=PASS_DB
    )
except OperationalError as e:
    print(f"Connection error: {e}")
    connection = None


def create_user(username: str, email: str, password: str):  # Encript
    try:
        n_user = users(username=username, email=email, password=password)
        db.session.add(n_user)
        db.session.commit()
        return True
    except Exception as e:
        print(f"Error creating user: {e}")
        return False
    # try:
    #     connection = psycopg2.connect(
    #         host=URL_DB, database=NAME_DB, user=USER_DB, password=PASS_DB
    #     )
    #     # Test SQLInjection.
    #     sql_statment = (
    #         f"INSERT INTO users_(username, email, password) VALUES (%s, %s, %s)"
    #     )
    #     cur = connection.cursor()
    #     cur.execute(sql_statment, (username, email, password))
    #     connection.commit()
    #     cur.close()
    #     return True
    # except Exception as e:
    #     print(f"Error insert username: {e}")
    #     return False


def login_user(username: str, password: str):
    try:
        sql_statment = f"SELECT * FROM users_ WHERE username = %s"
        cur = connection.cursor()
        cur.execute(sql_statment, username)
        user = cur.fetchone()
        print(user[3])
        # TODO encript password
        cur.close()
        if user[3] == password:
            return user[0]
        else:
            return 0
    except Exception as e:
        print(f"Error login: {e}")
        return 0


def get_all_ex():
    pass


def get_monthly_ex():
    pass


def get_especific_ex():
    pass
