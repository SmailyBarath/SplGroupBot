from pyrogram import Client, filters
from . import get_id
from config import DEV

DEV_USERS = DEV.SUDO_USERS + [DEV.OWNER_ID]

async def kick_user(_, m):
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
        return False, f"**Can't kick sudo users !**"
    x = await _.get_chat_member(m.chat.id, id)
    if x.privileges:
        return False, f"**Can't kick an admin !**"
    await _.ban_chat_member(m.chat.id, id)
    men = (await _.get_users(id)).mention
    if reason:
        return True, f"**{men} kicked !\n\nReason : {reason}**"
    else:
        return True, f"**{men} kicked !**"
