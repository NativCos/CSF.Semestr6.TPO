"""
Модуль тестирования UI
"""
from selenium import webdriver


class Config:
    BASE_URL = 'http://178.62.61.130:8081/'


driver = webdriver.Chrome()


# Main
driver.get('{}'.format(Config.BASE_URL))
# Наличие верного заголовка сайта
assert 'ЦСКА' in driver.title
# Наличие Bootstrap контейнера для содержимого сайта
elem = driver.find_element_by_class_name('rgb-wrapper')
assert elem.find_element_by_id('rgb-wrapper') is not None

driver.close()
