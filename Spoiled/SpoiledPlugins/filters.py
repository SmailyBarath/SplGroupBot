from pyrogram import Client, filters
from config import DEV

DEV_USERS = DEV.SUDO_USERS + [DEV.OWNER_ID]

@Client.on_message(filters.command("filter") & filters.group)
async def filter(_, m):
    id = m.from_user.id
    if not id in DEV_USERS:
        x = await _.get_chat_member(m.chat.id, id)
        if not x.privileges:
            return await m.reply("**You don't have right to do this !**")
        x = x.privileges
        if not x.can_change_info:
            return await m.reply("**You don't have right to edit filters !**")
    reply = m.reply_to_message
    if not reply:
        txt = m.text.split()
        if len(txt) < 3:
            return await m.reply("**/filter trigger text**")
        trigger = m.text.split()[1]
        content = {"file": None, "text": m.text.split(None, 2)[2]}
    if reply:
        if reply.text:
            if len(m.command) < 2:
                return await m.reply("**Give a word to filter it !**")
            trigger = m.text.split()[1]
            content = {"file": None, "text": reply.text}
        elif reply.media:
            caption = reply.caption if reply.caption else None
            if len(m.command) < 2:
                return await m.reply("**Give a word to filter it !**")
            if reply.photo:
                content = {"file": ["photo", reply.photo.file_id], "text": caption}
            if reply.video:
                content = {"file": ["video", reply.video.file_id], "text": caption}
            if reply.sticker:
                content = {"file": ["sticker", reply.sticker.file_id], "text": caption}
            if reply.document:
                content = {"file": ["document", reply.document.file_id], "text": caption}
            if reply.audio:
                content = {"file": ["audio", reply.audio.file_id], "text": caption}
            if reply.voice:
                content = {"file": ["voice", reply.voice.file_id], "text": caption}
            if reply.animation:
                content = {"file": ["animation", reply.animation.file_id], "text": caption}
