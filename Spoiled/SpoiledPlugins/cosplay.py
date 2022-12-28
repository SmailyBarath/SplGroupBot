import requests
from pyrogram import Client, filters

@Client.on_message(filters.command("cosplay"))
async def waifu(_, m):
  r = requests.get("https://waifu-api.vercel.app").json() 
  await m.reply_photo(r)
  
@Client.on_message(filters.command("lewd"))
async def ewaifu(_, m):
  r = requests.get("https://waifu-api.vercel.app/items/1").json()
  await m.reply_photo(r)
