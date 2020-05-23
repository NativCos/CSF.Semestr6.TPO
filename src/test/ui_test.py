"""
Модуль тестирования UI
"""
from selenium import webdriver


class Config:
    URL = '127.0.0.1:8080/pt/'


driver = webdriver.Chrome()


# Main
driver.get('{}'.format(Config.URL))
assert '<<>>' in driver.title
elem = driver.find_element_by_class_name('<<>>')
assert elem.find_element_by_id('<<>>') is not None


driver.close()
