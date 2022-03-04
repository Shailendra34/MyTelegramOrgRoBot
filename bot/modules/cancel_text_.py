from telegram import (
    Update
)
from bot import (
    Config,
    ConversationHandler
)


def cancel(update: Update, context):
    """ ConversationHandler /cancel state """
    update.message.reply_text(Config.CANCELLED_MESG)
    return ConversationHandler.END


def error(update: Update, context):
    """Log Errors caused by Updates."""
    print("Update %s caused error %s", update, context.error)
