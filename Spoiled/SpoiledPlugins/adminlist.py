from pyrogram import Client, filters, enums

creator = None
admins = []
bots = []
deleted = []

@Client.on_message(filters.command(["admins", "adminlist", "staff"]) & filters.group)
async def al(_, m):
    global creator, admins, bots, deleted
    ok = await m.reply("**Fetching staff...**")
    async for x in _.get_chat_members(m.chat.id, filter=enums.ChatMembersFilter.ADMINISTRATORS):
        if x.user.is_bot:
            bots.append(x.user.mention)
        elif x.status.name == "OWNER":
            creator = x.user.mention
        elif x.user.is_deleted:
            deleted.append(x.user.mention)
        else:
            admins.append(x.user.mention)

    txt = f"**{m.chat.title} staff :**"
    txt += "\n\n"
    txt += " 👑**Creator :**"
    txt += "\n"
    txt += f" • {creator}"
    if admins:
        txt += "\n\n"
        txt += " 👨‍💻**Admins :**"
        for adm in admins:
            txt += f" • {adm}"
            txt += "\n"
    if bots:
        txt += "\n\n"
        txt += " 🤖**Bots :**"
        for adm in bots:
            txt += f" • {adm}"
            txt += "\n"
    if deleted:
        txt += "\n\n"
        txt += " 👻**Admins :**"
        for adm in deleted:
            txt += f" • **None**"
            txt += "\n"
    try:
        await ok.edit(txt)
    except:
        await m.reply(txt)
    
        
