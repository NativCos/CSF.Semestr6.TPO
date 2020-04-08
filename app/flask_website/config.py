import os


class Config(object):
    ROOT = os.path.abspath(os.path.dirname(__file__))
    DEBUG = True
    TESTING = True
    HOST = '127.0.0.1'
    PORT = 8080
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'
    TEMPLATE_FOLDER = os.path.join(ROOT, 'templates')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SITEADMIN_NAME = root
    SITEADMIN_PASSWORD = root
    SALT = "abc"
