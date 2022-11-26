from . import db 

bldb = db.blacklist

async def add_blacklist(chat_id: int, word):
    x = await bldb.find_one({"chat_id": chat_id})
    if x:
        list = x["words"]
        list.append(word)
        return await bldb.update_one({"chat_id: chat_id}, {"$set": {"words": list}}, upsert=True)
    else:
        list = [word]
        return await bldb.update_one({"chat_id: chat_id}, {"$set": {"words": list}}, upsert=True)

async def del_blacklist(chat_id: int, word):
    x = await bldb.find_one({"chat_id": chat_id})
    if x:
        list = x["words"]
        list.remove(word)
        return await bldb.update_one({"chat_id: chat_id}, {"$set": {"words": list}}, upsert=True)

async def is_blacklist(chat_id: int, word):
    x = await bldb.find_one({"chat_id": chat_id})
    if x:
        list = x["words"]
        if word in list:
            return True
        return False
    return False

async def get_blacklist(chat_id: int):
    x = await bldb.find_one({"chat_id": chat_id})
    if not x:
        return []
    return x["words"]

async def clear_blacklist(chat_id: int):
    x = await get_blacklist(chat_id)
    if not x:
        return
    for c in x:
        await del_blacklist(chat_id, c)



