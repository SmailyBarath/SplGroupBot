from . import db

logodb = db.logo

async def get_latest_id(chat_id):
    x = await logodb.find_one({"chat_id": chat_id})
    if x:
        c = int(x["id"])
        return c

async def set_latest_id(chat_id, id):
    x = await logodb.find_one({"chat_id": chat_id})
    if x:
        await logodb.delete_one({"chat_id": chat_id})
    await logodb.update_one({"chat_id": chat_id}, {"$set": {"id": id}}, upsert=True)
