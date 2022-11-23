from googletrans import Translator
from pyrogram import Client, filters

def trans_to(txt, lan):
    t = Translator()
    x = t.translate(txt, dest=lan)
    return x

@Client.on_message(filters.command(["tr", "tl"]))
async def trans(_, m):
    if not m.reply_to_message:
        return await m.reply("Reply to a message !")
    if not m.reply_to_message.text and not m.reply_to_message.caption:
        return await m.reply("No text found to translate !")
    txt = m.reply_to_message.text
    lan = m.text.split()[1] if len(m.command) > 1 else "en"
    try:
        x = trans_to(txt, lan)
    except:
        x = trans_to(txt, "en")
    await m.reply(x)
