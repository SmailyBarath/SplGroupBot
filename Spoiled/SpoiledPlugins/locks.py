from pyrogram import Client, filters
from config import DEV

DEV_USERS = DEV.SUDO_USERS + [DEV.OWNER_ID]

AVAILABLE = ["photo", "video", "doc", voice", "audio", "gif", "url"]

@Client.on_message(filters.command("lock"))
async def lock(_, m):
    if not m.from_user.id in DEV_USERS:
        x = await _.get_chat_member(m.chat.id, m.from_user.id)
        if not x.status in ["creator", "administrator"]:
            return await m.reply("Only admins are allowed to perform !")
    if not len(m.command) > 1:
        return await m.reply("`/lock` < locktype >")
    locktype = m.text.split()[1]
    if not locktype in AVAILABLE:
        return await m.reply("Undefined locktype, use `/locktypes` to know !")
    g = await is_lock(m.chat.id, locktype)
    if g:
        return await m.reply(f"**{locktype}s** already locked in {m.chat.title}")
    await add_lock(m.chat.id, locktype)
    await m.reply(f"**{locktype}s** are now locked in **{m.chat.title}**")

@Client.on_message(filters.command("unlock"))
async def unlock(_, m):
    if not m.from_user.id in DEV_USERS:
        x = await _.get_chat_member(m.chat.id, m.from_user.id)
        if not x.status in ["creator", "administrator"]:
            return await m.reply("Only admins are allowed to perform !")
    if not len(m.command) > 1:
        return await m.reply("`/unlock` < locktype >")
    locktype = m.text.split()[1]
    if not locktype in AVAILABLE:
        return await m.reply("Undefined locktype, use `/locktypes` to know !")
    g = await is_lock(m.chat.id, locktype)
    if not g:
        return await m.reply(f"**{locktype}s** aren't locked in {m.chat.title}")
    await del_lock(m.chat.id, locktype)
    await m.reply(f"**{locktype}s** are now unlocked in **{m.chat.title}**")

@Client.on_message(filters.command("locktypes"))
async def locktypes(_, m):
    if not m.from_user.id in DEV_USERS:
        x = await _.get_chat_member(m.chat.id, m.from_user.id)
        if not x.status in ["creator", "administrator"]:
            return await m.reply("Only admins are allowed to perform !")
    txt = "**Available locktypes**"
    txt += "\n\n"
    for z in AVAILABLE:
        txt += f"- {z}\n"
    await m.reply(txt)
