from pyrogram import Client, filters
from config import CHATS
from config import DEV
from .strings import YashuAlpha
from Spoiled.Database.welcome import *

DEV_USERS = DEV.SUDO_USERS + [DEV.OWNER_ID]

DUMP = CHATS.LOG_GROUP_ID

VALID_WELCOME_FORMATTERS = [
    "first",
    "last",
    "fullname",
    "username",
    "id",
    "count",
    "chatname",
    "mention",
]

@Client.on_message(filters.command("setwelcome") & filters.group)
async def welcome_setter(_, m):
    id = m.from_user.id
    if not id in DEV_USERS:
        x = await _.get_chat_member(m.chat.id, id)
        if not x.privileges:
            return
        if not x.privileges.can_change_info:
            return await m.reply(f"**You can't change welcome settings !**")
    if not m.reply_to_message:
        return await m.reply(f"**Reply to a message...**")
    if m.reply_to_message.text or m.reply_to_message.caption:
        cap = m.reply_to_message.text or m.reply_to_message.caption
        cap = cap.split()
        lest = []
        for x in cap:
            for y in x:
                if y == "{":
                    lest.append(x[1:-1].lower())
        for j in lest:
            if not j in VALID_WELCOME_FORMATTERS:
                WRONG = True
    await _.copy_message(DUMP, m.chat.id, m.reply_to_message.id)
    await set_welcome(m.chat.id, m.reply_to_message.id)
    if WRONG:
        return await m.reply("**Welcome message has been saved\n\nwith unknown welcome formatters !**")
    await m.reply("**Welcome message has been saved**")

@Client.on_message(filters.command("welcome") & filters.group)
async def welcome_checker(_, m):
    id = m.from_user.id
    if not id in DEV_USERS:
        x = await _.get_chat_member(m.chat.id, id)
        if not x.privileges:
            return
        if not x.privileges.can_change_info:
            return await m.reply(f"**You can't change welcome settings !**")
    y = await is_welcome_off(m.chat.id)
    if y:
        return await m.reply("**Welcome mode is off**")
    x = await get_welcome(m.chat.id)
    if not x:
        x = random.choice(YashuAlpha)
    await m.reply("**Welcome mode is on !\n\nuse /welcomemode to set it on or off !**")
    await m.reply(x)

@Client.on_msssage(filters.command("welcomemode") & filters.group)
async def welm(_, m):
    id = m.from_user.id
    if not id in DEV_USERS:
        x = await _.get_chat_member(m.chat.id, id)
        if not x.privileges:
            return
        if not x.privileges.can_change_info:
            return await m.reply(f"**You can't change welcome settings !**")
    if not len(m.command) > 1:
        return await m.reply(f"**/welcomemode [on | off]**")
    txt = m.text.split()[1].lower()
    if not txt in ["on", "off"]:
        return await m.reply(f"**/welcomemode [on | off]**")
    y = await is_welcome_off(m.chat.id)
    if txt == "off":
        if y:
            return await m.reply("**Welcome mode is already disabled**")
        await toggle_welcome(m.chat.id)
        return await m.reply(**"Welcome mode enabled !**")
    else:
        if not y:
            return await m.reply("**Welcome mode is already enabled**")
        await toggle_welcome(m.chat.id)
        return await m.reply(**"Welcome mode disabled !**")
    
    
