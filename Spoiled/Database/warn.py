from . import db

warndb = db.warn

async def warn_user(chat_id: int, user_id: int):
    user_id = str(user_id)
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

async def dwarn_user(chat_id: int, user_id: int):
    user_id = str(user_id)
    x = await warndb.find_one({"chat_id": chat_id})
    if not x:
        return
    warns = x["warns"]
    if not user_id in warns:
        return
    h = warns[user_id]
    if h == 0:
        return
    h -= 1
    return await warndb.update_one({"chat_id": chat_id}, {"$set": {"warns": {user_id: h}}}, upsert=True)

async def get_warns(chat_id: int, user_id: int):
    user_id = str(user_id)
    x = await warndb.find_one({"chat_id": chat_id})
    if not x:
        return 0
    warns = x["warns"]
    if not user_id in warns:
        return 0
    h = warns[user_id]
    return h
