from pyrogram import Client, filters

@Client.on_message(filters.command("setwelcome") & filters.group)
