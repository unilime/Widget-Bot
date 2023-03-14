import telegram
from config import TELEGRAM_BOT_TOKEN, TELEGRAM_CHAT_ID


def notify_ending(message):
    bot = telegram.Bot(token=TELEGRAM_BOT_TOKEN)
    bot.sendMessage(chat_id=TELEGRAM_CHAT_ID, text=message)


def generate_message(title, message='Test Message'):
    full_t_message = title + '\n\n' + \
                     'Error: ' + message
    return full_t_message
