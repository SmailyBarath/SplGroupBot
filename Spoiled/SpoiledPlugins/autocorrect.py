from pyrogram import filters, Client as app
from pyrogram.types import Message

from .arq import arq
from .chatbot import eor

@app.on_message(filters.command("autocorrect"))
async def autocorrect_bot(_, message: Message):
    if not message.reply_to_message:
        return await message.reply_text("Reply to a text message.")
    reply = message.reply_to_message
    text = reply.text or reply.caption
    if not text:
        return await message.reply_text("Reply to a text message.")
    data = await arq.spellcheck(text)
    if not data.ok:
        return await message.reply_text("Something wrong happened.")
    result = data.result
    await message.reply_text(result.corrected if result.corrected else "Empty")


IS_ENABLED = True


@app.on_message(
    filters.text,
    group=7
)
async def autocorrect_ubot(_, message: Message):
    if not IS_ENABLED:
        return
    text = message.text
    data = await arq.spellcheck(text)
    corrected = data.result.corrected
    if corrected == text:
        return
    await message.reply(corrected + "*")
