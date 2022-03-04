from telegram import (
    Update,
    ParseMode
)
from telegram.ext import (
    ConversationHandler
)
from bot import (
    Config,
    GLOBAL_USERS_DICTIONARY,
    INPUT_PHONE_NUMBER
)
from bot.helper_funcs.helper_steps import (
    extract_code_imn_ges,
    parse_to_meaning_ful_text
)
from bot.helper_funcs.my_telegram_org.step_two import (
    login_step_get_stel_cookie
)
from bot.helper_funcs.my_telegram_org.step_three import scarp_tg_existing_app
from bot.helper_funcs.my_telegram_org.step_four import create_new_tg_app


def input_tg_code(update: Update, context):
    """ ConversationHandler INPUT_TG_CODE state """
    user = update.message.from_user
    current_user_creds = GLOBAL_USERS_DICTIONARY.get(user.id)
    aes_mesg_i = update.message.reply_text(Config.BEFORE_SUCC_LOGIN)
    provided_code = extract_code_imn_ges(update.message)
    if provided_code is None:
        aes_mesg_i.edit_text(
            text=Config.IN_VALID_CODE_PVDED,
            parse_mode=ParseMode.HTML
        )
        return INPUT_PHONE_NUMBER
    status_r, cookie_v = login_step_get_stel_cookie(
        current_user_creds.get("input_phone_number"),
        current_user_creds.get("random_hash"),
        provided_code
    )
    if status_r:
        status_t, response_dv = scarp_tg_existing_app(cookie_v)
        if not status_t:
            create_new_tg_app(
                cookie_v,
                response_dv.get("tg_app_hash"),
                Config.APP_TITLE,
                Config.APP_SHORT_NAME,
                Config.APP_URL,
                Config.APP_PLATFORM,
                Config.APP_DESCRIPTION
            )
        status_t, response_dv = scarp_tg_existing_app(cookie_v)
        if status_t:
            input_phone_number = current_user_creds.get("input_phone_number")
            me_t = parse_to_meaning_ful_text(
                input_phone_number,
                response_dv
            )
            me_t += "\n"
            GLOBAL_USERS_DICTIONARY.update({
                user.id: {
                    "input_phone_number": input_phone_number,
                    "stea": response_dv
                }
            })
            me_t += "\n"
            me_t += Config.FOOTER_TEXT
            aes_mesg_i.edit_text(
                text=me_t,
                parse_mode=ParseMode.HTML
            )
        else:
            aes_mesg_i.edit_text(Config.ERRED_PAGE)
    else:
        aes_mesg_i.edit_text(cookie_v)
    return ConversationHandler.END
