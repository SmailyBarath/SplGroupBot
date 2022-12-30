from pyrogram import Client, filters
from Spoiled.Database.hugs import *
import random

@Client.on_message(filters.command("hug"))
async def hugger(_, m):
    if m.reply_to_message:
        men1 = m.from_user.mention
        men2 = m.reply_to_message.from_user.mention
        cap = f"{men1} hugging {men2} ✨❤️ !"
    else:
        cap = None

    id = await get_latest_id(-1001607588458)
    num = []
    for i in range(1, id+1):
        num.append(i)
    mid = random.choice(num)
    x = await _.get_messages(-1001607588458, mid)
    while (not x.photo and not x.video and not x.animation) or x.caption != "#hug":
        mid = random.choice(num)
        x = await _.get_messages(-1001607588458, mid)
    if x.photo:
        return await m.reply_photo(x.photo.file_id, caption=cap if cap else "")
    elif x.animation:
        return await m.reply_animation(x.animation.file_id, caption=cap if cap else "")
    else:
        return await m.reply_video(x.video.file_id, caption=cap if cap else "")

@Client.on_message(filters.command("kiss"))
async def kisser(_, m):
    if m.reply_to_message:
        men1 = m.from_user.mention
        men2 = m.reply_to_message.from_user.mention
        cap = f"{men1} kissing {men2} ✨❤️ !"
    else:
        cap = None

    id = await get_latest_id(-1001607588458)
    num = []
    for i in range(1, id+1):
        num.append(i)
    mid = random.choice(num)
    x = await _.get_messages(-1001607588458, mid)
    while (not x.photo and not x.video and not x.animation) or x.caption != "#kiss":
        mid = random.choice(num)
        x = await _.get_messages(-1001607588458, mid)
    if x.photo:
        return await m.reply_photo(x.photo.file_id, caption=cap if cap else "")
    elif x.animation:
        return await m.reply_animation(x.animation.file_id, caption=cap if cap else "")
    else:
        return await m.reply_video(x.video.file_id, caption=cap if cap else "")

@Client.on_message(filters.channel)
async def channeler(_, m):
    if m:
        if m.chat.id == -1001607588458:
            await set_latest_id(m.chat.id, m.id)
