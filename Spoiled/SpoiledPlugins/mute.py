from . import verify
from pyrogram import Client, filters
from . import get_id
from config import DEV
from pyrogram.types import ChatPermissions
from datetime import datetime, timedelta

DEV_USERS = DEV.SUDO_USERS + [DEV.OWNER_ID]

async def mute_user(_, m):
    try:
        id = await get_id(_, m)
    except:
        return False, f"**Reply to a user or provide id !**"
    reason = None
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
        return False, f"**Can't mute sudo users !**"
    x = await _.get_chat_member(m.chat.id, id)
    if x.status.ChatMemberStatus.RESTRICTED:
        return False, "**Already restricted**"
    if x.privileges:
        return False, f"**Can't mute an admin !**"
    await _.restrict_chat_member(m.chat.id, id, permissions=ChatPermissions())
    men = (await _.get_users(id)).mention
    if reason:
        return True, f"**{men} muted !\n\nReason : {reason}**"
    else:
        return True, f"**{men} muted !**"

async def unmute_user(_, m):
    try:
        id = await get_id(_, m)
    except:
        return False, f"**Reply to a user or provide id !**"
    x = await _.get_chat_member(m.chat.id, id)
    if not x.status.ChatMemberStatus.RESTRICTED:
        return False, "**User isn't restricted!**"
    await _.unban_chat_member(m.chat.id, id)
    men = (await _.get_users(id)).mention
    return True, f"**{men} unmuted !**"

@Client.on_message(filters.command(["mute", "smute"]) & filters.group)
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
    if not x.privileges:
        return await m.reply(f"**I'm not admin !**")
    x = x.privileges
    if not x.can_restrict_members:
        return await m.reply(f"**I got no rights to restrict members !**")
    g, h = await mute_user(_, m)
    if not g:
        return await m.reply(h)
    if m.text.split()[0][1].lower() == "s":
        return
    await m.reply(h)

@Client.on_message(filters.command(["unmute"]) & filters.group)
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
    if not x.privileges:
        return await m.reply(f"**I'm not admin !**")
    x = x.privileges
    if not x.can_restrict_members:
        return await m.reply("I got no rights to restrict members !")
    g, h = await unmute_user(_, m)
    if not g:
        return await m.reply(h)
    await m.reply(h)

async def tmute_user(_, m):
    try:
        id = await get_id(_, m)
    except:
        return False, f"**Reply to a user or provide id !**"
    if not m.reply_to_message:
        if len(m.command) == 3:
            try:
                tim = int(m.text.split()[2])
            except:
                return await m.reply(f"**Enter a value which will be considered in minutes !**")
            reason = None
        elif len(m.command) > 3: 
            try:
                tim = int(m.text.split()[2])
            except:
                return await m.reply(f"**Enter a value which will be considered in minutes !**")
            reason = m.text.split(None, 3)[3] 
        else:
            return await m.reply(f"**Enter a value which will be considered in minutes !**")   
    else:
        if len(m.command) > 1:
            try:
                tim = int(m.text.split(None, 2)[1])
            except:
                return await m.reply(f"**Enter a value which will be considered in minutes !**")
            reason = None
        elif len(m.command) > 2: 
            try:
                tim = int(m.text.split(None, 2)[1])
            except:
                return await m.reply(f"**Enter a value which will be considered in minutes !**")
            reason = m.text.split(None, 2)[2]
        else:
            return await m.reply(f"**Enter a value which will be considered in minutes !**")
    myid = (await _.get_me()).id
    if id == myid:
        return False, "😒😒.."
    if id in DEV_USERS:
        return False, f"**Can't mute sudo users !**"
    x = await _.get_chat_member(m.chat.id, id)
    if x.privileges:
        return False, f"**Can't mute an admin !**"
    await _.restrict_chat_member(m.chat.id, id, ChatPermissions(), datetime.now()+timedelta(minutes=tim))
    men = (await _.get_users(id)).mention
    if reason:
        return True, f"**{men} muted for {tim}min!\n\nReason : {reason}**"
    else:
        return True, f"**{men} muted for {tim}min!**"

@Client.on_message(filters.command(["tmute"]) & filters.group)
async def tban(_, m):
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
    if not x.privileges:
        return await m.reply(f"**I'm not admin !**")
    x = x.privileges
    if not x.can_restrict_members:
        return await m.reply(f"**I got no rights to restrict members !**")
    g, h = await tmute_user(_, m)
    if not g:
        return await m.reply(h)
    if m.text.split()[0][1].lower() == "s":
        return
    await m.reply(h)
