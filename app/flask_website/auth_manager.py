"""
Модуль, который обеспечивает управление сессиями пользователей.
"""
from flask_login import UserMixin, LoginManager, login_user
from flask_website.models import Admin, Contentmaker
from flask_website.service import AdminService, ContentmakerService

auth_manager = LoginManager()


class UserRole:
    administrator = 0
    contentmaker = 1


class FlaskUser(UserMixin):
    def __init__(self, id_login, control_object):
        self.id_login = id_login
        self.control_object = control_object

    def __repr__(self):
        return "<FlaskUser(login=%r, role=%r)>" % (self.id_login, self.get_user_role())

    def get_user_role(self):
        return self.convert_id_login_to_user_role(self.id_login)

    def get_id(self):
        return self.id_login

    def get_control_object(self) -> object:
        return self.control_object

    @staticmethod
    def convert_id_login_to_user_role(id_login):
        if id_login == 'root':
            return UserRole.administrator
        else:
            return UserRole.contentmaker

    @staticmethod
    def login(login: str, password: str) -> bool:
        user_role = FlaskUser.convert_id_login_to_user_role(login)
        if user_role == UserRole.contentmaker:
            try:
                c = Contentmaker.query.filter_by(login=str(login)).first()
                if c.password == password:
                    login_user(FlaskUser(login, ContentmakerService(c)))
                    return True
                else:
                    return False
            except Exception:
                return False
        elif user_role == UserRole.administrator:
            if Admin().get_password() == password:
                login_user(FlaskUser(login, AdminService()))
                return True
            else:
                return False
        return False


@auth_manager.user_loader
def load_user(id_login):
    user_role = FlaskUser.convert_id_login_to_user_role(id_login)
    if user_role == UserRole.contentmaker:
        return FlaskUser(id_login, ContentmakerService( Contentmaker.query.filter_by(login=str(id_login)).first()) )
    elif user_role == UserRole.administrator:
        return FlaskUser(id_login, AdminService())


@auth_manager.unauthorized_handler
def unauthorized():
    return 'Вы кто такие? Я вас не звал!'
