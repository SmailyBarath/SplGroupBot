from pyrogram import Client, idle
from config import API, TOKENS, CHATS
from Spoiled import Yashu
#
spoil = Client(":SPOILED-BOT:",
               api_id=API.API_ID,
               api_hash=API.API_HASH,
               bot_token=TOKENS.BOT_TOKEN,
               plugins=dict(root="Spoiled/SpoiledPlugins")
               )

UN = "@Spl_levi_ackerman_bot"
def Asynchorous():
    global UN
    spoil.start()
    try:
        spoil.send_message(CHATS.LOG_GROUP_ID, "Bot started !")
    except:
        pass
    print("Bot started !")
    Yashu.run_polling()

Asynchorous()
