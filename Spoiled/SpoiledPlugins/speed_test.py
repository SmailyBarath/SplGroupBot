import speedtest
from config import DEV
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import CallbackContext, CallbackQueryHandler
from telegram.constants import ParseMode
from Spoiled import Yashu

DEV_USERS = [DEV.OWNER_ID] + DEV.SUDO_USERS


def convert(speed):
    return round(int(speed) / 1048576, 2)


async def speedtestxyz(update: Update, context: CallbackContext):
    user = update.effective_user
    if not user.id in DEV_USERS:
        return
    buttons = [
        [
            InlineKeyboardButton("Image", callback_data="speedtest_image"),
            InlineKeyboardButton("Text", callback_data="speedtest_text"),
        ]
    ]
    await update.effective_message.reply_text(
        "Select SpeedTest Mode", reply_markup=InlineKeyboardMarkup(buttons)
    )


async def speedtestxyz_callback(update: Update, context: CallbackContext):
    query = update.callback_query
    user = update.effective_user
    if not user.id in DEV_USERS:
        return
    if query.from_user.id in DEV_USERS:
        msg = await update.effective_message.edit_text("Running a speedtest....")
        speed = speedtest.Speedtest()
        speed.get_best_server()
        speed.download()
        speed.upload()
        replymsg = "SpeedTest Results:"

        if query.data == "speedtest_image":
            speedtest_image = speed.results.share()
            await update.effective_message.reply_photo(
                photo=speedtest_image, caption=replymsg
            )
            msg.delete()

        elif query.data == "speedtest_text":
            result = speed.results.dict()
            replymsg += f"\nDownload: `{convert(result['download'])}Mb/s`\nUpload: `{convert(result['upload'])}Mb/s`\nPing: `{result['ping']}`"
            await update.effective_message.edit_text(replymsg, parse_mode=ParseMode.MARKDOWN)
    else:
        await query.answer("You are not a part of EYuii Chan Club.")

Yashu.add_handler(CommandHandler("speedtest", speedtestxyz))
Yashu.add_handler(CallbackQueryHandler(speedtestxyz_callback, pattern="speedtest_.*"))
