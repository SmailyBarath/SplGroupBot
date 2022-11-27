from . import db

pusersdb = db.pusers


async def get_served_pusers() -> list:
    chats = pusersdb.find({"user_id": {"$gt": 0}})
    if not chats:
        return []
    chats_list = []
    for chat in await chats.to_list(length=1000000000):
        chats_list.append(chat["user_id"])
    return chats_list


async def is_served_puser(chat_id: int) -> bool:
    chat = await pusersdb.find_one({"user_id": chat_id})
    if not chat:
        return False
    return True


async def add_served_puser(chat_id: int):
    is_served = await is_served_puser(chat_id)
    if is_served:
        return
    return await pusersdb.insert_one({"user_id": chat_id})


async def remove_served_puser(chat_id: int):
    is_served = await is_served_puser(chat_id)
    if not is_served:
        return
    return await pusersdb.delete_one({"user_id": chat_id})
