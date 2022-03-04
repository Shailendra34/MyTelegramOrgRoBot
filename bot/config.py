import os
from dotenv import load_dotenv
from bot.translation import Translation

load_dotenv("config.env")

    MUST_JOIN = os.environ.get('MUST_JOIN', None)
    if MUST_JOIN.startswith("@"):
        MUST_JOIN = MUST_JOIN.replace("@", "")
else:
    MUST_JOIN = ""
    if MUST_JOIN.startswith("@"):
        MUST_JOIN = MUST_JOIN[1:]


class Config:
    WEBHOOK = bool(os.environ.get("WEBHOOK", False))
    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", None)
    URL = os.environ.get("URL", "")
    PORT = int(os.environ.get("PORT", 5000))
    CHUNK_SIZE = 10280
    APP_TITLE = os.environ.get("APP_TITLE", "")
    APP_SHORT_NAME = os.environ.get("APP_SHORT_NAME", "")
    APP_URL = os.environ.get("APP_URL", "")
    APP_PLATFORM = [
        "android",
        "ios",
        "wp",
        "bb",
        "desktop",
        "web",
        "ubp",
        "other"
    ]
    APP_DESCRIPTION = os.environ.get(
        "APP_DESCRIPTION",
        "created using @HeroOfficialBots"
    )
    
    FOOTER_TEXT = os.environ.get("FTEXT", "❤️ @SpEcHlDe")
    START_TEXT = os.environ.get("START_TEXT", Translation.START_TEXT)
    AFTER_RECVD_CODE_TEXT = os.environ.get(
        "AFTER_RECVD_CODE_TEXT",
        Translation.AFTER_RECVD_CODE_TEXT
    )
    BEFORE_SUCC_LOGIN = os.environ.get(
        "BEFORE_SUCC_LOGIN",
        Translation.BEFORE_SUCC_LOGIN
    )
    ERRED_PAGE = os.environ.get("ERRED_PAGE", Translation.ERRED_PAGE)
    CANCELLED_MESG = os.environ.get(
        "CANCELLED_MESG",
        Translation.CANCELLED_MESG
    )
    IN_VALID_CODE_PVDED = os.environ.get(
        "IN_VALID_CODE_PVDED",
        Translation.IN_VALID_CODE_PVDED
    )
    IN_VALID_PHNO_PVDED = os.environ.get(
        "IN_VALID_PHNO_PVDED",
        Translation.IN_VALID_PHNO_PVDED
    )
