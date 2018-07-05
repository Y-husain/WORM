from flask import Flask
from flask_restplus import Api
from V1.configurations.config import app_config

api = Api(
    version='1.0',
    title='Business Review API',
    description='A Simple Maintenance API',
    prefix='/api/v1')


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(app_config[config_name])
    api.init_app(app)
    return app