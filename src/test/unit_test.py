"""
Модуль тестирования UNIT
"""
import unittest
from flask_website import init_app
from flask_website.service import ClientService, ContentmakerService, AdminService
from datetime import datetime

init_app()


class Config:
    URL = '127.0.0.1:8080/pt/'


class ClientServiceTest(unittest.TestCase):
    """Тестирование клиента"""
    def test_get_all_matches(self):
        assert ClientService.get_all_matches() is not None

    def test_get_all_news(self):
        assert ClientService.get_all_news() is not None


class ContentmakerServiceTest(unittest.TestCase):
    """Тестирование контент мейкера"""
    def test_add_new_news(self):
        ContentmakerService.add_new_news('Это заголовок новости', 'Это сама новость.',
                                                               datetime(2020, 5, 5))

    def test_add_new_match(self):
        ContentmakerService.add_new_match(datetime(2020,5,5), 4, 4, 'А это имя соперника',
                                                                'А это имя того места где игра')


class AdminServiceTest(unittest.TestCase):
    """Тестирование администратора"""
    def test_add_new_contentmacker(self):
        AdminService().add_new_contentmacker('contentmacker_login', 'mail@site')
        assert len( AdminService().get_all_contenmakers()) >= 1

    def test_get_own_admin(self):
        assert AdminService().get_own_admin() is not None

    def test_ch_pass(self):
        AdminService().change_password('rootroot')
        assert AdminService().get_own_admin().get_password() is 'rootroot'

if __name__ == '__main__':
    unittest.main()
