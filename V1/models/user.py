from flask_bcrypt import Bcrypt
from V1 import db
import psycopg2
import datetime
import jwt


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
        self.admin = admin

    def create(self):
        """Save user in a database"""
        try:
            db.cur.execute(
                "INSERT INTO users(firstname,lastname, email, password, secret admin) VALUES(%s,%s,%s,%s)",
                (self.firstname, self.lastname, self.email, self.password_hash,
                 self.admin))
            db.conn.commit()
        except (Exception, psycopg2.IntegrityError) as error:
            print(error)
