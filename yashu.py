from pyrogram import Client, idle
from config import API, TOKENS, CHATS
from Spoiled import Yashu
import asyncio

spoil = Client(":SPOILED-BOT:",
               api_id=API.API_ID,
               api_hash=API.API_HASH,
               bot_token=TOKENS.BOT_TOKEN,
               plugins=dict(root="Spoiled/SpoiledPlugins")
               )

def Asynchorous():
    spoil.start()
    try:
        spoil.send_message(CHATS.LOG_GROUP_ID, "Bot started !")
    except:
        pass
    print("Bot started !")
    Yashu.run_polling()
    idle()

Asynchorous()
