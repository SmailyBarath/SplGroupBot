# MODULE VERIFIED BY @NORTH_YANKTON

from pyrogram import Client, filters
from config import DEV, STUFF
import time
from .afk import get_readable_time
from . import startTime

DEV_USERS = DEV.SUDO_USERS + [DEV.OWNER_ID]

@Client.on_message(filters.command(["alive", "ping"]))
async def alive(_, m):
    start = time.time()
    ok = await m.reply("`Building Alive and Pinging..!`")
    myfn = (await _.get_me()).first_name
    txt = f"**Hi {m.from_user.first_name} !, I'm {myfn}**\n\n"
    txt += f"**Bot owner : [Barath](t.me/{DEV.OWNER_USERNAME})**\n\n"
    if DEV.SUDO_USERS:
        txt += f"**Sudo status : ✅ , {len(DEV.SUDO_USERS)}**\n\n"
    else:
        txt += f"**Sudo status : ❌**\n\n"
    txt += f"**Uptime : {get_readable_time(int(time.time()-startTime))}\n**"
    end = time.time()
    dur = (str(end-start))[0:5]
    await ok.delete()
    await m.reply_photo(STUFF.PING_IMG, caption=txt + "\n" + f"**Ping : {dur} Sec**")
