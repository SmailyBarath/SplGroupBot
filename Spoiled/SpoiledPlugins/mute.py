from . import verify
from pyrogram import Client, filters
from . import get_id
from config import DEV
from pyrogram.types import ChatPermissions

DEV_USERS = DEV.SUDO_USERS + [DEV.OWNER_ID]

async def mute_user(_, m):
    try:
        id = await get_id(_, m)
    except:
        return False, f"**Reply to a user or provide id !**"
    if id in DEV_USERS:
        return False, f"**Can't mute sudo users !**"
    x = await _.get_chat_member(m.chat.id, id)
    if x.privileges:
        return False, f"**Can't mute an admin !**"
    await _.restict_chat_member(m.chat.id, id, permissions=ChatPermissions())
    men = (await _.get_users(id)).mention
    return True, f"**{men} muted !**"

async def unmute_user(_, m):
    try:
        id = await get_id(_, m)
    except:
        return False, f"**Reply to a user or provide id !**"
    x = await _.get_chat_member(m.chat.id, id)
    await _.unban_chat_member(m.chat.id, id)
    men = (await _.get_users(id)).mention
    return True, f"**{men} unmuted !**"

@Client.on_message(filters.command(["mute", "smute"]))
async def ban(_, m):
    id = m.from_user.id
    if not id in DEV_USERS:
        x = await _.get_chat_member(m.chat.id, id)
        if not x.privileges:
            return await m.reply("You need to be admin to do this !")
        priv = x.privileges
        if not priv.can_restrict_members:
            return await m.reply("You got no rights to restrict !")
    myid = (await _.get_me()).id
    x = await _.get_chat_member(m.chat.id, myid)
    x = x.privileges
    if not x.can_restrict_members:
        return await m.reply("I got no rights to restrict members !")
    g, h = await mute_user(_, m)
    if not g:
        return await m.reply(h)
    if m.text.split()[0][1].lower() == "s":
        return
    await m.reply(h)

@Client.on_message(filters.command(["unmute"]))
async def unban(_, m):
    id = m.from_user.id
    if not id in DEV_USERS:
        x = await _.get_chat_member(m.chat.id, id)
        if not x.privileges:
            return await m.reply("You need to be admin to do this !")
        priv = x.privileges
        if not priv.can_restrict_members:
            return await m.reply("You got no rights to restrict !")
    myid = (await _.get_me()).id
    x = await _.get_chat_member(m.chat.id, myid)
    x = x.privileges
    if not x.can_restrict_members:
        return await m.reply("I got no rights to restrict members !")
    g, h = await unmute_user(_, m)
    if not g:
        return await m.reply(h)
    await m.reply(h)
