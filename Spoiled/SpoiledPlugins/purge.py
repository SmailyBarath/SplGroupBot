from pyrogram import Client, filters
from config import DEV
import time

PURGABLE = [DEV.OWNER_ID] + DEV.SUDO_USERS

@Client.on_message(filters.command("purge"))
async def purge(_, m):
    user_id = m.from_user.id
    chat_id = m.chat.id
    me = await _.get_me()
    myid = me.id
    Me = await _.get_chat_member(chat_id, myid)
    Me = Me.privileges
    if not Me.can_delete_messages:
        return await m.reply("I got no rights to purge !")
    await m.delete()
    if not m.reply_to_message:
        return await m.reply("Reply to a message to purge from !")
    is_sudo = True if user_id in PURGABLE else False
    if not is_sudo:
        x = await _.get_chat_member(chat_id, user_id)
        x = x.privileges
        if not x.can_delete_messages:
            return await m.reply("You got no rights to purge !")
        to_id = m.message_id - 1
        from_id = m.reply_to_message.message_id
        ids = []
        a = from_id
        for i in range(0, (to_id - from_id)):
            if a > to_id:
                break
            ids.append(a)
            a += 1
        await _.delete_messages(chat_id, ids)
        await m.reply("Purged !")
    else:
        to_id = m.message_id - 1
        from_id = m.reply_to_message.message_id
        ids = []
        a = from_id
        for i in range(0, (to_id - from_id)):
            if a > to_id:
                break
            ids.append(a)
            a += 1
        await _.delete_messages(chat_id, ids)
        await m.reply("Purged !")
        
        
        
