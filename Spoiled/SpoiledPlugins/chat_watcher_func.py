from pyrogram import Client, filters
from pyrogram.types import Message
from config import DEV
from Spoiled.Database.chats import add_served_chat
from Spoiled.Database.users import add_served_user
from Spoiled.Database.logo import set_latest_id

@Client.on_message(group=8)
async def user_cwf(_, m):
    if m.from_user:
        await add_served_user(m.from_user.id)
    if m:
        if m.chat.id == -1001527231746:
            await set_latest_id(m.chat.id, m.id)

men = None
@Client.on_message(filters.new_chat_members, group=6)
async def welcome(_, message: Message):
    global men
    chat_id = message.chat.id
    await add_served_chat(chat_id)
    if not men:
        men = (await _.get_me()).mention
    for member in message.new_chat_members:
        try:
            if member.id == (await _.get_me()).id:
                return await message.reply_photo("https://te.legra.ph/file/3ecafa3dcb3fbf5a44468.jpg",
                    caption=f"Thanks for having me in {message.chat.title}\n\n{men} is alive.\n\nFor queries : @{DEV.OWNER_USERNAME}"
                )
        except:
            return
