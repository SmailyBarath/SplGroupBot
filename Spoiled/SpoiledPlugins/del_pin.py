from pyrogram import Client, filters
from . import verify, verify_right

@Client.on_message(filters.command("del") & filters.group)
async def dele(_, m):
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

@Client.on_message(filters.command(["pin", "unpin"]) & filters.group)
async def pin(_, m):
    id = m.from_user.id
    g, h = await verify(_, m)
    if not g:
        return await m.reply(h)
    g = await verify_right(m.chat.id, id, "can_pin_messages")
    if not g:
        return await m.reply("You got no right to do this")
    if not m.reply_to_message:
        return await m.reply("What I've to do ?")
    if m.text.split()[0][1] == "u":
        await m.reply_to_message.unpin()
        await m.reply(f"**Message unpinned !**")
    else:
        await m.reply_to_message.pin()
        await m.reply(f"**Message pinned !**")
    
