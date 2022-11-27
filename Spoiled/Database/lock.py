from . import db

lockdb = db.lock

async def add_lock(chat_id: int, word):
    x = await lockdb.find_one({"chat_id": chat_id})
    if x:
        list = x["words"]
        list.append(word)
        return await lockdb.update_one({"chat_id": chat_id}, {"$set": {"words": list}}, upsert=True)
    else:
        list = [word]
        return await lockdb.update_one({"chat_id": chat_id}, {"$set": {"words": list}}, upsert=True)

async def del_lock(chat_id: int, word):
    x = await lockdb.find_one({"chat_id": chat_id})
    if x:
        list = x["words"]
        list.remove(word)
        return await lockdb.update_one({"chat_id": chat_id}, {"$set": {"words": list}}, upsert=True)

async def is_lock(chat_id: int, word):
    x = await lockdb.find_one({"chat_id": chat_id})
    if x:
        list = x["words"]
        if word in list:
            return True
        return False
    return False

async def get_locks(chat_id: int):
    x = await lockdb.find_one({"chat_id": chat_id})
    if not x:
        return []
    return x["words"]

async def clear_locks(chat_id: int):
    x = await get_locks(chat_id)
    if not x:
        return
    for c in x:
        await del_lock(chat_id, c)
