from pyrogram import Client, filters
from config import CHATS
from config import DEV
from .strings import YashuAlpha
from Spoiled.Database.welcome import *
import random

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

@Client.on_message(filters.group & filters.new_chat_members, group=10)
async def cwf(_, m):
    x = await is_welcome_off(m.chat.id)
    if x:
        return
    x = await get_welcome(m.chat.id)
    if not x:
        x = random.choice(YashuAlpha)
        if "{first}" in x.split():
            h = m.new_chat_members[0].first_name
            x = x.replace("{first}", h)
        return await m.reply(x)
    msg = await _.get_messages(DUMP, x)
    if not msg:
        x = random.choice(YashuAlpha)
        if "{first}" in x.split():
            h = m.new_chat_members[0].first_name
            x.replace("{first}", h)
        return await m.reply(x)
    if msg.media:
        txt = msg.caption if msg.caption else None
        if txt:
            if "{first}" in txt:
                h = m.new_chat_members[0].first_name
                txt = txt.replace("{first}", h)
            if "{last}" in txt:
                h = m.new_chat_members[0].last_name if m.new_chat_members[0].last_name else None
                txt = txt.replace("{last}", h)
            if "{fullname}" in txt:
                h = m.new_chat_members[0].first_name
                o = m.new_chat_members[0].last_name if m.new_chat_members[0].last_name else None
                if o:
                    txt = txt.replace("{fullname}", h+o)
                else:
                    txt = txt.replace("{fullname}", h)
            if "{username}" in txt:
                h = m.new_chat_members[0].username if m.new_chat_members[0].username else None
                h = "@" + h
                txt = txt.replace("{username}", h)
            if "{id}" in txt:
                h = m.new_chat_members[0].id
                h = f"`{h}`"
                txt = txt.replace("{id}", h)
            if "{count}" in txt:
                h = await _.get_chat_members_count(m.chat.id)
                h = f"**{h}**"
                txt = txt.replace("{count}", str(h))
            if "{chatname}" in txt:
                h = m.chat.title
                h = f"**{h}**"
                txt = txt.replace("{chatname}", h)
            if "{mention}" in txt:
                h = m.new_chat_members[0].mention
                txt = txt.replace("{mention}", h)
            
        if msg.photo:
            return await m.reply_photo(msg.photo.file_id, caption=txt if txt else None)
        if msg.video:
            return await m.reply_video(msg.video.file_id, caption=txt if txt else None)
        if msg.animation:
            return await m.reply_animation(msg.animation.file_id, caption=txt if txt else None)
        if msg.audio:
            return await m.reply_audio(msg.audio.file_id, caption=txt if txt else None)
        if msg.document:
            return await m.reply_document(msg.document.file_id, caption=txt if txt else None, force_document=True)
        if msg.sticker:
            return await m.reply_sticker(msg.sticker.file_id)

    elif msg.text:
        txt = msg.text if msg.text else None
        if txt:
            if "{first}" in txt:
                h = m.new_chat_members[0].first_name
                txt = txt.replace("{first}", h)
            if "{last}" in txt:
                h = m.new_chat_members[0].last_name if m.new_chat_members[0].last_name else None
                txt = txt.replace("{last}", h)
            if "{fullname}" in txt:
                h = m.new_chat_members[0].first_name
                o = m.new_chat_members[0].last_name if m.new_chat_members[0].last_name else None
                if o:
                    txt = txt.replace("{fullname}", h+o)
                else:
                    txt = txt.replace("{fullname}", h)
            if "{username}" in txt:
                h = m.new_chat_members[0].username if m.new_chat_members[0].username else None
                h = "@" + h
                txt = txt.replace("{username}", h)
            if "{id}" in txt:
                h = m.new_chat_members[0].id
                h = f"`{h}`"
                txt = txt.replace("{id}", h)
            if "{count}" in txt:
                h = await _.get_chat_members_count(m.chat.id)
                h = f"**{h}**"
                txt = txt.replace("{count}", str(h))
            if "{chatname}" in txt:
                h = m.chat.title
                h = f"**{h}**"
                txt = txt.replace("{chatname}", h)
            if "{mention}" in txt:
                h = m.new_chat_members[0].mention
                txt = txt.replace("{mention}", h)
        
        return await m.reply(txt)



    

@Client.on_message(filters.command("clearwelcome") & filters.group)
async def welcomclr(_, m):
    id = m.from_user.id
    if not id in DEV_USERS:
        x = await _.get_chat_member(m.chat.id, id)
        if not x.privileges:
            return
        if not x.privileges.can_change_info:
            return await m.reply(f"**You can't change welcome settings !**")
    await clear_welcome(m.chat.id)
    await m.reply("**Welcome messages cleared !**")

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
    WRONG = False
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
    frwd = await _.copy_message(DUMP, m.chat.id, m.reply_to_message.id)
    await set_welcome(m.chat.id, frwd.id)
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
    else:
        x = await _.get_messages(DUMP, x)
        await m.reply("**Welcome mode is on !\n\nuse /welcomemode to set it on or off !**")
        if x.media:
            if x.photo:
                return await m.reply_photo(x.photo.file_id, caption=x.caption if x.caption else None)
            if x.video:
                return await m.reply_video(x.video.file_id, caption=x.caption if x.caption else None)
            if x.audio:
                return await m.reply_audio(x.audio.file_id, caption=x.caption if x.caption else None)
            if x.document:
                return await m.reply_document(x.document.file_id, caption=x.caption if x.caption else None, force_document=True)
            if x.animation:
                return await m.reply_animation(x.animation.file_id, caption=x.caption if x.caption else None)
            if x.sticker:
                return await m.reply_sticker(x.sticker.file_id)
        elif x.text:
            return await m.reply(x.text)


        

@Client.on_message(filters.command("welcomemode") & filters.group)
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
        return await m.reply("**Welcome mode disabled !**")
    
    
