from config import DEV
from pyrogram.types import Message
import time

chat_admins = {}

async def get_admins(chat_id):
    global chat_admins
    if chat_id in chat_admins:
        up_time = chat_admins[chat_id]["updated"]
        if time.time() - up_time > 600:
            admin_list = []
            async for member in _.iter_chat_members(m.chat.id, filter="administrators"):
                admin_list.append(member.user.id)
            chat_admins[chat_id]["admin_list"] = admin_list
            return admin_list
        else:
            return chat_admins[chat_id]["admin_list"]
    else:
        admin_list = []
        async for member in _.iter_chat_members(m.chat.id, filter="administrators"):
            admin_list.append(member.user.id)
        chat_admins[chat_id]["admin_list"] = admin_list
        return admin_list
