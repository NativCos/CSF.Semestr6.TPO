"""
Модуль отвечает за бизнес логику приложения.
"""
from flask_website.models import News, Admin, Game_match, Contentmaker
from datetime import datetime
from flask_website import db
import random
import string


def _randomString(stringLength=8):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))


class IClientService(object):
    @staticmethod
    def get_list_news(start_date: datetime, end_date: datetime):
        return db.session.query(News).filter(News.date.between(start_date, end_date)).all()

    @staticmethod
    def get_all_news():
        return News.query.all()

    @staticmethod
    def get_thenews(id: int) -> News:
        return News.query.filter_by(id=int(id)).first()

    @staticmethod
    def get_thematch(id: int) -> Game_match:
        return Game_match.query.filter_by(id=int(id)).first()

    @staticmethod
    def get_list_matches(start_date: datetime, end_date: datetime):
        return db.session.query(Game_match).filter(Game_match.date.between(start_date, end_date)).all()

    @staticmethod
    def get_all_matches():
        return db.session.query(Game_match).order_by(Game_match.date)


class ClientService(IClientService):
    def __init__(self):
        pass


class IContentmakerService(object):
    @staticmethod
    def add_new_news(header: str, body: str, date: datetime) -> None:
        nn = News()
        nn.header = header
        nn.body = body
        nn.date = date
        db.session.add(nn)
        db.session.commit()

    @staticmethod
    def del_news(id: int) -> None:
        nn = News()
        nn.id = id
        db.session.delete(nn)
        db.session.commit()

    @staticmethod
    def add_new_match(date: datetime, score_own: int, score_rival: int, rival: str, place_of_play: str) -> None:
        nm = Game_match()
        nm.date = date
        nm.score_own = score_own
        nm.score_rival = score_rival
        nm.rival = rival
        nm.place_of_play = place_of_play
        db.session.add(nm)
        db.session.commit()

    @staticmethod
    def del_match(id: int) -> None:
        n = Game_match()
        n.id = id
        db.session.delete(n)
        db.session.commit()

    @staticmethod
    def ch_match(id: int, date: datetime, score_own: int, score_rival: int, rival: str, place_of_play: str) -> None:
        n = Game_match()
        n.id = id
        n.date = date
        n.score_own = score_own
        n.score_rival = score_rival
        n.rival = rival
        n.place_of_play = place_of_play
        db.session.delete(n)
        db.session.add(n)
        db.session.commit()


class ContentmakerService(IContentmakerService, IClientService):
    def __init__(self, own_contentmaker: Contentmaker):
        super().__init__()
        self.own_contentmaker = own_contentmaker

    def get_own_contentmaker(self) -> Contentmaker:
        return self.own_contentmaker

    def change_password(self, newpass: str) -> None:
        db.update(Contentmaker).where(Contentmaker.id == self.own_contentmaker.id).values(password=newpass)
        db.session.commit()


class AdminService(IContentmakerService, IClientService):
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(AdminService, cls).__new__(cls)
        return cls.instance

    def get_own_admin(self) -> Admin:
        return Admin()

    def change_password(self, newpass: str) -> None:
        Admin().update_password(newpass)

    def add_new_contentmacker(self, login: str, mail: str) -> None:
        ncm = Contentmaker()
        ncm.login = login
        ncm.mail = mail
        ncm.password = _randomString()
        db.session.add(ncm)
        db.session.commit()

    def del_contentmaker(self, id: int) -> None:
        cm = Contentmaker()
        cm.id = id
        db.session.delete(cm)
        db.session.commit()

    def get_all_contenmakers(self):
        return Contentmaker.query.all()
