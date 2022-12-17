from . import db

logodb = db.logo

async def get_latest_id(chat_id):
    x = logodb.find({"chat_id": chat_id})
    if x:
        c = int(x["id"])
        return c

async def set_latest_id(chat_id, id):
    x = logodb.find({"chat_id": chat_id})
    if x:
        logodb.delete_one({"chat_id": chat_id})
    logodb.update_one({"chat_id": chat_id}, {"$set": {"id": id}}, upsert=True)
