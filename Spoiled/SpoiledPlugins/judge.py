import random
from pyrogram import filters, Client as pbot

@pbot.on_message(filters.command("judge"))
async def judge(_, m):
    if not m.reply_to_message:
        return await m.reply("<code>You need to reply to someone.</code>")
    x = m.reply_to_message.from_user.mention
    y = [f"**is lying!**", f"**is telling the truth.**"]
    z = random.choice(y)
    return await m.reply(x + " " + z)
