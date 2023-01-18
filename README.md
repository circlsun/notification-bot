# Bot notifications checking Devmen lessons

This is Telegram-Bot for notification about checking Devmen lessons.

## How to install

Python3 should be already installed. 
Then use `pip` (or `pip3`, if there is a conflict with Python2) to install dependencies:
```
pip install -r requirements.txt
```
### Virtual envs

`.env` file contents:

```
TELEGRAM_TOKEN='*******************'
TELEGRAM_CHAT_ID='*********'
DEVMEN_TOKEN='******************************************'
```

`TELEGRAM_TOKEN` - If you need to create a Telegram bot. To do this, contact [BotFather](https://telegram.me/BotFather).

`TELEGRAM_CHAT_ID` - This is a link to a Telegram channel.

`DEVMEN_TOKEN` - The student's personal token can be obtained here: [API-Devmen](https://dvmn.org/api/docs/).

```
/user/main.py/
|--foo.py
|  :
|--bar.py
|--.env
```
## Usage

Run the python script main.py with concole command:
```
python3 main.py
```

## Project Goals

The code is written for educational purposes for the online-course of the 
"Chatbots in Python" on [Devmen](https://dvmn.org/)
