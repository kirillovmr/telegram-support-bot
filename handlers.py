import os
from telegram.ext import CommandHandler, MessageHandler, Filters

from settings import WELCOME_MESSAGE, WELCOME_EMOJI, TELEGRAM_SUPPORT_CHAT_ID

# To be executed once the user starts a bot
def start(update, context):
    # Send welcome message to the user
    update.message.reply_text(WELCOME_MESSAGE)
    update.message.reply_text(WELCOME_EMOJI)

    # Generate and send user info to support channel
    user_info = update.message.from_user
    text_message = f"📞 New user connected: id {55787210}, "

    if user_info.first_name:
        text_message += f"{user_info.first_name} "

    if user_info.last_name:
        text_message += f"{user_info.last_name} "

    if user_info.username:
        text_message += f"@{user_info.username}"

    context.bot.send_message(
        chat_id=TELEGRAM_SUPPORT_CHAT_ID,
        text=text_message
    )


# To be executed once the user sends ANY message to the bot
def forward_to_chat(update, context):
    update.message.forward(chat_id=TELEGRAM_SUPPORT_CHAT_ID)


# To be executed once once of the managers replies to the user message in a support chat
def forward_to_user(update, context):
    user_id = update.message.reply_to_message.forward_from.id
    context.bot.copy_message(
        message_id=update.message.message_id,
        chat_id=user_id,
        from_chat_id=update.message.chat_id
    )


# Setting up update handlers
def setup_dispatcher(dp):
    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(MessageHandler(Filters.chat_type.private, forward_to_chat))
    dp.add_handler(MessageHandler(Filters.chat(TELEGRAM_SUPPORT_CHAT_ID) & Filters.reply, forward_to_user))
    return dp
