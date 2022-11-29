from . import verify
from pyrogram import Client, filters
from . import get_id
from config import DEV

DEV_USERS = DEV.SUDO_USERS + [DEV.OWNER_ID]

async def ban_user(_, m):
    try:
        id = await get_id(_, m)
    except:
        return False, f"**Reply to a user or provide id !**"
    if not m.reply_to_message:
        if len(m.command) > 2:
            reason = m.text.split(None, 2)[2]
    else:
        if len(m.command) > 1:
            reason = m.text.split(None, 1)[1]
    myid = (await _.get_me()).id
    if id == myid:
        return False, "😒😒.."
    if id in DEV_USERS:
        return False, f"**Can't ban sudo users !**"
    x = await _.get_chat_member(m.chat.id, id)
    if x.privileges:
        return False, f"**Can't ban an admin !**"
    await _.ban_chat_member(m.chat.id, id)
    men = (await _.get_users(id)).mention
    if reason:
        return True, f"**{men} banned !\n\nReason : {reason}**"
    else:
        return True, f"**{men} banned !**"

async def unban_user(_, m):
    try:
        id = await get_id(_, m)
    except:
        return False, f"**Reply to a user or provide id !**"
    x = await _.get_chat_member(m.chat.id, id)
    await _.unban_chat_member(m.chat.id, id)
    men = (await _.get_users(id)).mention
    return True, f"**{men} unbanned !**"

@Client.on_message(filters.command(["ban", "sban"]) & filters.group)
async def ban(_, m):
    id = m.from_user.id
    if not id in DEV_USERS:
        x = await _.get_chat_member(m.chat.id, id)
        if not x.privileges:
            return await m.reply("You need to be admin this !")
        priv = x.privileges
        if not priv.can_restrict_members:
            return await m.reply("You got no rights to restrict !")
    myid = (await _.get_me()).id
    x = await _.get_chat_member(m.chat.id, myid)
    if not x.privileges:
        return await m.reply(f"**I'm not admin !**")
    x = x.privileges
    if not x.can_restrict_members:
        return await m.reply("I got no rights to restrict members !")
    g, h = await ban_user(_, m)
    if not g:
        return await m.reply(h)
    if m.text.split()[0][1].lower() == "s":
        return
    await m.reply(h)

@Client.on_message(filters.command(["unban"]) & filters.group)
async def unban(_, m):
    id = m.from_user.id
    if not id in DEV_USERS:
        x = await _.get_chat_member(m.chat.id, id)
        if not x.privileges:
            return await m.reply("You need to be admin this !")
        priv = x.privileges
        if not priv.can_restrict_members:
            return await m.reply("You got no rights to restrict !")
    myid = (await _.get_me()).id
    x = await _.get_chat_member(m.chat.id, myid)
    if not x.privileges:
        return await m.reply(f"**I'm not admin !**")
    x = x.privileges
    if not x.can_restrict_members:
        return await m.reply("I got no rights to restrict members !")
    g, h = await unban_user(_, m)
    if not g:
        return await m.reply(h)
    await m.reply(h)
