from pyrogram.types import InlineKeyboardButton as IKB, InlineKeyboardMarkup as IKM
from config import CHATS
from Spoiled.SpoiledPlugins import botname, botun

START_TEXT = """

Hello {} !
✪ I'm {}, an anime-themed group management bot ✨
────────────────────────
× Service Uptime: {}
× {} users.
────────────────────────
✪ Hit /help for more info.

"""

START_MARKUP = IKM(
               [
               [
               IKB(f"About {botname} ✨💭", callback_data="about_bot")
               ],
               [
               IKB("Commands ✨💭", callback_data="help"),
               IKB("Support ✨💭" url=f"t.me/{CHATS.SUPPORT_CHAT}")
               ],
               [
               IKB("➕ Add Me To Your Group ➕", url=f"t.me/{botun}?startgroup=True")
               ]
               ]
               )
