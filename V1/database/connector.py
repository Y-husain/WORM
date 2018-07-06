import pprint as pp
import psycopg2


class DatabaseConnection:
    """Database connection"""

    def __init__(self):
        try:
            self.connection = psycopg2.connect(
                "dbname='connect_api' user='hassan' host='localhost' password='yahya' port='5432'"
            )
            self.connection.autocommit = True
            self.cursor = self.connection.cursor()
        except:
            pp.pprint("SORRY cannot connect to database")

    def create_tables(self):
        try:
            user_table = """CREATE TABLE users(
            id SERIAL PRIMARY KEY,
            firstname VARCHAR(100) NOT NULL,
            lastname VARCHAR(100) NOT NULL,
            email VARCHAR(100) NOT NULL,
            password VARCHAR(100) NOT NULL,
            secret VARCHAR(100)
        )"""
            self.cursor.execute(user_table)
        except (Exception, psycopg2.DatabaseError) as e:
            pp.pprint(e)

    def insert_user(self, firstname, lastname, email, password, secret):
        try:
            self.cursor.execute(
                "INSERT INTO users(firstname,lastname, email, password, secret) VALUES(%s,%s,%s,%s,%s)",
                (firstname, lastname, email, password, secret))
        except (Exception, psycopg2.IntegrityError) as error:
            pp.pprint(error)
