import requests
import time
import os
import telegram
import logging
from dotenv import load_dotenv


logger = logging.getLogger('TgLog')


class MyLogsHandler(logging.Handler):
    """Logger handler for Telegram"""

    def __init__(self, tg_token: str, tg_chat_id: str,):

        super().__init__()
        self.tg_token = tg_token
        self.tg_chat_id = tg_chat_id
        self.bot = telegram.Bot(token=self.tg_token)

    def emit(self, record):
        log_entry = self.format(record)
        self.bot.send_message(chat_id=self.tg_chat_id, text=log_entry)


def run_bot(devmen_token, tg_token, tg_chat_id, logger):
    url = 'https://dvmn.org/api/long_polling/'
    head = {
        'Authorization': f'Token {devmen_token}'
    }
    timestamp = None
    bot = telegram.Bot(token=tg_token)
    logger.info('The bot is running!')
    while True:
        payload = {
            'timeout': 60,  # seconds
            'timestamp': timestamp
        }
        try:
            response = requests.get(url, headers=head, params=payload)
            response.raise_for_status
            status_info = response.json()

            if status_info['status'] == 'timeout':
                timestamp = status_info['timestamp_to_request']
            elif status_info['status'] == 'found':
                lesson = status_info['new_attempts'][0]['lesson_title']
                conclusion = 'The teacher liked everything, \
                    you can start the next task!'
                if status_info['new_attempts'][0]['is_negative']:
                    conclusion = 'Unfortunately you have errors.'
                message = f'Have you checked the work of "{lesson}"! \n\n' \
                          f'{conclusion}'
                bot.send_message(text=message, chat_id=tg_chat_id)

        except requests.exceptions.ReadTimeout:
            logger.exception('The Devmen is not responding')
        except requests.exceptions.ConnectionError:
            time.sleep(5)
            logger.exception('Connection error!')
        except Exception:
            logger.exception('Error!')


def main():
    load_dotenv()
    devmen_token = os.getenv('DEVMEN_TOKEN')
    tg_token = os.getenv('TELEGRAM_TOKEN')
    tg_chat_id = os.getenv('TELEGRAM_CHAT_ID')

    logger.setLevel(level=logging.INFO)
    logger.addHandler(MyLogsHandler(tg_token, tg_chat_id))
    logger.info('BingoBom!')

    run_bot(devmen_token, tg_token, tg_chat_id, logger)


if __name__ == '__main__':
    main()
