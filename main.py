from telegram.ext import Updater

from handlers import setup_dispatcher
from settings import TELEGRAM_TOKEN, HEROKU_APP_NAME, PORT

# Configure app to receive updates from bot
updater = Updater(TELEGRAM_TOKEN)

# Get and setup an event dispatcher from Telegram bot API
dp = updater.dispatcher
dp = setup_dispatcher(dp)

# Run bot in a polling mode (for testing only)
if HEROKU_APP_NAME is None:
    print("Can't detect 'HEROKU_APP_NAME' env. Running bot in pooling mode.")

    updater.start_polling()

    # Start idle (block any further code execution until one of the signals [SIGINT, SIGTERM, SIGABRT] received)
    updater.idle()

# Run bot in a webhook mode (make Telegram API to send updates here)
else:
    print(f"Running bot in webhook mode. Make sure that this url is correct: https://{HEROKU_APP_NAME}.herokuapp.com/")
    updater.start_webhook(
        listen="0.0.0.0",
        port=PORT,
        url_path=TELEGRAM_TOKEN,
        webhook_url=f"https://{HEROKU_APP_NAME}.herokuapp.com/{TELEGRAM_TOKEN}"
    )

    updater.idle()
