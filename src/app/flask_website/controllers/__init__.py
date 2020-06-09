from .contentmaker import contentmaker_blueprints
from .siteadmin import siteadmin_blueprints
from .root import root_blueprints
from .api import api_blueprints

import locale
locale.setlocale(locale.LC_TIME, 'ru_RU.UTF-8')

__all__ = ['contentmaker_blueprints','siteadmin_blueprints','root_blueprints','api_blueprints']