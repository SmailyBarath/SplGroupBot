from pyrogram import Client, filters
from Spoiled.Database.afk import *
import time
from config import DEV

DEV_USERS = SUDO_USERS + [OWNER_ID]

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

@Client.on_message(group=1)
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
        await m.reply(f"**{first_name}** is back online and was away for {dur}.\n\n**Reason** : `{reason}`")
    else:
        await m.reply(f"**{first_name}** is back online and was away for {dur}.")
    await del_afk(user_id)

def get_readable_time(seconds: int) -> str:
    count = 0
    ping_time = ""
    time_list = []
    time_suffix_list = ["s", "m", "h", "days"]
    while count < 4:
        count += 1
        if count < 3:
            remainder, result = divmod(seconds, 60)
        else:
            remainder, result = divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)
    for i in range(len(time_list)):
        time_list[i] = str(time_list[i]) + time_suffix_list[i]
    if len(time_list) == 4:
        ping_time += time_list.pop() + ", "
    time_list.reverse()
    ping_time += ":".join(time_list)
    return ping_time

@Client.on_message(group=2)
async def reply_afk(_, m):
    if m.reply_to_message:
        if not m.reply_to_message.from_user:
            return 
        id = m.reply_to_message.from_user.id
        afk, details = await is_afk(id)
        if afk:
            first_name = (await _.get_users(id)).first_name
            start = details["time"]
            reason = details["reason"]
            end = time.time()
            dur = end - start
            dur = get_readable_time(int(dur))
            if reason:
                await m.reply(f"**{first_name}** is back online and was away for {dur}.\n\n**Reason** : `{reason}`")
            else:
                await m.reply(f"**{first_name}** is back online and was away for {dur}.")
    else:
        if m.text or m.caption:
            args = m.text.split() if m.text else m.caption.split()
            uns = []
            for x in args:
                if x[0] == "@":
                    uns.append(x)
            if not uns:
                return
            for z in uns:
                id = (await _.get_users(z)).id
                afk, details = await is_afk(id)
                if afk:
                    first_name = (await _.get_users(id)).first_name
                    start = details["time"]
                    reason = details["reason"]
                    end = time.time()
                    dur = end - start
                    dur = get_readable_time(int(dur))
                    if reason:
                        await m.reply(f"**{first_name}** is back online and was away for {dur}.\n\n**Reason** : `{reason}`")
                    else:
                        await m.reply(f"**{first_name}** is back online and was away for {dur}.")


@Client.on_message(filters.command("afkusers") & filters.user(DEV_USERS))
async def afk_users(_, m):
    x = await get_afk_users()
    return await m.reply(f"**AFK Users** : {x}")
