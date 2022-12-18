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

async def Asynchorous():
    await spoil.start()
    try:
        await spoil.send_message(CHATS.LOG_GROUP_ID, "Bot started !")
    except:
        pass
    print("Bot started !")
    await Yashu.run_polling()

loop = asyncio.get_event_loop()
loop.run_until_complete(Asynchorous())
