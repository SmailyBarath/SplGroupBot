from pyrogram import Client, filters
from Spoiled.Database.etc import *
import random

@Client.on_message(filters.command("pat"))
async def hugger(_, m):
    if m.reply_to_message:
        men1 = m.from_user.mention
        men2 = m.reply_to_message.from_user.mention
        cap = f"{men1} patting {men2} 💥 !"
    else:
        if len(m.command) > 1:
            men1 = m.from_user.mention
            txt = m.text.split()[1]
            try:
                men2 = (await _.get_users(txt)).mention
                cap = f"{men1} patting {men2} 💥 !"
            except:    
                cap = None
        else:
            cap = None

    id = await get_latest_id(-1001605629866)
    num = []
    for i in range(1, id+1):
        num.append(i)
    mid = random.choice(num)
    x = await _.get_messages(-1001605629866, mid)
    while (not x.photo and not x.video and not x.animation) or x.caption != "#pat":
        mid = random.choice(num)
        x = await _.get_messages(-1001605629866, mid)
    if x.photo:
        return await m.reply_photo(x.photo.file_id, caption=cap if cap else "")
    elif x.animation:
        return await m.reply_animation(x.animation.file_id, caption=cap if cap else "")
    else:
        return await m.reply_video(x.video.file_id, caption=cap if cap else "")

@Client.on_message(filters.command("bite"))
async def biter(_, m):
    if m.reply_to_message:
        men1 = m.from_user.mention
        men2 = m.reply_to_message.from_user.mention
        cap = f"{men1} biting {men2} 💥 !"
    else:
        if len(m.command) > 1:
            men1 = m.from_user.mention
            txt = m.text.split()[1]
            try:
                men2 = (await _.get_users(txt)).mention
                cap = f"{men1} biting {men2} 💥 !"
            except:    
                cap = None
        else:
            cap = None

    id = await get_latest_id(-1001605629866)
    num = []
    for i in range(1, id+1):
        num.append(i)
    mid = random.choice(num)
    x = await _.get_messages(-1001605629866, mid)
    while (not x.photo and not x.video and not x.animation) or x.caption != "#bite":
        mid = random.choice(num)
        x = await _.get_messages(-1001605629866, mid)
    if x.photo:
        return await m.reply_photo(x.photo.file_id, caption=cap if cap else "")
    elif x.animation:
        return await m.reply_animation(x.animation.file_id, caption=cap if cap else "")
    else:
        return await m.reply_video(x.video.file_id, caption=cap if cap else "")

@Client.on_message(filters.command("curse"))
async def curser(_, m):
    if m.reply_to_message:
        men1 = m.from_user.mention
        men2 = m.reply_to_message.from_user.mention
        cap = f"{men1} cursing {men2} 🤬 !"
    else:
        if len(m.command) > 1:
            men1 = m.from_user.mention
            txt = m.text.split()[1]
            try:
                men2 = (await _.get_users(txt)).mention
                cap = f"{men1} cursing {men2} 🤬 !"
            except:    
                cap = None
        else:
            cap = None

    id = await get_latest_id(-1001605629866)
    num = []
    for i in range(1, id+1):
        num.append(i)
    mid = random.choice(num)
    x = await _.get_messages(-1001605629866, mid)
    while (not x.photo and not x.video and not x.animation) or x.caption != "#curse":
        mid = random.choice(num)
        x = await _.get_messages(-1001605629866, mid)
    if x.photo:
        return await m.reply_photo(x.photo.file_id, caption=cap if cap else "")
    elif x.animation:
        return await m.reply_animation(x.animation.file_id, caption=cap if cap else "")
    else:
        return await m.reply_video(x.video.file_id, caption=cap if cap else "")


@Client.on_message(filters.command("thigh"))
async def thigher(_, m):
    if m.reply_to_message:
        men1 = m.from_user.mention
        men2 = m.reply_to_message.from_user.mention
        cap = f""
    else:
        if len(m.command) > 1:
            men1 = m.from_user.mention
            txt = m.text.split()[1]
            try:
                men2 = (await _.get_users(txt)).mention
                cap = f""
            except:    
                cap = None
        else:
            cap = None

    id = await get_latest_id(-1001605629866)
    num = []
    for i in range(1, id+1):
        num.append(i)
    mid = random.choice(num)
    x = await _.get_messages(-1001605629866, mid)
    while (not x.photo and not x.video and not x.animation) or x.caption != "#thigh":
        mid = random.choice(num)
        x = await _.get_messages(-1001605629866, mid)
    if x.photo:
        return await m.reply_photo(x.photo.file_id, caption=cap if cap else "")
    elif x.animation:
        return await m.reply_animation(x.animation.file_id, caption=cap if cap else "")
    else:
        return await m.reply_video(x.video.file_id, caption=cap if cap else "")

@Client.on_message(filters.command("bully"))
async def kisser(_, m):
    if m.reply_to_message:
        men1 = m.from_user.mention
        men2 = m.reply_to_message.from_user.mention
        cap = f"{men1} bullying {men2} 🤭 !"
    else:
        if len(m.command) > 1:
            men1 = m.from_user.mention
            txt = m.text.split()[1]
            try:
                men2 = (await _.get_users(txt)).mention
                cap = f"{men1} bullying {men2} 🤭 !"
            except:    
                cap = None
        else:
            cap = None

    id = await get_latest_id(-1001605629866)
    num = []
    for i in range(1, id+1):
        num.append(i)
    mid = random.choice(num)
    x = await _.get_messages(-1001605629866, mid)
    while (not x.photo and not x.video and not x.animation) or x.caption != "#bully":
        mid = random.choice(num)
        x = await _.get_messages(-1001605629866, mid)
    if x.photo:
        return await m.reply_photo(x.photo.file_id, caption=cap if cap else "")
    elif x.animation:
        return await m.reply_animation(x.animation.file_id, caption=cap if cap else "")
    else:
        return await m.reply_video(x.video.file_id, caption=cap if cap else "")

@Client.on_message(group=21)
async def channeler(_, m):
    if m:
        if m.chat.id == -1001605629866:
            await set_latest_id(m.chat.id, m.id)
