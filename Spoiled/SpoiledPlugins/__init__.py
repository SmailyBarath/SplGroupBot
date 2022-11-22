from pyrogram.types import InlineKeyboardButton as IKB, InlineKeyboardMarkup as IKM
from config.CHATS import SUPPORT_CHAT
from telegram.ext import ApplicationBuilder
from config.TOKENS import BOT_TOKEN

SUPPORT_CHAT_MARKUP = IKM(
                      [
                      [
                      IKB("Support ✨💭", url=f"t.me/{SUPPORT_CHAT}")
                      ]
                      ]
                      )

async def get_id(_, m):
    try:
        if m.reply_to_message:
            id = m.reply_to_message.from_user.id
        else:
            txt = m.text.split()
            if txt[1][0] == "@":
                id = (await _.get_users(txt[1])).id
            else:
                id = int(txt[1])
    except:
        pass

async def log(_, id, message):
    try:
        await _.send_message(id, f"#LOGS\n\n{message}")
    except:
        pass
