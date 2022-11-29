from pyrogram import Client, filters
from . import verify, verify_right
from config import DEV

DEV_USERS = DEV.SUDO_USERS + [DEV.OWNER_ID]

@Client.on_message(filters.command("del") & filters.group)
async def dele(_, m):
    id = m.from_user.id
    if not id in DEV_USERS:
        d = await _.get_chat_member(m.chat.id, id)
        if not d.privileges: 
            try:
                return await m.delete()
            except:
                return
        if not d.privileges.can_delete_messages:
            try:
                return await m.delete()
            except:
                return
        if not m.reply_to_message:
            try:
                return await m.delete()
            except:
                return
        try:
            await m.reply_to_message.delete()
            await m.delete()
        except:
            return

@Client.on_message(filters.command(["pin", "unpin"]) & filters.group)
async def pin(_, m):
    id = m.from_user.id
    id = m.from_user.id
    if not id in DEV_USERS:
        d = await _.get_chat_member(m.chat.id, id)
        if not d.privileges:
            return await m.reply(f"**Only admins are allowed to do this.**")
        if not d.privileges.can_pin_messages:
            return await m.reply(f"**You got no right to do this**")
    if not m.reply_to_message:
        return await m.reply(f"**What I've to do ?**")
    if m.text.split()[0][1] == "u":
        await m.reply_to_message.unpin()
        await m.reply(f"**Message unpinned !**")
    else:
        await m.reply_to_message.pin()
        await m.reply(f"**Message pinned !**")
    
