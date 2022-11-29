import cloudscraper
from bs4 import BeautifulSoup as bs
from telegram import Update
from telegram.ext import CallbackContext, CommandHandler
from telegram.constants import ParseMode
from Spoiled import Yashu
from html import escape

combot_stickers_url = "https://combot.org/telegram/stickers?q="

async def stickerid(update: Update, context: CallbackContext):
    msg = update.effective_message
    if msg.reply_to_message and msg.reply_to_message.sticker:
        await update.effective_message.reply_text("The sticker id you are replying is :\n <code>"
            + escape(msg.reply_to_message.sticker.file_id)
            + "</code>",
            parse_mode=ParseMode.HTML,
        )
    else:
        await update.effective_message.reply_text(
            "Please reply to sticker message to get id sticker",
            parse_mode=ParseMode.HTML,
        )

async def cb_sticker(update: Update, context: CallbackContext):
    msg = update.effective_message
    split = msg.text.split(" ", 1)
    if len(split) == 1:
        await msg.reply_text("Provide some name to search for pack.")
        return

    scraper = cloudscraper.create_scraper()
    text = scraper.get(combot_stickers_url + split[1]).text
    soup = bs(text, "lxml")
    results = soup.find_all("a", {"class": "sticker-pack__btn"})
    titles = soup.find_all("div", "sticker-pack__title")
    if not results:
        await msg.reply_text("No results found :(.")
        return
    reply = f"Stickers for *{split[1]}*:"
    for result, title in zip(results, titles):
        link = result["href"]
        reply += f"\n• [{title.get_text()}]({link})"
    await msg.reply_text(reply, parse_mode=ParseMode.MARKDOWN)

Yashu.add_handler(CommandHandler("stickers", cb_sticker))
Yashu.add_handler(CommandHandler("stickerid", stickerid))
