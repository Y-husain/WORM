from flask_restplus import Resource, Namespace, fields
from flask import request
from flask_bcrypt import Bcrypt
from psycopg2.extras import RealDictCursor
import json
import re

from V1.models.user import User
from V1.database.connector import DatabaseConnection
database_connection = DatabaseConnection()

auth_namespace = Namespace(
    "auth", description="Authentication Related Operation")

registration_model = auth_namespace.model(
    "Registration", {
        "FirstName":
        fields.String(
            required=True, description='Your First Name', example='John'),
        "LastName":
        fields.String(
            required=True, description='Your Last Name', example='Doe'),
        "Email":
        fields.String(
            required=True,
            description='your email accounts',
            example='john_doe@example.com'),
        "Password":
        fields.String(
            required=True,
            description='Your secret password',
            example='vU22f53nNp'),
        "Secret":
        fields.String(
            required=True, description='Your secret word', example="MyMum")
    })

auth_namespace.route('/signup')


@auth_namespace.route('/signup')
class Signup(Resource):
    """Handle signup routes"""

    @auth_namespace.expect(registration_model)
    def post(self):
        """Register new user"""
        data = request.get_json()
        try:
            firstname = data["FirstName"]
            lastname = data["LastName"]
            email = data["Email"]
            password = data["Password"]
            secret = data["Secret"]
        except KeyError:
            return {"Message": "Please fill all the inputs"}
        all_email = database_connection.query_email()
        confirm = bool(email in all_email)
        if confirm:
            return {"Message": "Email already exist"}
        if not confirm:
            user = User(firstname, lastname, email, password, secret)
            user.save()
            return {'Message': 'Successfully Registered'}, 201
