from os import getenv as e

class API:
    API_ID = e("API_ID", 10763476)
    API_HASH = e("API_HASH", "e7d6d5493a896264a09d04fda7a30f9d")

class TOKENS:
    BOT_TOKEN = e("BOT_TOKEN", "5878056492:AAGCL9aAQPIqmDhkLWZf3bOYt8UdmS8qe7Q")
    ARQ_API_KEY = e("ARQ_API_KEY", "PNZJLN-ZZFHVK-USQLIZ-MQEWJN-ARQ")

class DEV:
    SUDO_USERS = e("SUDO_USERS", [5868832590])
    OWNER_ID = e("OWNER_ID", 5868832590)
    OWNER_USERNAME = e("OWNER_USERNAME", "ShutupKeshav")

class DATABASE:
    MONGO_DB_URL = e("MONGO_DB_URL", "mongodb+srv://musicbot:<password>@cluster0.61lydz4.mongodb.net/?retryWrites=true&w=majority")
    SQL_DB_URL = e("SQL_DB_URL", None)

class STUFF:
    START_IMG = e("START_IMG", "https://te.legra.ph/file/3ecafa3dcb3fbf5a44468.jpg")
    PING_IMG = e("PING_IMG", "https://te.legra.ph/file/3ecafa3dcb3fbf5a44468.jpg")

class CHATS:
    SUPPORT_CHAT = e("SUPPORT_CHAT", "Spoiled_Community")
    LOG_GROUP_ID = int(e("LOG_GROUP_ID", -1001643158613))
