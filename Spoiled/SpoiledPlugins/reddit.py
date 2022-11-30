from pyrogram import filters, Client as app
from .arq import arq

@app.on_message(filters.command("reddit"))
async def reddit(_, message):
    if len(message.command) != 2:
        return await message.reply_text("/reddit needs an argument")
    subreddit = message.text.split(None, 1)[1]
    m = await message.reply_text("Searching")
    reddit = await arq.reddit(subreddit)
    if not reddit.ok:
        return await m.edit(reddit.result)
    reddit = reddit.result
    nsfw = reddit.nsfw
    sreddit = reddit.subreddit
    title = reddit.title
    image = reddit.url
    link = reddit.postLink
    if nsfw:
        return await m.edit("NSFW RESULTS COULD NOT BE SHOWN.")
    caption = f"""
**Title:** `{title}`
**Subreddit:** {sreddit}
**PostLink:** {link}"""
    try:
        await message.reply_photo(photo=image, caption=caption)
        await m.delete()
    except Exception as e:
        await m.edit(e.MESSAGE)
