import requests
import time
import os
import telegram
from dotenv import load_dotenv


def request_devmen(devmen_token, timestamp):
    url = 'https://dvmn.org/api/long_polling/'
    head = {
        'Authorization': f'Token {devmen_token}'
    }
    payload = {
        'timeout': 60,  # seconds
        'timestamp': timestamp
    }
    response = requests.get(url, headers=head, params=payload)
    response.raise_for_status
    return response.json()


def run_bot(devmen_token, tg_token, tg_chat_id):
    timestamp = None
    while True:
        try:
            status_info = request_devmen(devmen_token, timestamp)
            if status_info['status'] == 'timeout':
                timestamp = status_info['timestamp_to_request']
            elif status_info['status'] == 'found':
                lesson = status_info['new_attempts'][0]['lesson_title']
                conclusion = 'The teacher liked everything, \
                    you can start the next task!'
                if status_info['new_attempts'][0]['is_negative']:
                    conclusion = 'Unfortunately you have errors.'
                bot = telegram.Bot(token=tg_token)
                message = f'Have you checked the work of "{lesson}"! \n\n' \
                          f'{conclusion}'
                bot.send_message(text=message, chat_id=tg_chat_id)

        except requests.exceptions.ReadTimeout:
            pass
        except requests.exceptions.ConnectionError:
            time.sleep(5)
            print('reconnect!')


def main():
    load_dotenv()
    devmen_token = os.getenv('DEVMEN_TOKEN')
    tg_token = os.getenv('TELEGRAM_TOKEN')
    tg_chat_id = os.getenv('TELEGRAM_CHAT_ID')

    run_bot(devmen_token, tg_token, tg_chat_id)


if __name__ == '__main__':
    main()
