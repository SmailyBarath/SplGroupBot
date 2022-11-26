from pyrogram import Client, filters
from Spoiled.Database.afk import *
import time

@Client.on_message(filters.command("afk") | filters.command("brb", ""))
async def afk(_, m):
    user_id = m.from_user.id
    first_name = m.from_user.first_name
    await m.reply(f"**{first_name}** is not AFK")
    reason = m.text.split(None, 1)[1] if len(m.command) > 1 else None
    start = time.time()
    details = {"reason": reason, "time": start}
    await add_afk(user_id, details)

B_UN = None

@Client.on_message(group=1):
async def cwf(_, m):
    global B_UN
    if not B_UN:
        B_UN = (await _.get_me()).username
    user_id = m.from_user.id
    if m.text:
        if m.text.split()[0] in ["/afk", f"/afk@{B_UN}", "brb"]:
            return
    afk, details = await is_afk(user_id)
    if not afk:
        return
    first_name = m.from_user.first_name
    start = details["time"]
    reason = details["reason"]
    end = time.time()
    dur = end - start
    dur = get_readable_time(int(dur))
    if reason:
        await m.reply(f"**{first_name}** is back online and was away for {dur}.\n\n**Reason** : `{reason}`)
    else:
        await m.reply(f"**{first_name}** is back online and was away for {dur}.")
    await del_afk(user_id)
