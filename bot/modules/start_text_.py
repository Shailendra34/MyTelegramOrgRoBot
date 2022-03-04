from telegram import (
    Update,
    ParseMode
)
from bot import Config, INPUT_PHONE_NUMBER


def start(update: Update, context):
    """ ConversationHandler entry_point /start """
    update.message.reply_text(
        Config.START_TEXT,
        parse_mode=ParseMode.HTML
    )
    return INPUT_PHONE_NUMBER
