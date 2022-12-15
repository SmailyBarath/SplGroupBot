from pyrogram import Client, filters
from Spoiled.Database.chats import *
from config import DEV
from pyrogram.errors import FloodWait
from pyrogram.types import Message
import asyncio

DEV_USERS = DEV.SUDO_USERS + [DEV.OWNER_ID]

@Client.on_message(filters.command("broadcast") & filters.user(DEV_USERS))
async def broadcast(_, message):
    if message.reply_to_message:
        x = message.reply_to_message.message_id
        y = message.chat.id
    else:
        if len(message.command) < 2:
            return await message.reply_text(
                "**Usage**:\n/broadcast [MESSAGE] or [Reply to a Message]"
            )
        query = message.text.split(None, 1)[1]
    sent = 0
    pinned = 0
    chats = []
    schats = await get_served_chats()
    for chat in schats:
        chats.append(int(chat["chat_id"]))
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
                    await _.pin_chat_message(i, ok.message_id)
                    pinned += 1
                except:
                    continue 
            else:
                ok = await _.send_message(i, query)
                sent += 1
                CASTED.append(i)
                try:
                    await _.pin_chat_message(i, ok.message_id)
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
    await m.reply(f"**Served chats** :-\n{msg}\n\n**Count** :- {len(chats)}")
