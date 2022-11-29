from pyrogram import Client, filters
from . import verify, verify_right

@Client.on_message(filters.command("del"))
async def del(_, m):
    id = m.from_user.id
    g, h = await verify(_, m)
    if not g:
        try:
            return await m.delete()
        except:
            return
    g = await verify_right(m.chat.id, id, "can_delete_messages")
    if not g:
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
