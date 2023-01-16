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

`TELEGRAM_TOKEN`: You also need to create a Telegram bot. To do this, contact [BotFather](https://telegram.me/BotFather).

`TELEGRAM_CHAT_ID` is a link to a public Telegram channel in which photos will be published.

`DEVMEN_TOKEN` - pause of publications in hours.

```
/user/main.py/
|--foo.py
|  :
|--bar.py
|--.env


## Project Goals

The code is written for educational purposes for the online-course of the 
"Chatbots in Python" on [Devmen](https://dvmn.org/)
