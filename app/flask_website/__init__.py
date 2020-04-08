import os

from flask import Flask, render_template

import flask_website
from flask_website.config import Config
from flask_sqlalchemy import SQLAlchemy

app = None
db = None


def init_app(config_else: Config = None):
    """Configure an instance of the Flask application."""

    flask_website.app = Flask(__name__, instance_relative_config=True)

    flask_website.app.config.from_object(Config)
    if config is not None:
        flask_website.app.config.from_object(config_else)

    flask_website.db = SQLAlchemy(flask_website.app)

    # apply the blueprints to the app
    from flask_website.controllers.root import root_blueprints

    flask_website.app.register_blueprint(root_blueprints)


def run_app(config_else: Config = None):
    """Run of the Flask application."""

    init_app(config_else)

    flask_website.app.run(flask_website.app.config['HOST'], flask_website.app.config['PORT'])
