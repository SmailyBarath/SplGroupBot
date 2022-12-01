from pyrogram import Client, filters
from Spoiled.Database.rules import *
from config import DEV

DEV_USERS = DEV.SUDO_USERS + [DEV.OWNER_ID]

@Client.on_message(filters.command("setrules") & filters.group)
async def ruleset(_, m):
    id = m.from_user.id
    if not id in DEV_USERS:
        x = await _.get_chat_members(m.chat.id, id)
        if not x.privileges:
            return
        if not x.privileges.can_change_info:
            return await m.reply("**You can't change rules of this group !**")

    if not m.reply_to_message:
        if len(m.command) < 2:
            return await m.reply("**Either reply to a message or use /setrules rules !**")

    if m.reply_to_message:
        if not m.reply_to_message.text or not m.reply_to_message.caption:
            return await m.reply("**No text found in replied message !")
        txt = m.reply_to_message.text if m.reply_to_message.text else m.reply_to_message.caption
        await set_rules(m.chat.id, txt)
        return await m.reply(f"**Rules set for {m.chat.title}**")
    txt = m.text.split(None, 1)[1]
    await set_rules(m.chat.id, txt)
    return await m.reply(f"**Rules set for {m.chat.title}**")

@Client.on_message(filters.command("rules") & filters.group)
async def getr(_, m):
    x = await get_rules(m.chat.id)
    if not x:
        return await m.reply(f"**No rules in {m.chat.title}**")
    return await m.reply(x)

@Client.on_message(filters.command("clearrules") & filters.group)
async def clrr(_, m):
    id = m.from_user.id
    if not id in DEV_USERS:
        x = await _.get_chat_members(m.chat.id, id)
        if not x.privileges:
            return
        if not x.privileges.can_change_info:
            return await m.reply("**You can't change rules of this group !**")

    x = await get_rules(m.chat.id)
    if not x:
        return await m.reply(f"**No rules in {m.chat.title}**")
    await clear_rules(m.chat.id)
    await m.reply(f"**Rules cleared in {m.chat.title}**")

