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
    global IDS
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
            IDS = {}
            LIST = {chat_id: user_id}
            IDS = {m.id}
            a = 1
        x = await get_flood(m.chat.id)
        if a == x:
            men = (await _.get_users(user_id))
            txt = f"**{men} flooding...**"
            y = await get_flood_mode(m.chat.id)
            SET = []
            for j in IDS:
                SET.append(j)
            if y == "delete":
                try:
                    await _.delete_messages(m.chat.id, SET)
                    return await m.reply(txt)
                except:
                    return await m.reply(txt)
            elif y == "mute":
                try:
                    await _.restrict_chat_member(m.chat.id, user_id, permissions=ChatPermissions())
                    return await m.reply(txt + f"**\n\nmuted...**")
                except:
                    return await m.reply(txt)
            elif y == "ban":
                try:
                    await _.ban_chat_member(m.chat.id, user_id)
                    return await m.reply(txt + f"**\n\banned...**")
                except:
                    return await m.reply(txt)
            elif y == "tmute":
                try:
                    await _.restrict_chat_member(m.chat.id, user_id, ChatPermissions(), datetime.now()+timedelta(minutes=(await get_mute_time(chat_id))))
                    return await m.reply(txt + f"**\n\nmuted for {await get_mute_time(chat_id)}min..**")
                except:
                    return await m.reply(txt)
                    
    
