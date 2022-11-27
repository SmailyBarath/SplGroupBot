from pyrogram import Client, filters
from Spoiled.Database.approve import *
from . import get_id

@Client.on_message(filters.command("approve"))
async def approve_user(_, m):
    user_id = m.from_user.id
