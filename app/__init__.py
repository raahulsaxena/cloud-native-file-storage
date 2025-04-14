from flask import Flask
from app.routes import api

def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config.Config')  # <- Link the config class here

    app.register_blueprint(api)
    return app