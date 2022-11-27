from pyrogram import Client, filters
from Spoiled.Database.blacklist import *
from Spoiled.Database.approve import is_approved
from config import DEV
from pyrogram.types import InlineKeyboardButton as IKB, InlineKeyboardMarkup as IKM

DEV_USERS = [DEV.OWNER_ID] + DEV.SUDO_USERS

@Client.on_message(filters.command(["addblacklist", "addblocklist"]) & filters.group)
async def blacklist(_, m):
    if not m.from_user.id in DEV_USERS:
        x = await _.get_chat_member(m.chat.id, m.from_user.id)
        if not x.privileges:
            return await m.reply("Only admin can perform this action !")
    if not len(m.command) > 1:
        return await m.reply("`/addblacklist < word > `")
    word = m.text.split()[1].lower()
    check = await is_blacklist(m.chat.id, word)
    if check:
        return await m.reply(f"`{word}` is already blacklisted !")
    await add_blacklist(m.chat.id, word)
    await m.reply(f"`{word}` added to blacklist !")

@Client.on_message(filters.command(["rmblacklist", "rmblocklist"]) & filters.group)
async def rmblacklist(_, m):
    if not m.from_user.id in DEV_USERS:
        x = await _.get_chat_member(m.chat.id, m.from_user.id)
        if not x.privileges:
            return await m.reply("Only admin can perform this action !")
    if not len(m.command) > 1:
        return await m.reply("`/rmblacklist < word > `")
    word = m.text.split()[1].lower()
    check = await is_blacklist(m.chat.id, word)
    if not check:
        return await m.reply(f"`{word}` isn't blacklisted !")
    await del_blacklist(m.chat.id, word)
    await m.reply(f"`{word}` removed from blacklist !")
    
@Client.on_message(filters.command(["blacklist", "blocklist"]) & filters.group)
async def gbl(_, m):
    markup = IKM(
         [
         [
         IKB("Clear all 🗑️", callback_data="clear_all")
         ]
         ]
         )
    if not m.from_user.id in DEV_USERS:
        x = await _.get_chat_member(m.chat.id, m.from_user.id)
        if not x.privileges:
            return await m.reply("Only admin can perform this action !")
    li = await get_blacklist(m.chat.id)
    if not li:
        return await m.reply("blacklist is empty !")
    txt = f"**Words blacklist :** {m.chat.title}"
    txt += "\n\n"
    for h in li:
        txt += f"- `{h}`\n"
    await m.reply(txt, reply_markup=markup)

@Client.on_callback_query(filters.regex("clear_all"))
async def clear_cbq(_, q):
    id = q.from_user.id
    if not id in DEV_USERS:
        x = await _.get_chat_member(q.message.chat.id, id)
        if x.status != "creator":
            return await q.answer("Only owner can perform this action !", show_alert=True)
    await q.answer("clearing list !", show_alert=True)
    await clear_blacklist(q.message.chat.id)
    await q.edit_message_text("Blacklist cleared !")

@Client.on_message(group=3)
async def cwf(_, m):
    if m.from_user:
        if await is_approved(m.chat.id, m.from_user.id):
            return
        if m.from_user.id in DEV_USERS:
            return
        z = await _.get_chat_member(m.chat.id, m.from_user.id)
        if z.privileges:
            return
    if m.text or m.caption:
        txt = m.text.split() if m.text else m.caption.split()
        g = await get_blacklist(m.chat.id)
        for j in txt:
            if j.lower() in g:
                try:
                    await m.delete()
                except:
                    pass
            
