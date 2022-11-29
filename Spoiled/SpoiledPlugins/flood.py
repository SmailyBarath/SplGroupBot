"""from pyrogram import Client, filters
from Spoiled.Database.flood import *
from config import DEV
from pyrogram.types import InlineKeyboardButton as IKB, InlineKeyboardMarkup as IKM

DEV_USERS = DEV.SUDO_USERS + [DEV.OWNER_ID]

@Client.on_callback_query(filters.regex("toggle_flood") | filters.regex("det_flood") | filters.regex("close_flood"))
async def cbq(_, q):
    id = q.from_user.id
    if not id in DEV_USERS:
        x = await _.get_chat_member(q.message.chat.id, id)
        if not x.privileges:
            return
        if not x.privileges.can_change_info:
            return await q.answer(f"**You can't change flood settings !**", show_alert=True)
    if q.data == "toggle_flood":
        x = await is_flood_on(q.message.chat.id)
        if x:
            await q.answer("Turning flood off...")
            await flood_off(q.message.chat.id)
        else:
            await q.answer("Turning flood on...")
            await flood_on(q.message.chat.id)
        x = await is_flood_on(q.message.chat.id)
        if x:
            y = "Enabled ✅"
        else:
            y = "Disabled ❌"
        markup = IKM(
             [
             [
             IKB("Flood mode", callback_data="det_flood"),
             IKB("{}".format(y), callback_data="toggle_flood")
             ],
             [
             IKB("Close 🗑️", callback_data="close_flood")
             ]
             ]
             )
        await q.edit_message_reply_markup(reply_markup=markup)  
    elif q.data == "det_flood":
        await q.answer("Click on button beside to toggle flood settings !", show_alert=True)
    elif q.data == "close_flood":  
        await q.answer()
        await q.message.delete()

@Client.on_message(filters.command(["flood", "floods"]) & filters.group)
async def flooooods(_, m):
    id = m.from_user.id
    if not id in DEV_USERS:
        x = await _.get_chat_member(m.chat.id, id)
        if not x.privileges:
            return
        if not x.privileges.can_change_info:
            return await m.reply(f"**You can't change flood settings !**")
    x = await is_flood_on(m.chat.id)
    if x:
        y = "Enabled ✅"
    else:
        y = "Disabled ❌"
    markup = IKM(
             [
             [
             IKB("Flood mode", callback_data="det_flood"),
             IKB("{}".format(y), callback_data="toggle_flood")
             ],
             [
             IKB("Close 🗑️", callback_data="close_flood")
             ]
             ]
             )    
    await m.reply(f"**⚙️ Flood settings in {m.chat.title}\n\n• Group id : {m.chat.id}**", reply_markup=markup)
    

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
        return await m.reply(f"**Choose from [delete, mute, ban, tmute, kick]**")
    if not val in ["delete", "ban", "mute", "tmute", "kick"]:
        return await m.reply(f"**Choose from [delete, mute, ban, tmute, kick]**")
    if val == "tmute":
        try:
            tim = int(m.text.split()[2])
            if tim < 0:
                return await m.reply("😒😒..")
            await set_mute_time(m.chat.id, tim)
        except:
            return await m.reply(f"**Give a value which will be considered in minutes !**")
    await set_flood_mode(m.chat.id, val)
    await m.reply(f"**Flood mode set to {val}**")

LIST = {}
IDS = {}
a = 0
@Client.on_message(filters.group, group=9)
async def cwf(_, m):
    global a
    global LIST
    global IDS
    on = await is_flood_on(m.chat.id)
    if not on:
        return
    chat_id = m.chat.id
    if m.from_user:
        user_id = m.from_user.id
        if not chat_id in LIST:
            LIST = {chat_id: user_id}
            a = 1
            IDS = {chat_id: [m.id]}
        if LIST[chat_id] == user_id:
            a += 1
            IDS[chat_id].append(m.id)
        else:
            LIST.pop(chat_id)
            IDS[chat_id].clear()
            LIST[chat_id] = user_id
            IDS[chat_id].append(m.id)
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
"""                  
    
