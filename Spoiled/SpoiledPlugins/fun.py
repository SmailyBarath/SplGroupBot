import html
import random
import time

import Spoiled.SpoiledPlugins.fun_strings as fun_strings
from Spoiled import Yashu 
from telegram import Update
from telegram.constants import ParseMode
from telegram.error import BadRequest
from telegram.ext import CallbackContext, CommandHandler

GIF_ID = "CgACAgQAAx0CSVUvGgAC7KpfWxMrgGyQs-GUUJgt-TSO8cOIDgACaAgAAlZD0VHT3Zynpr5nGxsE"


async def runs(update: Update, context: CallbackContext):
    temp = random.choice(fun_strings.RUN_STRINGS)
    await update.effective_message.reply_text(temp)


async def sanitize(update: Update, context: CallbackContext):
    message = update.effective_message
    name = (
        message.reply_to_message.from_user.first_name
        if message.reply_to_message
        else message.from_user.first_name
    )
    reply_animation = (
        await message.reply_to_message.reply_animation
        if message.reply_to_message
        else await message.reply_animation
    )
    reply_animation(random.choice(fun_strings.GIFS), caption=f"*Sanitizes {name}*")



async def roll(update: Update, context: CallbackContext):
    await update.effective_message.reply_text(random.choice(range(1, 7)))


async def shout(update: Update, context: CallbackContext):
    args = context.args
    text = " ".join(args)
    result = []
    result.append(" ".join(list(text)))
    for pos, symbol in enumerate(text[1:]):
        result.append(symbol + " " + "  " * pos + symbol)
    result = list("\n".join(result))
    result[0] = text[0]
    result = "".join(result)
    msg = "```\n" + result + "```"
    return await update.effective_message.reply_text(msg, parse_mode="MARKDOWN")


async def shrug(update: Update, context: CallbackContext):
    msg = update.effective_message
    reply_text = (
        await msg.reply_to_message.reply_text if msg.reply_to_message else await msg.reply_text
    )
    reply_text(r"¯\_(ツ)_/¯")


async def bluetext(update: Update, context: CallbackContext):
    msg = update.effective_message
    reply_text = (
        await msg.reply_to_message.reply_text if msg.reply_to_message else await msg.reply_text
    )
    reply_text(
        "/BLUE /TEXT\n/MUST /CLICK\n/I /AM /A /STUPID /ANIMAL /THAT /IS /ATTRACTED /TO /COLORS",
    )


async def rlg(update: Update, context: CallbackContext):
    eyes = random.choice(fun_strings.EYES)
    mouth = random.choice(fun_strings.MOUTHS)
    ears = random.choice(fun_strings.EARS)

    if len(eyes) == 2:
        repl = ears[0] + eyes[0] + mouth[0] + eyes[1] + ears[1]
    else:
        repl = ears[0] + eyes[0] + mouth[0] + eyes[0] + ears[1]
    await update.effective_message.reply_text(repl)


async def decide(update: Update, context: CallbackContext):
    reply_text = (
        await update.effective_message.reply_to_message.reply_text
        if update.effective_message.reply_to_message
        else await update.effective_message.reply_text
    )
    reply_text(random.choice(fun_strings.DECIDE))


async def eightball(update: Update, context: CallbackContext):
    reply_text = (
        await update.effective_message.reply_to_message.reply_text
        if update.effective_message.reply_to_message
        else await update.effective_message.reply_text
    )
    reply_text(random.choice(fun_strings.EIGHTBALL))


async def table(update: Update, context: CallbackContext):
    reply_text = (
        await update.effective_message.reply_to_message.reply_text
        if update.effective_message.reply_to_message
        else await update.effective_message.reply_text
    )
    reply_text(random.choice(fun_strings.TABLE))


Yashu.add_handler(CommandHandler("sanitize", sanitize))
Yashu.add_handler(CommandHandler("run", runs))
Yashu.add_handler(CommandHandler("roll", roll))
Yashu.add_handler(CommandHandler("shrug", shrug))
Yashu.add_handler(CommandHandler("rlg", rlg))
Yashu.add_handler(CommandHandler("bluetext", bluetext))
Yashu.add_handler(CommandHandler("decide", decide))
Yashu.add_handler(CommandHandler("8ball", eightball))
Yashu.add_handler(CommandHandler("shout", shout))
Yashu.add_handler(CommandHandler("table", table))
