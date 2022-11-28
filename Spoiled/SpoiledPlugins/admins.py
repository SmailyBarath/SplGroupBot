from pyrogram import Client, filters, enums
import time

admin_list = {}

async def list_admins(_, m):
    global admin_list
    chat_id = m.chat.id
    admins = admin_list[chat_id]["admins"]
    if not admins:
        l = reload_admins(_)
        admin_list[chat_id] = {"admins": l, "updated": time.time()}
        return l
    if (int(time.time()-admin_list[chat_id]["updated"])) >= 600:
        l = reload_admins(_)
        admin_list[chat_id] = {"admins": l, "updated": time.time()}
        return l

async def reload_admins(_: Client):
    l = []
    async for x in _.get_chat_members(chat_id, filter=enums.ChatMembersFilter.ADMINISTRATORS):
        l.append(x.user.id)
    return l

