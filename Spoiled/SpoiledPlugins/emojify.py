from pyrogram import Client as End, filters
from pyrogram.types import Message as Dev 
from Spoiled.Addons.emotes import *
from Spoiled.Database.blocked import is_blocked

@End.on_message(filters.command("emojify"))
async def doli(ailika, jhulika: Dev):
        if await is_blocked(jhulika.from_user.id) is True:
            return
        txt = jhulika.text
        if len(jhulika.command) != 2:
            return await jhulika.reply("Try: < /emojify Crystal >")
        txt = txt.split(None, 1)[1]
        final = ""
        for a in txt:
            a = a.lower()
            a = str(a)
            if a in END_TEXT:
                letter = END_EMOJI[END_TEXT.index(a)]
                final += letter
            else:
                final += a
        await jhulika.reply(final)

@End.on_message(filters.command("crystal"))
async def crystal(ailika, jhulika: Dev):
    if is_blocked(jhulika.from_user.id) is True:
        return
    txt = jhulika.text
    if len(jhulika.command)!= 3:
        return await jhulika.reply("Try: < /crystal ✨ doli >")
    emoji = txt.split(None, 2)[1]
    text = txt.split(None, 2)[2]
    final = ""
    for a in text:
        a = a.lower()
        a = str(a)
        if a in END_TEXT:
            letter = END_CJ[END_TEXT.index(a)].format(cj=emoji)
            final += letter
        else:
            final += a
    await jhulika.reply(final)
