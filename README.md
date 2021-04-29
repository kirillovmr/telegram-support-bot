## How bot works:

1. Your client write a message to your bot
2. Bot forwards the message to your secret chat
3. Any chat participant can reply on a forwarded message
4. Bot will copy the message and send it to your client

## .env variables

You need to specify these env variables to run this bot.  
If you run it locally, you can also write them in `.env` text file.

``` bash
# Your bot's token
TELEGRAM_TOKEN=

# chat_id where the bot will forward all incoming messages
TELEGRAM_SUPPORT_CHAT_ID=

# Name of your Heroku app for webhook setup (NEEDED ON DEPLOY ONLY)
# HEROKU_APP_NAME=

# Text of a message that bot will write on /start command (OPTIONAL)
# WELCOME_MESSAGE=

# Emoji that will be sent after WELCOME_MESSAGE (OPTIONAL)
# WELCOME_EMOJI=
```

## Run bot locally

First, you need to install all dependencies:

```bash
pip3 install -r requirements.txt
```

Then you can run the bot.  
Don't forget to create `.env` file in the root folder with all required params (read above).

``` bash
python main.py
```
