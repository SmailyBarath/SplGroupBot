from pyrogram import Client, filters
from gtts import gTTS

def convert(txt):
    tts = gTTS(txt)
    x = tts.save()
    return x

@Client.on_message(filters.command("tts"))
async def teeteeyess(_, m):
    reply = m.reply_to_message
    if not reply:
        if len(m.command) < 2:
            return await m.reply("**Either reply or give some text !**")
    
    if reply:
        if not reply.text and not reply.caption:
            return await m.reply("**No text found in replied messages !**")
        txt = reply.text if reply.text else reply.caption
        path = convert(txt)
    else:
        txt = m.text.split(None, 1)[1]
        path = convert(txt)

    try:
        await m.reply_voice(path)
    except:
        await m.reply_audio(path)
            
