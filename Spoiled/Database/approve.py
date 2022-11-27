from . import db

appdb = db.approve

async def is_approved(chat_id: int, user_id: int):
    x = await appdb.find_one({"chat_id": chat_id})
    if not x:
        return False
    list = x["approved"]
    if user_id in list:
        return True
    return False

async def approve(chat_id: int, user_id: int):
    x = await appdb.find_one({"chat_id": chat_id})
    if x:
        list = x["approved"]
        list.append(user_id)
        return await appdb.update_one({"chat_id": chat_id}, {"$set": {"approved": list}}, upsert=True)
    list = [user_id]
    return await appdb.update_one({"chat_id": chat_id}, {"$set": {"approved": list}}, upsert=True)

async def disapprove(chat_id: int, user_id: int):
    x = await appdb.find_one({"chat_id": chat_id})
    if x:
        list = x["approved"]
        list.remove(user_id)
        return await appdb.update_one({"chat_id": chat_id}, {"$set": {"approved": list}}, upsert=True)

async def get_approved(chat_id):
    x = await appdb.find_one({"chat_id": chat_id})
    if not x:
        return []
    return x["approved"]
