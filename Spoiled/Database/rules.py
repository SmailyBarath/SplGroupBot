from . import db

rulesdb = db.rules

async def set_rules(chat_id: int, rules):
    await rulesdb.update_one({"chat_id": chat_id}, {"$set": {"rules": rules}}, upsert=True)

async def get_rules(chat_id: int):
    x = await rulesdb.find_one({"chat_id": chat_id})
    if not x:
        return None
    return x["rules"]

async def clear_rules(chat_id: int):
    await rulesdb.delete_one({"chat_id": chat_id})
