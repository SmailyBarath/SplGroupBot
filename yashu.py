from pyrogram import Client, idle
from config import API, TOKENS

spoil = Client(":SPOILED-BOT:",
               api_id=API.API_ID,
               api_hash=API.API_HASH,
               bot_token=TOKENS.BOT_TOKEN,
               plugins=dict(root="Spoiled/SpoiledPlugins")
               )
