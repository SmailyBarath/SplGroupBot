from pyrogram import Client, filters
from config import DEV

@Client.on_message(filters.new_chat_members, group=6)
async def welcome(_, message: Message):
    chat_id = message.chat.id
    await add_served_chat(chat_id)
    men = (await _.get_me()).mention
    for member in message.new_chat_members:
        try:
            if member.id == (await _.get_me()).id:
                return await message.reply_photo("https://te.legra.ph/file/3ecafa3dcb3fbf5a44468.jpg",
                    caption=f"Thanks for having me in {message.chat.title}\n\n{men} is alive.\n\nFor queries : @{DEV.OWNER_USERNAME}"
                )
        except:
            return
