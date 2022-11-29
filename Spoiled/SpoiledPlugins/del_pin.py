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
            pass
    
