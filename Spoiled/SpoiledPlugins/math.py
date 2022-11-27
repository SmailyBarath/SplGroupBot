import math

import pynewtonmath as newton
from Spoiled import Yashu
from telegram import Update
from telegram.ext import CallbackContext, CommandHandler


async def simplify(update: Update, context: CallbackContext):
    args = context.args
    message = update.effective_message
    await message.reply_text(newton.simplify("{}".format(args[0])))


async def factor(update: Update, context: CallbackContext):
    args = context.args
    message = update.effective_message
    await message.reply_text(newton.factor("{}".format(args[0])))


async def derive(update: Update, context: CallbackContext):
    args = context.args
    message = update.effective_message
    await message.reply_text(newton.derive("{}".format(args[0])))


async def integrate(update: Update, context: CallbackContext):
    args = context.args
    message = update.effective_message
    await message.reply_text(newton.integrate("{}".format(args[0])))


async def zeroes(update: Update, context: CallbackContext):
    args = context.args
    message = update.effective_message
    await message.reply_text(newton.zeroes("{}".format(args[0])))


async def tangent(update: Update, context: CallbackContext):
    args = context.args
    message = update.effective_message
    await message.reply_text(newton.tangent("{}".format(args[0])))


async def area(update: Update, context: CallbackContext):
    args = context.args
    message = update.effective_message
    await message.reply_text(newton.area("{}".format(args[0])))


async def cos(update: Update, context: CallbackContext):
    args = context.args
    message = update.effective_message
    await message.reply_text(math.cos(int(args[0])))


async def sin(update: Update, context: CallbackContext):
    args = context.args
    message = update.effective_message
    await message.reply_text(math.sin(int(args[0])))


async def tan(update: Update, context: CallbackContext):
    args = context.args
    message = update.effective_message
    await message.reply_text(math.tan(int(args[0])))


async def arccos(update: Update, context: CallbackContext):
    args = context.args
    message = update.effective_message
    await message.reply_text(math.acos(int(args[0])))


async def arcsin(update: Update, context: CallbackContext):
    args = context.args
    message = update.effective_message
    await message.reply_text(math.asin(int(args[0])))


async def arctan(update: Update, context: CallbackContext):
    args = context.args
    message = update.effective_message
    await message.reply_text(math.atan(int(args[0])))


async def abs(update: Update, context: CallbackContext):
    args = context.args
    message = update.effective_message
    await message.reply_text(math.fabs(int(args[0])))


async def log(update: Update, context: CallbackContext):
    args = context.args
    message = update.effective_message
    await message.reply_text(math.log(int(args[0])))

Yashu.add_handler(CommandHandler("math", simplify))
Yashu.add_handler(CommandHandler("factor", factor))
Yashu.add_handler(CommandHandler("derive", derive))
Yashu.add_handler(CommandHandler("integrate", integrate))
Yashu.add_handler(CommandHandler("zeroes", zeroes))
Yashu.add_handler(CommandHandler("tangent", tangent))
Yashu.add_handler(CommandHandler("area", area))
Yashu.add_handler(CommandHandler("cos", cos))
Yashu.add_handler(CommandHandler("sin", sin))
Yashu.add_handler(CommandHandler("tan", tan))
Yashu.add_handler(CommandHandler("arccos", arccos))
Yashu.add_handler(CommandHandler("arcsin", arcsin))
Yashu.add_handler(CommandHandler("arctan", arctan))
Yashu.add_handler(CommandHandler("abs", abs))
Yashu.add_handler(CommandHandler("log", log))

