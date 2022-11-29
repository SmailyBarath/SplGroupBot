"""from pyrogram import Client, filters
from config import CHATS
from config import DEV

DEV_USERS = DEV.SUDO_USERS + [DEV.OWNER_ID]

DUMP = CHATS.MESSAGE_DUMP_CHAT

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
        return await m.reply(
"""
