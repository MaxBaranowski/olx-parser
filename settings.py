# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

import os
import warnings

from envparse import env

env_file_path = os.path.join(os.path.dirname(__file__), '.env')
if not os.path.isfile(env_file_path):
    warnings.warn('.env file not found. The application will be stopped.', ResourceWarning)
    exit(1)

env.read_envfile(env_file_path)


class config:
    DEFAULT_USER_AGENT = env.str('DEFAULT_USER_AGENT',
                                 default='Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.91 Safari/537.36')

    BASE_URL = env.str('BASE_URL', default='https://www.olx.ua/')
    PHONE_URL = env.str('PHONE_URL', default='https://www.olx.ua/ajax/misc/contact/phone/')

    CATEGORY = env.str('CATEGORY', default='nedvizhimost')
    SUB_CATEGORY = env.str('SUB_CATEGORY', default='arenda-kvartir')
    SUB_SUB_CATEGORY = env.str('SUB_SUB_CATEGORY', default='dolgosrochnaya-arenda-kvartir')
    CITY = env.str('CITY', default='odessa')
    DISTRICT_ID = env.int('DISTRICT_ID', default=89)
    MIN_PRICE = env.int('MIN_PRICE', default=1000)
    MAX_PRICE = env.int('MAX_PRICE', default=5000)
    MIN_ROOMS = env.int('MIN_ROOMS', default=1)
    MAX_ROOMS = env.int('MAX_ROOMS', default=1)
    WITH_PHOTOS = int(env.bool('WITH_PHOTOS', default=True))
    WITH_PROMOTED = env.bool('WITH_PROMOTED', default=False)
    PUBLICATION_DATE = [item.lower() for item in env.list('PUBLICATION_DATE', default=['сегодня', 'вчера'])]

    USER_EMAIL = env.str('USER_EMAIL', default=None)
    USER_PASSWORD = env.str('USER_PASSWORD', default=None)

    DB_CONFIG = {
        'apiKey': env.str('DB_API_KEY', default=''),
        'authDomain': env.str('DB_AUTH_DOMAIN', default=''),
        'databaseURL': env.str('DB_DATABASE_URL', default=''),
        'storageBucket': env.str('DB_STORAGE_BUCKET', default=''),
    }

    TELEGRAM_BOT_API_URL = env.str('TELEGRAM_BOT_API_URL', default='https://api.telegram.org/bot')
    TELEGRAM_BOT_KEY = env.str('TELEGRAM_BOT_KEY', default=None)
    TELEGRAM_CHAT_IDS = env.list('TELEGRAM_CHAT_IDS', default=[])

    LOG_FILENAME = env.str('LOG_FILENAME', default='olx_parser_log')
