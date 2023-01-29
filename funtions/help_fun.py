import psycopg2

connection = psycopg2.connect(host="", database="", user="", password="")


def create_user(username: str, email: str, password: str):  # Encript
    try:
        # Test SQLInjection.
        sql_statment = f"INSERT INTO Users_ (username, email, password, confirmed) VALUES ({username}, {email}, {password})"
        cur = connection.cursor(sql_statment)
        cur.execute()
        connection.commit()
        return True
    except Exception as e:
        print(f"Error insert username: {e}")
        return False


def login_user(username: str, password: str):
    try:
        sql_statment = f"SELECT * FROM Users_ WHERE username = {username}"
        cur = connection.cursor()
        cur.execute(sql_statment)
        user = cur.fetchone()
        # TODO encript password
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
