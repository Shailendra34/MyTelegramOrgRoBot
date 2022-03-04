""" STEP FIVE """


from telegram import (
    Message
)


def parse_to_meaning_ful_text(input_phone_number: str, in_dict) -> str:
    """ convert the dictionary returned in STEP FOUR
    into Telegram HTML text """
    me_t = ""
    me_t += "<i>Phone Number</i>: "
    me_t += f"<u>{input_phone_number}</u>"
    me_t += "\n"
    me_t += "\n"
    me_t += "<i>App Configuration</i>"
    me_t += "\n"
    me_t += "<b>APP ID</b>: "
    me_t += "<code>{}</code>".format(in_dict["App Configuration"]["app_id"])
    me_t += "\n"
    me_t += "<b>API HASH</b>: "
    me_t += "<code>{}</code>".format(in_dict["App Configuration"]["api_hash"])
    me_t += "\n"
    me_t += "\n"
    me_t += "<i>Available MTProto Servers</i>"
    me_t += "\n"
    me_t += "<b>Production Configuration</b>: "
    me_t += "<code>{}</code> <u>{}</u>".format(
        in_dict["Available MTProto Servers"]["production_configuration"]["IP"],
        in_dict["Available MTProto Servers"]["production_configuration"]["DC"]
    )
    me_t += "\n"
    me_t += "<b>Test Configuration</b>: "
    me_t += "<code>{}</code> <u>{}</u>".format(
        in_dict["Available MTProto Servers"]["test_configuration"]["IP"],
        in_dict["Available MTProto Servers"]["test_configuration"]["DC"]
    )
    me_t += "\n"
    me_t += "\n"
    me_t += "<i>Disclaimer</i>: "
    me_t += "<u>{}</u>".format(
        in_dict["Disclaimer"]
    )
    return me_t


def extract_code_imn_ges(ptb_message: Message) -> str:
    """ extracts the input message, and returns the
    Telegram Web login code"""
    telegram_web_login_code = None
    incoming_message_text = ptb_message.text
    incoming_message_text_in_lower_case = incoming_message_text.lower()
    if "web login code" in incoming_message_text_in_lower_case:
        parted_message_pts = incoming_message_text.split("\n")
        if len(parted_message_pts) >= 2:
            telegram_web_login_code = parted_message_pts[1]
    elif "\n" in incoming_message_text_in_lower_case:
        telegram_web_login_code = None
    else:
        telegram_web_login_code = incoming_message_text
    return telegram_web_login_code


def get_phno_imn_ges(ptb_message: Message) -> str:
    """ gets the phone number (in international format),
    from the input message"""
    my_telegram_ph_no = None
    if ptb_message.text is not None:
        if len(ptb_message.entities) > 0:
            for c_entity in ptb_message.entities:
                if c_entity.type == "phone_number":
                    my_telegram_ph_no = ptb_message.text[
                        c_entity.offset:c_entity.length
                    ]
        else:
            my_telegram_ph_no = ptb_message.text
    elif ptb_message.contact is not None:
        if ptb_message.contact.phone_number != "":
            my_telegram_ph_no = ptb_message.contact.phone_number
    return my_telegram_ph_no
