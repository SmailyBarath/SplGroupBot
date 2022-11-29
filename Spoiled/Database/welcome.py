from . import db

welcomedb = db.welcome

async def set_welcome(chat_id: int, msg_id: int):
    await welcomedb.update_one({"chat_id": chat_id}, {"$set": {"msg_id": msg_id}}, upsert=True)
