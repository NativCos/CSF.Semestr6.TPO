import os


class Config(object):
    ROOT = os.path.abspath(os.path.dirname(__file__))
    DEBUG = True
    TESTING = True
    HOST = '192.168.1.22'
    PORT = 8080
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'
    TEMPLATE_FOLDER = os.path.join(ROOT, 'templates')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SITEADMIN_NAME = 'root'
    SITEADMIN_PASSWORD = 'root'
    SALT = 'abc'
    SERVER_NAME = HOST + ':' + ('' if PORT == 80 else str(PORT))
    APPLICATION_ROOT = '/pt'
    SECRET_KEY = b'_5#y2L"F4Q8z]/'
