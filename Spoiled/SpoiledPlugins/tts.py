from pyrogram import Client, filters, enums
from gtts import gTTS

def convert(txt):
    tts = gTTS(txt)
    x = "alpha.mp3"
    tts.save(x)
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
        await _.send_chat_action(m.chat.id, enums.ChatAction.RECORD_AUDIO)
        await m.reply_voice(path)
        await _.send_chat_action(m.chat.id, enums.ChatAction.CANCEL)
    except:
        await _.send_chat_action(m.chat.id, enums.ChatAction.RECORD_AUDIO)
        await m.reply_audio(path)
        await _.send_chat_action(m.chat.id, enums.ChatAction.CANCEL)
            
