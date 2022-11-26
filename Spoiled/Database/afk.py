from . import db

afkdb = db.afk

async def is_afk(user_id: int):
    x = await afkdb.find_one({"user_id": user_id})
    if not x:
        return False, {}
    return True, x["details"]

async def add_afk(user_id: int, details):
    await afkdb.update_one({"user_id": user_id}, {"$set": {"details": details}}, upsert=True)

async def del_afk(user_id: int):
    await afkdb.delete_one({"user_id": user_id})

async def get_afk_users():
    x = afkdb.find({"user_id": {"$gt": 0}})
    if not x:
        return 0
    l = []
    for z in await x.to_list(length=1000000000):
        l.append(x["user_id"])
    return len(l)
