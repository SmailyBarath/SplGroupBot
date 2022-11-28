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

@Client.on_message(filters.command("reload"))
async def reload(_, m):
    ok = await m.reply("Reloading bot...\n\n--loading\n l-- ⏳\n l-- ⏳")
    x = await reload_admins(_)
    await ok.edit("Reloading bot...\n\n--loading\n l-- Admin list updated ✅\n l-- ⏳")
    x = (await _.get_me()).id
    x = await _.get_chat_member(m.chat.id, x)
    x = x.privileges
    if not x.can_restrict_members:
        txt = "No ban rights ❌"
    else:
        txt = "Bot can ban ✅"
    await ok.edit(f"Reloading bot...\n\n--loaded\n l-- Admin list updated ✅\n l-- {txt}")
    
