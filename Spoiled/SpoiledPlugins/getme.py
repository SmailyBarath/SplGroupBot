from pyrogram import Client, filters
# 1

@Client.on_message(filters.command("getme") & filters.group)
async def geth(_, m):
    x = await _.get_chat_member(m.chat.id, m.from_user.id)
    await m.reply(x.status)
