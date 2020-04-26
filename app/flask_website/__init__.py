import os

from flask import Flask, render_template

import flask_website
from flask_website.config import Config
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, instance_relative_config=True)
db = SQLAlchemy(app)

from flask_website.models import News, Contentmaker, Game_match


class PrefixMiddleware(object):

    def __init__(self, app, prefix=''):
        self.app = app
        self.prefix = prefix

    def __call__(self, environ, start_response):

        if environ['PATH_INFO'].startswith(self.prefix):
            environ['PATH_INFO'] = environ['PATH_INFO'][len(self.prefix):]
            environ['SCRIPT_NAME'] = self.prefix
            return self.app(environ, start_response)
        else:
            start_response('404', [('Content-Type', 'text/plain')])
            return ["This url does not belong to the app.".encode()]

def init_app(config_else: Config = None):
    """Configure an instance of the Flask application."""

    flask_website.app.config.from_object(Config)
    if config is not None:
        flask_website.app.config.from_object(config_else)

    flask_website.app.wsgi_app = PrefixMiddleware(flask_website.app.wsgi_app, prefix=flask_website.app.config['APPLICATION_ROOT'])

    # apply the blueprints to the app
    from flask_website.controllers.root import root_blueprints
    from flask_website.controllers.contentmaker import contentmaker_blueprints
    from flask_website.controllers.siteadmin import siteadmin_blueprints

    flask_website.app.register_blueprint(root_blueprints)
    flask_website.app.register_blueprint(contentmaker_blueprints)
    flask_website.app.register_blueprint(siteadmin_blueprints)


def run_app(config_else: Config = None):
    """Run of the Flask application."""

    init_app(config_else)

    flask_website.app.run()

