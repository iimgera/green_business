import requests

def send_message(message, chat_id):
    api_token = '5672472092:AAHfzXa5wW6KcBLvN46HGu1MuF-wMX0vzgo'
    api_url = f'https://api.telegram.org/bot{api_token}/sendMessage'
    response = requests.post(api_url, json={'chat_id': chat_id, 'text': message})

send_message(message='python1111111111111111', chat_id=-1001823757597)

# import requests

# def send_message(message, channel_id, bot_token):
#     api_url = f'https://api.telegram.org/bot{bot_token}/sendMessage'
#     response = requests.post(api_url, json={'chat_id': channel_id, 'text': message})

# bot_token = '5672472092:AAHfzXa5wW6KcBLvN46HGu1MuF-wMX0vzgo'
# channel_id = '-1001823757597' 
# send_message(message='Hello, channel!', channel_id=channel_id, bot_token=bot_token)
