from . import db

filtersdb = db.filters

async def del_all_filters(chat_id: int):
    x = await filtersdb.find_one({"chat_id": chat_id})
    if not x:
        return
    x = await list_filters(chat_id)
    if not x:
        return
    for y in x:
        await del_filter(chat_id, y)

async def add_filter(chat_id: int, data):
    x = await filtersdb.find_one({"chat_id": chat_id})
    if not x:
        await filtersdb.update_one({"chat_id": chat_id}, {"$set": {"data": data}}, upsert=True)
    else:
        list = x["data"]
        list.append(data)
        await filtersdb.update_one({"chat_id": chat_id}, {"$set": {"data": list}}, upsert=True)

async def is_filter(chat_id: int, name):
    x = await filtersdb.find_one({"chat_id": chat_id})
    if not x:
        return False
    list = x["data"]
    for c in list:
        if c[0] == name:
            return True
    return False

async def list_filters(chat_id: int):
    x = await filtersdb.find_one({"chat_id": chat_id})
    if not x:
        return []
    if "data" in x:
        list = x["data"]
    else:
        return []
    lmao = []
    for c in list:
        lmao.append(c[0])
    return lmao

async def del_filter(chat_id: int, name):
    x = await filtersdb.find_one({"chat_id": chat_id})
    if not x:
        return
    list = x["data"]
    for c in list:
        if c[0] == name:
            list.remove(c)
            return
    return

async def get_filter(chat_id: int, name):
    x = await filtersdb.find_one({"chat_id": chat_id})
    if not x:
        return {}
    list = x["data"]
    for c in list:
        if c[0] == name:
            return c[1]
    return {}
