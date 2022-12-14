from pyrogram import Client, idle
from config import API, TOKENS
from Spoiled import Yashu
#
spoil = Client(":SPOILED-BOT:",
               api_id=API.API_ID,
               api_hash=API.API_HASH,
               bot_token=TOKENS.BOT_TOKEN,
               plugins=dict(root="Spoiled/SpoiledPlugins")
               )

def Asynchorous():
    spoil.start()
    print("Bot started !")
    Yashu.run_polling()

Asynchorous()
