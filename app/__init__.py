import os
import configparser

from aiohttp import BasicAuth
from aiogram import Bot

TELEGRAM_TOKEN = os.environ['TELEGRAM_TOKEN']

config = configparser.ConfigParser()
config.read('config.ini')

BOT_ID = int(config.get('Telegram', 'bot_id'))
ADMIN_ID = int(config.get('Telegram', 'admin_id'))

if config.get('Proxy', 'use_proxy') == 'yes':
    proxy_url = os.environ['PROXY_URL']
    proxy_login = os.environ['PROXY_LOGIN']
    proxy_password = os.environ['PROXY_PASSWORD']

    proxy_auth = BasicAuth(login=proxy_login,
                           password=proxy_password)
    bot = Bot(token=TELEGRAM_TOKEN, parse_mode='Markdown',
              proxy_auth=proxy_auth, proxy=proxy_url)
else:
    bot = Bot(token=TELEGRAM_TOKEN, parse_mode='Markdown')

def get_bot() -> Bot:
    return bot

def get_admin_id() -> int:
    return ADMIN_ID

def get_bot_id() -> int:
    return BOT_ID