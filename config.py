from dotenv import load_dotenv
from os import environ, path

base_path = path.dirname(path.abspath(__file__))

if path.exists('.env'):
    load_dotenv(dotenv_path=base_path + '/.env')

CHROMEDRIVER_PATH = environ.get('CHROMEDRIVER_PATH', base_path + '/drivers/chromedriver')

EBAY_EDITORIAL_URL = environ.get('EBAY_EDITORIAL_URL')
EBAY_EDITORIAL_TOKEN = environ.get('EBAY_EDITORIAL_TOKEN')

WIDGET_URL = 'https://store.munkpack.com/products/coconut-cocoa-chip-keto-granola-bar-12-pack'

TELEGRAM_BOT_TOKEN = environ.get('TELEGRAM_BOT_TOKEN')
TELEGRAM_CHAT_ID = environ.get('TELEGRAM_CHAT_ID')