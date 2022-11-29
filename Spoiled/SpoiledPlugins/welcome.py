from pyrogram import Client, filters
from config import CHATS
from config import DEV

DEV_USERS = DEV.SUDO_USERS + [DEV.OWNER_ID]

DUMP = CHATS.MESSAGE_DUMP_CHAT

@Client.on_message(filters.command("setwelcome") & filters.group)
async def welcome_setter(_, m):
 
    
