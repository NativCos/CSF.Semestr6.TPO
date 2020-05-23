"""
Веб приложение сайт футбольного клуба ЦСКА.
"""
import os
from datetime import datetime

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import flask_website

app = Flask(__name__, instance_relative_config=True)
db = SQLAlchemy(app)

from .models import News, Contentmaker, Game_match
from .auth_manager import auth_manager

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


def init_db():
    """подобие миграции"""
    if not flask_website.db.engine.dialect.has_table(flask_website.db.engine,
                                                     News.__tablename__):  # If table don't exist, Create.
        flask_website.db.create_all()
        flask_website.db.session.commit()
        for i in range(3):
            new_news = News()
            new_news.header = "test news"
            new_news.date = datetime.utcnow()
            new_news.body = "test news.test news.test news.test news.test news.test news.test news.test news.test news.test news.test news"
            flask_website.db.session.add(new_news)
            new_match = Game_match()
            new_match.date = datetime(2050,1,1)
            new_match.place_of_play = "test match place"
            new_match.rival = 'rest match rival'
            new_match.score_own = 4
            new_match.score_rival = 1
            flask_website.db.session.add(new_match)
            flask_website.db.session.commit()
        new_match = Game_match()
        new_match.date = datetime(2019, 1, 1)
        new_match.place_of_play = "test match place"
        new_match.rival = 'rest match rival'
        new_match.score_own = 4
        new_match.score_rival = 1
        flask_website.db.session.add(new_match)
        new_match = Game_match()
        new_match.date = datetime(2019, 1, 2)
        new_match.place_of_play = "test match place"
        new_match.rival = 'rest match rival'
        new_match.score_own = 4
        new_match.score_rival = 1
        flask_website.db.session.add(new_match)
        new_match = Game_match()
        new_match.date = datetime(2019, 1, 3)
        new_match.place_of_play = "test match place"
        new_match.rival = 'rest match rival'
        new_match.score_own = 4
        new_match.score_rival = 1
        flask_website.db.session.add(new_match)
        new_match = Game_match()
        new_match.date = datetime(2050, 1, 1)
        new_match.place_of_play = "test match place"
        new_match.rival = 'rest match rival'
        new_match.score_own = 999
        new_match.score_rival = 999
        flask_website.db.session.add(new_match)
        flask_website.db.session.commit()


def init_app(config_file=None):
    """Configure an instance of the Flask application."""
    flask_website.app.config['PATH_TO_CONFIG_FILE'] = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'config.cfg')
    flask_website.app.config.from_pyfile(flask_website.app.config['PATH_TO_CONFIG_FILE'])
    if config_file is not None:
        flask_website.app.config.from_pyfile(config_file)
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

    init_db()


def run_app(config_file=None):
    """Run of the Flask application."""
    init_app(config_file)
    flask_website.app.run()
