from flask import Flask
from flask_restplus import Api
from V1.configurations.config import app_config
from V1.database.connector import connectorDB

api = Api(
    version='1.0',
    title='Business Review API',
    description='A Simple Business Review API',
    prefix='/api/v1')

db = connectorDB()


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(app_config[config_name])
    db.init_app(config_name)
    api.init_app(app)
    return app