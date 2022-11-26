# MODULE VERIFIED BY @NORTH_YANKTON

from pyrogram import Client, filters
from config import DEV, STUFF
import time

DEV_USERS = DEV.SUDO_USERS + [DEV.OWNER_ID]

@Client.on_message(filters.command(["alive", "ping"]) & filters.user(DEV_USERS))
async def alive(_, m):
    start = time.time()
    ok = await m.reply("`Building Alive and Pinging..!`")
    myfn = (await _.get_me()).first_name
    txt = f"**Hi {m.from_user.first_name} !, I'm {myfn}**\n"
    txt += f"**Bot owner : [Yashu-Alpha](t.me/{DEV.OWNER_USERNAME})**\n"
    if DEV.SUDO_USERS:
        txt += f"**Sudo status : ✅ , {len(DEV.SUDO_USERS)}**\n"
    else:
        txt += f"**Sudo status : ❌**\n"
    end = time.time()
    dur = (str(end-start))[0:5]
    await ok.delete()
    await m.reply_photo(STUFF.PING_IMG, caption=txt + "\n" + f"**Ping : {dur}s**")
