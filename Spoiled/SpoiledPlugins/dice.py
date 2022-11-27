from pyrogram import Client, filters

@Client.on_message(filters.command("dice"))
async def dice(_, m):
    try:
        await _.send_dice(m.chat.id, "🎲")
    except:
        pass
