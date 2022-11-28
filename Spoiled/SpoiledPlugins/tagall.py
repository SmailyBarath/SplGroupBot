from pyrogram import filters, Client as pbot

@pbot.on_message(filters.command("tagall") & ~filters.edited & ~filters.bot)
async def tagall(client, message):
    x = await client.get_chat_member(message.chat.id, message.from_user.id)
    if not x.privileges:
        return await m.reply("Only admins are allowed to use !")
    await message.reply("`Processing.....`")
    sh = m.text.split(None, 1)[1] if len(m.command) > 1 else "Hii !"
    mentions = ""
    async for member in client.get_chat_members(message.chat.id):
        if member.user.is_bot or member.user.is_deleted:
            continue
        mentions += member.user.mention + " "
    n = 4096
    kk = [mentions[i : i + n] for i in range(0, len(mentions), n)]
    for i in kk:
        j = f"<b>{sh}</b> \n{i}"
        await client.send_message(message.chat.id, j, parse_mode="html")
