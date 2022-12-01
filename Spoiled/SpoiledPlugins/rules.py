from pyrogram import Client, filters
from Spoiled.Database.rules import *
from config import DEV

DEV_USERS = DEV.SUDO_USERS + [DEV.OWNER_ID]

@Client.on_message(filters.command("setrules") & filters.group)
async def ruleset(_, m):
    id = m.from_user.id
    if not id in DEV_USERS:
        x = await _.get_chat_members(m.chat.id, id)
        if not x.privileges:
            return
        if not x.privileges.can_change_info:
            return await m.reply("**You can't change rules of this group !**")
     
