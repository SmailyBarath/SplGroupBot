from pyrogram import Client, filters, enums
from config import DEV
from Spoiled.Database.lock import *
from pyrogram.types import InlineKeyboardButton as IKB, InlineKeyboardMarkup as IKM

DEV_USERS = DEV.SUDO_USERS + [DEV.OWNER_ID]

AVAILABLE = ["photo", "video", "document", "voice", "audio", "gif", "url", "sticker"]

ASYNC = None

@Client.on_message(filters.command("lock") & filters.group)
async def lock(_, m):
    global ASYNC
    if not m.from_user.id in DEV_USERS:
        x = await _.get_chat_member(m.chat.id, m.from_user.id)
        if not x.status in ["creator", "administrator"]:
            return await m.reply("Only admins are allowed to perform !")
    if not len(m.command) > 1:
        return await m.reply("`/lock` < locktype >")
    locktype = m.text.split()[1].lower()
    if not locktype in AVAILABLE:
        return await m.reply("Undefined locktype, use `/locktypes` to know !")
    g = await is_lock(m.chat.id, locktype)
    if g:
        return await m.reply(f"**{locktype}s** already locked in {m.chat.title}")
    await add_lock(m.chat.id, locktype)
    await m.reply(f"**{locktype}s** are now locked in **{m.chat.title}**")
    ASYNC = True

@Client.on_message(filters.command("unlock") & filters.group)
async def unlock(_, m):
    global ASYNC
    if not m.from_user.id in DEV_USERS:
        x = await _.get_chat_member(m.chat.id, m.from_user.id)
        if not x.status in ["creator", "administrator"]:
            return await m.reply("Only admins are allowed to perform !")
    if not len(m.command) > 1:
        return await m.reply("`/unlock` < locktype >")
    locktype = m.text.split()[1].lower()
    if not locktype in AVAILABLE:
        return await m.reply("Undefined locktype, use `/locktypes` to know !")
    g = await is_lock(m.chat.id, locktype)
    if not g:
        return await m.reply(f"**{locktype}s** aren't locked in {m.chat.title}")
    await del_lock(m.chat.id, locktype)
    await m.reply(f"**{locktype}s** are now unlocked in **{m.chat.title}**")
    ASYNC = True

@Client.on_message(filters.command("locktypes"))
async def locktypes(_, m):
    if not m.from_user.id in DEV_USERS:
        x = await _.get_chat_member(m.chat.id, m.from_user.id)
        if not x.status in ["creator", "administrator"]:
            return await m.reply("Only admins are allowed to perform !")
    txt = "**Available locktypes**"
    txt += "\n\n"
    for z in AVAILABLE:
        txt += f"- `{z}`\n"
    await m.reply(txt)

markup = IKM(
         [
         [
         IKB("Clear 🗑️", callback_data="clear_locks")
         ]
         ]
         )

@Client.on_message(filters.command("locks") & filters.group)
async def locks(_, m):
    if not m.from_user.id in DEV_USERS:
        x = await _.get_chat_member(m.chat.id, m.from_user.id)
        if not x.status in ["creator", "administrator"]:
            return await m.reply("Only admins are allowed to perform !")
    d = await get_locks(m.chat.id)
    if not d:
        return await m.reply(f"Nothing locked in **{m.chat.title}**")
    txt = f"**Locks in {m.chat.title}**"
    txt += "\n\n"
    for j in d:
        txt += f"- `{j}`\n"
    return await m.reply(txt, reply_markup=markup)

@Client.on_callback_query(filters.regex("clear_locks"))
async def lock_cbq(_, q):
    global ASYNC
    id = q.from_user.id
    if not id in DEV_USERS:
        x = await _.get_chat_member(q.message.chat.id, id)
        if x.status != "creator":
            return await q.answer("Only creator can clear all at once !", show_alert=True)
    await q.answer("Clearing locks !")
    await clear_locks(q.message.chat.id)
    await q.edit_message_text("Cleared all locks !")
    ASYNC = True

LOCKS = []
admins = []
@Client.on_message(group=4)
async def cwf(_, m):
    global admins
    if not admins:
        async for z in _.get_chat_members(m.chat.id, filter=enums.ChatMembersFilter.ADMINISTRATORS):
            if not z.user.is_bot and not z.user.is_deleted:
                admins.append(z.user.id)
    if m.from_user.id in (DEV_USERS + admins):
        return
    global LOCKS
    global ASYNC
    if not LOCKS:
        LOCKS = await get_locks(m.chat.id)
    if ASYNC:
        LOCKS = await get_locks(m.chat.id)
        ASYNC = False
    if not LOCKS:
        return

    if m.photo:
        if "photo" in LOCKS:
            try:
                await m.delete()
            except:
                pass
        return

    if m.video:
        if "video" in LOCKS:
            try:
                await m.delete()
            except:
                pass
        return

    if m.audio:
        if "audio" in LOCKS:
            try:
                await m.delete()
            except:
                pass
        return

    if m.voice:
        if "voice" in LOCKS:
            try:
                await m.delete()
            except:
                pass
        return

    if m.document:
        if "document" in LOCKS:
            try:
                await m.delete()
            except:
                pass
        return

    if m.animation:
        if "gif" in LOCKS:
            try:
                await m.delete()
            except:
                pass
        return

    if m.sticker:
        if "sticker" in LOCKS:
            try:
                await m.delete()
            except:
                pass
        return

    if m.text or m.caption:
        if "url" in LOCKS:
            txt = m.text.split() if m.text else m.caption.split()
            for z in txt:
                for t in z:
                    if t == ".":
                        ind = z.index(".")
                        l = len(z)
                        if ind == 0 or ind == l - 1:
                            return
                        try:
                            await m.delete()
                        except:
                            pass
        return
    
    
    
    
