from os import getenv as e

class API:
    API_ID = e("API_ID", None)
    API_HASH = e("API_HASH", None)

class TOKENS:
    BOT_TOKEN = e("BOT_TOKEN", None)
    ARQ_API_KEY = e("ARQ_API_KEY", "PNZJLN-ZZFHVK-USQLIZ-MQEWJN-ARQ")

class DEV:
    SUDO_USERS = e("SUDO_USERS", [5754821527])
    OWNER_ID = e("OWNER_ID", 5754821527)
    OWNER_USERNAME = e("OWNER_USERNAME", "@North_Yankton")

class DATABASE:
    MONGO_DB_URL = e("MONGO_DB_URL", None)
    SQL_DB_URL = e("SQL_DB_URL", None)

class STUFF:
    START_IMG = e("START_IMG", "https://te.legra.ph/file/3ecafa3dcb3fbf5a44468.jpg")
    PING_IMG = e("PING_IMG", "https://te.legra.ph/file/3ecafa3dcb3fbf5a44468.jpg")

class CHATS:
    SUPPORT_CHAT = e("SUPPORT_CHAT", "Spoiled_Community")
    LOG_GROUP_ID = int(e("LOG_GROUP_ID", None))
