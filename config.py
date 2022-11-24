from os import getenv as e

class API:
    API_ID = e("API_ID", None)
    API_HASH = e("API_HASH", None)

class TOKENS:
    BOT_TOKEN = e("BOT_TOKEN", None)

class DEV:
    SUDO_USERS = e("SUDO_USERS", None)

class DATABASE:
    MONGO_DB_URL = e("MONGO_DB_URL", None)

class STUFF:
    START_IMG = e("START_PIC", None)

class CHATS:
    SUPPORT_CHAT = e("SUPPORT_CHAT", "Spoiled_Community")
    LOG_GROUP_ID = int(e("LOG_GROUP_ID", None))
