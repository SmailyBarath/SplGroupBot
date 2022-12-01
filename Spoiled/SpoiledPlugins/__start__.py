from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton as IKB, InlineKeyboardMarkup as IKM
from Strings.start import START_TEXT
from config import STUFF, CHATS
import time
from . import startTime, botname
from .afk import get_readable_time
from Spoiled.Database.users import get_served_users
from Spoiled.Database.pusers import add_served_puser

botname = None
botun = None

@Client.on_message(filters.command("start") & filters.group)
async def st(_, m):
    global botname, botun
    if not botname or not botun:
        Me = await _.get_me()
        botname = Me.first_name
        botun = Me.username
    START_MARKUP = IKM(
               [
               [
               IKB(f"About {botname} ✨💭", callback_data="about_bot")
               ],
               [
               IKB("Commands ✨💭", callback_data="help"),
               IKB("Support ✨💭", url=f"t.me/{CHATS.SUPPORT_CHAT}")
               ],
               [
               IKB("➕ Add Me To Your Group ➕", url=f"t.me/{botun}?startgroup=True")
               ]
               ]
               )
    fn = m.from_user.first_name
    Upt = get_readable_time(int(time.time()-startTime))
    x = await get_served_users
    x = len(x)
    await add_served_puser(m.from_user.id)
    await m.reply_photo(STUFF.START_IMG, caption=START_TEXT.format(fn, botname, Upt, x), reply_markup=START_MARKUP)
