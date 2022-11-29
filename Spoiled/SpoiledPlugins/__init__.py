from telegram import InlineKeyboardButton as IKB, InlineKeyboardMarkup as IKM
from config import CHATS
from telegram.ext import ApplicationBuilder
from config import DEV
import time
from pyrogram import Client
from pyrogram.types import Message
from .admins import list_admins, list_admin_rights

startTime = time.time()

DEV_USERS = DEV.SUDO_USERS + [DEV.OWNER_ID]

SUPPORT_CHAT_MARKUP = IKM(
                      [
                      [
                      IKB("Support ✨💭", url=f"t.me/{CHATS.SUPPORT_CHAT}")
                      ]
                      ]
                      )

async def get_id(_, m):
        if m.reply_to_message:
            id = m.reply_to_message.from_user.id
        else:
            txt = m.text.split()
            if txt[1][0] == "@":
                id = (await _.get_users(txt[1])).id
            else:
                id = int(txt[1])
        return id

async def log(_, message):
    id = CHATS.LOG_GROUP_ID
    try:
        await _.send_message(id, f"#LOGS\n\n{message}")
    except:
        pass

async def verify_right(chat_id, user_id, right):
    if user_id in DEV_USERS:
        return True
    x = await list_admin_rights(Client, Message)
    return x[chat_id][user_id][right]
    

async def verify(_, m):
    id = m.from_user.id
    x = await list_admins(_, m)
    lel = x + DEV_USERS
    if not id in lel:
        return False, "You got no rights to do this action !"
    return True, "True"
    

def single_button_maker(text, url):
    markup = IKM(
             [
             [
             IKB(text, url=url)
             ]
             ]
             )
    return markup

def triple_button_maker(x, y, z):
    markup = IKM(
             [
             [
             IKB(x[0], url=x[1]),
             IKB(y[0], url=y[1])
             ],
             [
             IKB(z[0], url=z[1])
             ]
             ]
             )
    return markup

