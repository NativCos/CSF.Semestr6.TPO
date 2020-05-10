"""
Веб приложение сайт футбольного клуба ЦСКА.
"""
import os
from flask import Flask
import flask_website
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, instance_relative_config=True)
db = SQLAlchemy(app)

from flask_website.models import News, Contentmaker, Game_match
from flask_website.auth_manager import auth_manager

auth_manager.init_app(app)


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


def init_app(config_file):
    """Configure an instance of the Flask application."""
    flask_website.app.config.from_pyfile(os.path.join(os.path.abspath(os.path.dirname(__file__)), 'config.cfg'))
    if config_file is not None:
        flask_website.app.config.from_object(config_file)
        flask_website.app.config['PATH_TO_CONFIG_FILE'] = config_file

    flask_website.app.wsgi_app = PrefixMiddleware(flask_website.app.wsgi_app,
                                                  prefix=flask_website.app.config['APPLICATION_ROOT'])

    # apply the blueprints to the app
    from flask_website.controllers import root_blueprints
    from flask_website.controllers import contentmaker_blueprints
    from flask_website.controllers import siteadmin_blueprints
    from flask_website.controllers import api_blueprints

    flask_website.app.register_blueprint(root_blueprints)
    flask_website.app.register_blueprint(contentmaker_blueprints)
    flask_website.app.register_blueprint(siteadmin_blueprints)
    flask_website.app.register_blueprint(api_blueprints)

    # подобие миграции
    if not flask_website.db.engine.dialect.has_table(flask_website.db.engine,
                                                     News.__tablename__):  # If table don't exist, Create.
        db.create_all()
        db.session.commit()


def run_app(config_file=None):
    """Run of the Flask application."""
    init_app(config_file)
    flask_website.app.run()
