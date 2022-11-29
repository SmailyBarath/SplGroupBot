from . import db

flood_toggle_db = db.floods

fmdb = db.flood

fdb = flood_toggle_db

async def set_flood_value(chat_id: int, value):
    await fdb.update_one({"chat_id", chat_id}, {"$set": {"value": value}}, upsert=True)

async def set_flood_mode(chat_id: int, mode):
    await fmdb.update_one({"chat_id", chat_id}, {"$set": {"value": value}}, upsert=True)

async def get_flood(chat_id: int):
    x = await fdb.find_one({"chat_id": chat_id})
    if not x:
        return 0
    return x["value"]

async def get_flood_mode(chat_id: int):
    x = await fmdb.find_one({"chat_id": chat_id})
    if not x:
        return "delete"
    return x["mode"]

async def is_flood_on(chat_id: int) -> bool:
    chat = await flood_toggle_db.find_one({"chat_id": chat_id})
    if not chat:
        return False
    return True

async def flood_on(chat_id: int):
    is_flood = await is_flood_on(chat_id)
    if is_flood:
        return
    return await flood_toggle_db.insert_one({"chat_id": chat_id})


async def flood_off(chat_id: int):
    is_flood = await is_flood_on(chat_id)
    if not is_flood:
        return
    return await flood_toggle_db.delete_one({"chat_id": chat_id})
