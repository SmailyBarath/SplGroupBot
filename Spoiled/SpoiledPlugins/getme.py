from pyrogram import Client, filters
# 1

@Client.on_message(filters.command("getme") & filters.group)
async def geth(_, m):
    x = await _.get_chat_member(m.chat.id, m.from_user.id)
    await m.reply(x.status)

@Client.on_message(filters.command("getuser") & filters.group)
async def geth(_, m):
    id = int(m.text.split()[1])
    x = await _.get_chat_member(m.chat.id, id)
    await m.reply(x.status)
