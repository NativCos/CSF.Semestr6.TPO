from flask_website import db


class News(db.Model):
    __tablename__ = 'news'
    id = db.Column(db.Integer, primary_key=True)
    header = db.Column(db.String(300), index=True, unique=True, nullable=False)
    """Заголовок новости"""
    date = db.Column(db.DateTime, nullable=False)
    """Дата новости"""
    body = db.Column(db.String(10000), nullable=False)
    """текст новости"""

    def __repr__(self):
        return '<News {' + 'id=' + self.id + ',' + 'header=' + self.header + ',' + 'date=' + self.date + ',' + 'body=' + self.body + '}>'


class Football_player(db.Model):
    __tablename__ = 'football_player'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    """Имя игрока"""
    citizenship = db.Column(db.String(200), nullable=False)
    """Гражданство"""
    team_position = db.Column(db.String(200), nullable=False)
    """Позиция в команде"""

    def __repr__(self):
        return '<Football_player {' + 'id=' + self.id + ', ' + 'name=' + self.name + ', ' + 'citizenship=' + self.citizenship + ', ' + 'team_position=' + self.team_position + '}'


class Game_match(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime, nullable=True)
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
        return '<Game_match {' + 'id=' + self.id + ', '  'date=' + self.date + ', ' 'score_own=' + self.score_own + ', ' 'score_rival=' + self.score_rival + ', ' 'rival=' + self.rival + ', ' 'place_of_play=' + self.place_of_play + '}'


class Contentmaker(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False, unique=True)
    """Короткое имя"""
    date_of_creation = db.Column(db.DateTime, nullable=False)
    """Дата создания учетной записи контент мейкера"""
    mail = db.Column(db.String(200), nullable=False)
    """Почта для связи"""
    password = db.Column(db.String(200), nullable=False)
    """Пароль хешированный с солью"""

    def __repr__(self):
        return '<Contentmaker {' + 'id=' + self.id + ', '  'name=' + self.name + ', ' 'date_of_creation=' + self.date_of_creation + ', ' 'mail=' + self.mail + ', ' 'password=' + self.password + '}'
