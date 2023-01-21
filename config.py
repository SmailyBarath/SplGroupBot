from os import getenv as e

class API:
    API_ID = e("API_ID", None)
    API_HASH = e("API_HASH", None)

class TOKENS:
    BOT_TOKEN = e("BOT_TOKEN", None)
    ARQ_API_KEY = e("ARQ_API_KEY", "XFTAWU-EYHTRK-NRAXYQ-IRCDQK-ARQ")

class DEV:
    SUDO_USERS = e("SUDO_USERS", 2030938170)
    OWNER_ID = e("OWNER_ID", 1666544436)
    OWNER_USERNAME = e("OWNER_USERNAME", "ImCrazy_Boy")

class DATABASE:
    MONGO_DB_URL = e("MONGO_DB_URL", "")
    SQL_DB_URL = e("SQL_DB_URL", None)

class STUFF:
    START_IMG = e("START_IMG", "https://telegra.ph/file/32ebcdcdf37b6959145d6.jpg")
    PING_IMG = e("PING_IMG", "https://telegra.ph/file/9984e5ee4e0f2536f13ac.jpg")

class CHATS:
    SUPPORT_CHAT = e("SUPPORT_CHAT", "Spoiled_Community")
    LOG_GROUP_ID = int(e("LOG_GROUP_ID", -1001643158613))
