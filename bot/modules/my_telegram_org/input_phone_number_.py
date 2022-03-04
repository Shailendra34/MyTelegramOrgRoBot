from telegram import (
    Update,
    ParseMode
)
from bot import (
    Config,
    GLOBAL_USERS_DICTIONARY,
    INPUT_PHONE_NUMBER,
    INPUT_TG_CODE
)
from bot.helper_funcs.helper_steps import (
    get_phno_imn_ges
)
from bot.helper_funcs.my_telegram_org.step_one import (
    request_tg_code_get_random_hash
)


def input_phone_number(update: Update, context):
    """ ConversationHandler INPUT_PHONE_NUMBER state """
    user = update.message.from_user
    input_text = get_phno_imn_ges(update.message)
    if input_text is None:
        update.message.reply_text(
            text=Config.IN_VALID_PHNO_PVDED,
            parse_mode=ParseMode.HTML
        )
        return INPUT_PHONE_NUMBER
    random_hash = request_tg_code_get_random_hash(input_text)
    GLOBAL_USERS_DICTIONARY.update({
        user.id: {
            "input_phone_number": input_text,
            "random_hash": random_hash
        }
    })
    update.message.reply_text(
        Config.AFTER_RECVD_CODE_TEXT,
        parse_mode=ParseMode.HTML
    )
    return INPUT_TG_CODE
