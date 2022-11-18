from config import DEV
from pyrogram.types import Message
import time

chat_admins = {}

async def get_admins(chat_id):
    global chat_admins
    if chat_id in chat_admins:
        up_time = chat_admins[chat_id]["updated"]
        
