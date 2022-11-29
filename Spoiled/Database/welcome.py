from . import db

welcomedb = db.welcome

wdb = db.well

async def set_welcome(chat_id: int, msg_id: int):
    await welcomedb.update_one({"chat_id": chat_id}, {"$set": {"msg_id": msg_id}}, upsert=True)

async def get_welcome(chat_id: int):
    x = await welcomedb.find_one({"chat_id": chat_id})
    if not x:
        return None
    return x["msg_id"]

async def is_welcome_off(chat_id: int):
    x = await wdb.find_one({"chat_id": chat_id})
    if x:
        return True
    return False

async def toggle_welcome(chat_id: int):
    x = await wdb.find_one({"chat_id": chat_id})
    if x:
        return await wdb.delete_one({"chat_id": chat_id})
    return await wdb.insert_one({"chat_id": chat_id})
