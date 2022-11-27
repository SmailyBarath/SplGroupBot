from pyrogram import filters, Client as spl
import random

@spl.on_message(filters.command(["coin", "toss"]))
async def toss(_, m):
    men = m.from_user.mention
    txt = "{} flipped a coin!\n\nIt's {}!"
    poss = ["heads", "tails"]
    fin = random.choice(poss)
    await m.reply(txt.format(men, fin))
