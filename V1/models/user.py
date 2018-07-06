from flask_bcrypt import Bcrypt
from V1.database.connector import DatabaseConnection
from V1 import db
import psycopg2
import datetime
import jwt

database_connection = DatabaseConnection()


class User:
    """User class model"""

    def __init__(self,
                 firstname,
                 lastname,
                 email,
                 password,
                 secret,
                 admin=False):
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.password_hash = Bcrypt().generate_password_hash(password).decode()
        self.secret = secret
        self.admin = admin
        database_connection.insert_user(self.firstname, self.lastname,
                                        self.email, self.password_hash,
                                        self.secret)
