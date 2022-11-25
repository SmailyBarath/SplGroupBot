# MODULE VERIFIED BY @NORTH_YANKTON

import requests
from Spoiled import Yashu
from telegram import Update
from telegram.ext import CallbackContext, CommandHandler
from telegram.constants import ParseMode


async def ud(update: Update, context: CallbackContext):
    message = update.effective_message
    text = message.text[len("/ud ") :]
    results = requests.get(
        f"https://api.urbandictionary.com/v0/define?term={text}"
    ).json()
    try:
        reply_text = f'*{text}*\n\n{results["list"][0]["definition"]}\n\n_{results["list"][0]["example"]}_'
    except:
        reply_text = "No results found."
    await message.reply_text(reply_text, parse_mode=ParseMode.MARKDOWN)

Yashu.add_handler(CommandHandler(["ud", "urban"], ud))
