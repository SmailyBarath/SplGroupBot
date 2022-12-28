from pyrogram import Client, filters
from io import BytesIO
from requests import get


@Client.on_message(filters.command("write"))
async def writer(_, m):
    if m.reply_to_message:
        txt = m.reply_to_message.text
    else:
        if len(m.command) > 1:
            txt = m.text.split(None, 1)[1]
        else:
            return await m.reply("Either reply to a text or write..!")
    txt = txt.replace(" ", "%20")

    var = await m.reply("`processing...`")
    with BytesIO(get(f"https://apis.xditya.me/write?text={text}").content) as file:
        file.name: str = "image.jpg"
        try:
            await m.reply_photo(file)
        except Exception as e:
            await m.reply(e)
    await var.delete()
