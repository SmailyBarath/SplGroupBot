from pyrogram import Client, filters, enums
import time

admin_list = {}
tm = None

async def list_admins(_, m):
    global admin_list
    global tm
    chat_id = m.chat.id
    if not chat_id in admin_list:
        l = []
        async for x in _.get_chat_members(chat_id, filter=enums.ChatMembersFilter.ADMINISTRATORS):
            l.append(x.user.id)
        admin_list = {chat_id: l}
        tm = time.time()
        return l
    if (time.time()-tm) > 600:
        l = []
        admin_list[chat_id] = []
        async for x in _.get_chat_members(chat_id, filter=enums.ChatMembersFilter.ADMINISTRATORS):
            l.append(x.user.id)
        admin_list = {chat_id: l}
        tm = time.time()
        return l
    if RELOAD:
        l = []
        admin_list[chat_id] = []
        async for x in _.get_chat_members(chat_id, filter=enums.ChatMembersFilter.ADMINISTRATORS):
            l.append(x.user.id)
        admin_list = {chat_id: l}
        tm = time.time()
        return l

async def sender_admin(_, m):
    x = await _.get_chat_member(m.chat.id, m.from_user.id)
    if not x:
        return False
    if x.privileges:
        return True
    return False
