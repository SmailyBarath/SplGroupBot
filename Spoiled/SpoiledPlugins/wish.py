# MODULE VERIFIED BY @NORTH_YANKTON

import random
from pyrogram import filters, Client as pbot

@pbot.on_message(filters.command("wish"))
async def wish(_, m):
    try:
        txt = m.text.split(None, 1)[1]
    except:
        return await m.reply(f"""**You can use** `/wish` **as a general Wishing Well of sorts

For example:**
`/wish I could date you 😍`, `or
/wish that sushi was 🍣 in...`""")

    x = []
    for i in range(0, 101):
        x.append(i)
    y = random.choice(x)
    return await m.reply(f"""**Your wish has been cast. ✨**

<i>chance of success: {y}% </i>""")
