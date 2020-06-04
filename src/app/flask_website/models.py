"""
Модуль отвечает за слои persistence & repository.
Содержит данные для работы сервисного слоя приложения, модели данных предметной области.
Оборачивает операции создания и извлечения данных для сервисного уровня.
"""
from flask_website import db
from flask_website import app
import re
from datetime import datetime


class News(db.Model):
    """Модель новость"""
    __tablename__ = 'news'
    id = db.Column(db.Integer, primary_key=True)
    header = db.Column(db.String(300), index=True, nullable=False)
    """Заголовок новости"""
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    """Дата новости"""
    body = db.Column(db.String(10000), nullable=False)
    """текст новости"""

    def __repr__(self):
        return '<News (' + 'id=' + self.id + ',' + 'header=' + self.header + ',' + \
               'date=' + self.date + ',' + 'body=' + self.body + ')>'


class Game_match(db.Model):
    """Модель матч"""
    __tablename__ = 'game_match'
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    """Дата матча"""
    score_own = db.Column(db.Integer, nullable=True)
    """Счет нашей команды"""
    score_rival = db.Column(db.Integer, nullable=True)
    """Счет соперников"""
    rival = db.Column(db.String(200), nullable=False)
    """Имя команды соперников"""
    place_of_play = db.Column(db.String(200), nullable=False)
    """Место игры"""

    def __repr__(self):
        return '<Game_match (' + 'id=' + self.id + ', '  'date=' + self.date + ', ' 'score_own=' + \
               self.score_own + ', ' 'score_rival=' + self.score_rival + ', ' 'rival=' + \
               self.rival + ', ' 'place_of_play=' + self.place_of_play + ')>'


class Contentmaker(db.Model):
    """Модель контент мейкер"""
    __tablename__ = 'сontentmaker'
    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String(200), nullable=False, unique=True)
    """Короткое имя"""
    date_of_creation = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    """Дата создания учетной записи контент мейкера"""
    mail = db.Column(db.String(200), nullable=False)
    """Почта для связи"""
    password = db.Column(db.String(200), nullable=False)
    """Пароль хешированный с солью"""

    def __repr__(self):
        return '<Contentmaker (' + 'id=' + self.id + ', '  'name=' + self.name + ', ' 'date_of_creation=' + \
               self.date_of_creation + ', ' 'mail=' + self.mail + ', ' 'password=' + self.password + ')>'


class Admin(object):
    """Модель администратора"""
    def __init__(self):
        pass

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Admin, cls).__new__(cls)
        return cls.instance

    def __repr__(self):
        return '<Admin (' + 'login=' + self.get_login() + ', password=' + self.get_password() + ')>'

    def get_login(self) -> str:
        return app.config['SITEADMIN_NAME']

    def get_password(self) -> str:
        return app.config['SITEADMIN_PASSWORD']

    def update_password(self, newpassword: str):
        app.config.update(SITEADMIN_PASSWORD=newpassword)
        config_file = open(app.config['PATH_TO_CONFIG_FILE'], 'r')
        config_str = config_file.read()
        val = re.findall(r'SITEADMIN_PASSWORD = \'.*\'', config_str)
        if len(val) != 0:
            config_str = config_str.replace(val[0], 'SITEADMIN_PASSWORD = \'{}\''.format(newpassword))
        else:
            config_str = config_str + ('\nSITEADMIN_PASSWORD = \'' + newpassword + '\'')
        config_file.close()
        config_file_w = open(app.config['PATH_TO_CONFIG_FILE'], 'w')
        config_file_w.write(config_str)
        config_file_w.close()
