from config import DEV
from pyrogram import Client, filters

@Client.on_message(filters.command(
async def ban_unban(_, m):
    user_id = m.from_user.id
    chat_id = m.chat.id
    
