from telegram.ext import (
    Updater,
    CommandHandler,
    MessageHandler,
    Filters,
    ConversationHandler
)
from bot import (
    Config,
    INPUT_PHONE_NUMBER,
    INPUT_TG_CODE
)
from bot.modules.start_text_ import start
from bot.modules.my_telegram_org.input_phone_number_ import (
    input_phone_number
)
from bot.modules.my_telegram_org.input_tg_code_ import (
    input_tg_code
)


""" Initial Entry Point """
updater = Updater(Config.TG_BOT_TOKEN)

tg_bot_dis_patcher = updater.dispatcher

conv_handler = ConversationHandler(
    entry_points=[
        CommandHandler("start", start)
    ],

    states={
        INPUT_PHONE_NUMBER: [MessageHandler(
            Filters.text | Filters.contact,
            input_phone_number
        )],

        INPUT_TG_CODE: [MessageHandler(
            Filters.text,
            input_tg_code
        )],
    },

    fallbacks=[CommandHandler('start', start)]
)

tg_bot_dis_patcher.add_handler(conv_handler)

# Start the Bot
if Config.WEBHOOK:
    updater.start_webhook(
        listen="0.0.0.0",
        port=Config.PORT,
        url_path=Config.TG_BOT_TOKEN
    )
    updater.bot.set_webhook(
        url=Config.URL + Config.TG_BOT_TOKEN
    )
else:
    updater.start_polling()

print(
    """
Bot Started... 
    """
)

updater.idle()
