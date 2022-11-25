# MODULE VERIFIED BY @NORTH_YANKTON

import secureme
from pyrogram import Client, filters

@Client.on_message(filters.command("encrypt"))
async def encrypt(_, m):
    if m.reply_to_message:
        if m.reply_to_message.text:
            txt = m.reply_to_message.text
        else:
            return
    else:
        if len(m.command) > 1:
            txt = m.text.split(None, 1)[1]
        else:
            return
    if txt:
        k = secureme.encrypt(txt)
        await m.reply(k)

@Client.on_message(filters.command("decrypt"))
async def decrypt(_, m):
    if m.reply_to_message:
        if m.reply_to_message.text:
            txt = m.reply_to_message.text
        else:
            return
    else:
        if len(m.command) > 1:
            txt = m.text.split(None, 1)[1]
        else:
            return
    if txt:
        k = secureme.decrypt(txt)
        await m.reply(k)
