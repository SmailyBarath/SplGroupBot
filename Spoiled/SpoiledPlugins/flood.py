from pyrogram import Client, filters
from Spoiled.Database.flood import *
from config import DEV

DEV_USERS = DEV.SUDO_USERS + [DEV.OWNER_ID]

@Client.on_message(filters.command("floodmode") & filters.group)
async def fm(_, m):
    id = m.from_user.id
    if not id in DEV_USERS:
        x = await _.get_chat_member(m.chat.id, id)
        if not x.privileges:
            return
    g = await get_flood_mode(m.chat.id)
    await m.reply(f"**FloodMode Action : {g}**")

@Client.on_message(filters.command("floodvalue") & filters.group)
async def flv(_, m):
    id = m.from_user.id
    if not id in DEV_USERS:
        x = await _.get_chat_member(m.chat.id, id)
        if not x.privileges:
            return
    g = await get_flood(m.chat.id)
    await m.reply(f"**Flood Limit : {g}**")

@Client.on_message(filters.command("setflood") & filters.group)
async def setfl(_, m):
    id = m.from_user.id
    if not id in DEV_USERS:
        x = await _.get_chat_member(m.chat.id, id)
        if not x.privileges:
            return
        if not x.privileges.can_change_info:
            return await m.reply(f"**You can't change flood settings !**")
    if len(m.command) > 1:
        val = int(m.text.split()[1])
    else:
        return await m.reply(f"**Give a value !**")
    await set_flood_value(m.chat.id, val)
    await m.reply(f"**Flood value set to {val}**")

@Client.on_message(filters.command("setfloodmode") & filters.group)
async def setflm(_, m):
    id = m.from_user.id
    if not id in DEV_USERS:
        x = await _.get_chat_member(m.chat.id, id)
        if not x.privileges:
            return
        if not x.privileges.can_change_info:
            return await m.reply(f"**You can't change flood settings !**")
    if len(m.command) > 1:
        val = str(m.text.split()[1]).lower()
    else:
        return await m.reply(f"**Choose from [delete, mute, ban]**")
    if not val in ["delete", "ban", "mute"]:
        return await m.reply(f"**Choose from [delete, mute, ban, tmute, kick]**")
    await set_flood_mode(m.chat.id, val)
    await m.reply(f"**Flood mode set to {val}**")

LIST = {}
IDS = {}
@Client.on_message(filters.group, group=9)
async def cwf(_, m):
    global LIST
    chat_id = m.chat.id
    if m.from_user:
        user_id = m.from_user.id
        if not chat_id in LIST:
            LIST = {chat_id: user_id}
            a = 1
            IDS = {m.id}
        if user_id in LIST[chat_id]:
            a += 1
            IDS.add(m.id)
        else:
            LIST = {}
            LIST = {chat_id: user_id}
            a = 1
        x = await get_flood(m.chat.id)
        if a == x:
    
