import requests
from apps.articles.models import (
    TelegramBotSettings
)


def send_message(message, chat_id):
    telegram_settings = TelegramBotSettings.objects.first() 
    bot_token = telegram_settings.bot_token
    api_url = f'https://api.telegram.org/bot{bot_token}/sendMessage'
    response = requests.post(api_url, json={'chat_id': chat_id, 'text': message})


