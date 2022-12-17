from . import db

warndb = db.warn

async def warn_user(chat_id: int, user_id: int):
    x = await warndb.find_one({"chat_id": chat_id})
    if x:
        warns = x["warns"]
        if user_id in warns:
            warns[user_id] += 1
        else:
            warns[user_id] = 1
        return await warndb.update_one({"chat_id": chat_id}, {"$set": {"warns": {user_id: warns[user_id]}}}, upsert=True)
    else:
        warns = {"warns": {user_id: 1}}
        return await warndb.update_one({"chat_id": chat_id}, {"$set": warns}, upsert=True)
