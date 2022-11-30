from . import db

filtersdb = db.filters

async def add_filter(chat_id: int, data):
    x = await filterdb.find_one({"chat_id" chat_id})
    if not x:
        await filterdb.update_one({"chat_id": chat_id}, {"$set": {"data": data}}, upsert=True)
    else:
        list = x["data"]
        list.append(data)
        await filterdb.update_one({"chat_id": chat_id}, {"$set": {"data": list}}, upsert=True)

async def is_filter(chat_id: int, name):
    x = await filterdb.find_one({"chat_id" chat_id})
    if not x:
        return False
    list = x["data"]
    for c in list:
        if c[0] == name:
            return True
    return False

async def list_filters(chat_id: int):
    x = await filterdb.find_one({"chat_id" chat_id})
    if not x:
        return []
    list = x["data"]
    lmao = []
    for c in list:
        lmao.append(c[0])
    return lmao

async def del_filter(chat_id: int, name):
    x = await filterdb.find_one({"chat_id" chat_id})
    if not x:
        return
    list = x["data"]
    for c in list:
        if c[0] == name:
            list.remove(c)
            return
    return

async def get_filter(chat_id: int, name):
    x = await filterdb.find_one({"chat_id" chat_id})
    if not x:
        return {}
    list = x["data"]
    for c in list:
        if c[0] == name:
            return c[1]
    return {}
