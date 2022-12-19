from pyrogram.types import InlineKeyboardButton as IKB, InlineKeyboardMarkup as IKM, InputMediaPhoto as IMP
from Strings.help import *
from Strings.start import START_TEXT 
from pyrogram import Client
import time
from . import startTime
from .afk import get_readable_time
from config import STUFF, CHATS
from Spoiled.Database.users import get_served_users

def append_button(LIST, button1, button2, button3):
    LIST.append(button1)
    LIST.append(button2)
    LIST.append(button3)

def make_button(text, data):
    x = IKB(text, callback_data=data)
    return x

MAIN = []

FIRST_ROW = []
SECOND_ROW = []
THIRD_ROW = []
FOURTH_ROW = []
FIFTH_ROW = []
SIXTH_ROW = []

main_back = make_button("Back", "main_back")
cmd_back = make_button("Back", "cmd_back")

# buttons

first1 = make_button("AFK", "afk_help")
first2 = make_button("Admins", "admins_help")
first3 = make_button("Anime", "anime_help")

second1 = make_button("Anime quotes", "aq_help")
second2 = make_button("Approval", "approval_help")
second3 = make_button("Auto correct", "ac_help")

third1 = make_button("Blacklist", "bl_help")
third2 = make_button("Chatbot", "cb_help")
third3 = make_button("Floods", "flood_help")

fourth1 = make_button("Filters", "filters_help")
fourth2 = make_button("Fun", "fun_help")
fourth3 = make_button("Logos", "logo_help")

fifth1 = make_button("Misc", "misc_help")
fifth2 = make_button("Utils", "utils_help")
fifth3 = make_button("Stickers", "stcikers_help")

sixth1 = make_button("Locks", "locks_help")
sixth2 = make_button("Welcome", "welcome_help")
sixth3 = make_button("Rules", "rules_help")

append_button(FIRST_ROW, first1, first2, first3)
append_button(SECOND_ROW, second1, second2, second3)
append_button(THIRD_ROW, third1, third2, third3)
append_button(FOURTH_ROW, fourth1, fourth2, fourth3)
append_button(FIFTH_ROW, fifth1, fifth2, fifth3)
append_button(SIXTH_ROW, sixth1, sixth2, sixth3)

MAIN.append(FIRST_ROW)
MAIN.append(SECOND_ROW)
MAIN.append(THIRD_ROW)
MAIN.append(FOURTH_ROW)
MAIN.append(FIFTH_ROW)
MAIN.append(SIXTH_ROW)
MAIN.append([main_back])

CMD = [[cmd_back]]

TEXT = "Help section !, choose from below buttons."

botname = None
botun = None

@Client.on_callback_query(filters.regex("main_back"))
async def main_back_cbq(_, q):
    m = q.message
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
    x = await get_served_users()
    x = len(x)
    await q.answer()
    media = IMP(STUFF.START_IMG, caption=START_TEXT.format(fn, botname, Upt, x))
    await q.edit_message_media(media, reply_markup=START_MARKUP)

@Client.on_callback_query(filters.regex("help") | filters.regex("cmd_back"))
async def helper_cbq(_, q):
    await q.answer()
    await q.edit_message_text(TEXT, reply_markup=IKM(MAIN))

@Client.on_callback_query(filters.regex("afk_help"))
async def afk_cbq(_, q):
    await q.answer()
    await q.edit_message_text(AFK_HELP, reply_markup=IKM(CMD))

@Client.on_callback_query(filters.regex("admins_help"))
async def admins_cbq(_, q):
    await q.answer()
    await q.edit_message_text(ADMIN_HELP, reply_markup=IKM(CMD))

@Client.on_callback_query(filters.regex("anime_help"))
async def anime_cbq(_, q):
    await q.answer()
    await q.edit_message_text(ANIME_HELP, reply_markup=IKM(CMD))

@Client.on_callback_query(filters.regex("aq_help"))
async def aq_cbq(_, q):
    await q.answer()
    await q.edit_message_text(ANIMEQUOTES_HELP, reply_markup=IKM(CMD))

@Client.on_callback_query(filters.regex("approval_help"))
async def approval_cbq(_, q):
    await q.answer()
    await q.edit_message_text(APPROVAL_HELP, reply_markup=IKM(CMD))

@Client.on_callback_query(filters.regex("ac_help"))
async def ac_cbq(_, q):
    await q.answer()
    await q.edit_message_text(AUTOCORRECT_HELP, reply_markup=IKM(CMD))

@Client.on_callback_query(filters.regex("bl_help"))
async def bl_cbq(_, q):
    await q.answer()
    await q.edit_message_text(BLACKLIST_HELP, reply_markup=IKM(CMD))

@Client.on_callback_query(filters.regex("cb_help"))
async def cb_cbq(_, q):
    await q.answer()
    await q.edit_message_text(CHATBOT_HELP, reply_markup=IKM(CMD))

@Client.on_callback_query(filters.regex("flood_help"))
async def flood_cbq(_, q):
    await q.answer()
    await q.edit_message_text(FLOOD_HELP, reply_markup=IKM(CMD))

@Client.on_callback_query(filters.regex("filters_help"))
async def filters_cbq(_, q):
    await q.answer()
    await q.edit_message_text(FILTERS_HELP, reply_markup=IKM(CMD))

@Client.on_callback_query(filters.regex("fun_help"))
async def fun_cbq(_, q):
    await q.answer()
    await q.edit_message_text(FUN_HELP, reply_markup=IKM(CMD))

@Client.on_callback_query(filters.regex("logo_help"))
async def logo_cbq(_, q):
    await q.answer()
    await q.edit_message_text(LOGO_HELP, reply_markup=IKM(CMD))

@Client.on_callback_query(filters.regex("misc_help"))
async def misc_cbq(_, q):
    await q.answer()
    await q.edit_message_text(MISC_HELP, reply_markup=IKM(CMD))

@Client.on_callback_query(filters.regex("utils_help"))
async def utils_cbq(_, q):
    await q.answer()
    await q.edit_message_text(UTILS_HELP, reply_markup=IKM(CMD))

@Client.on_callback_query(filters.regex("stickers_help"))
async def stickers_cbq(_, q):
    await q.answer()
    await q.edit_message_text(STICKERS_HELP, reply_markup=IKM(CMD))

@Client.on_callback_query(filters.regex("locks_help"))
async def locks_cbq(_, q):
    await q.answer()
    await q.edit_message_text(LOCKS_HELP, reply_markup=IKM(CMD))

@Client.on_callback_query(filters.regex("welcome_help"))
async def welcome_cbq(_, q):
    await q.answer()
    await q.edit_message_text(WELCOME_HELP, reply_markup=IKM(CMD))

@Client.on_callback_query(filters.regex("rules_help"))
async def rules_cbq(_, q):
    await q.answer()
    await q.edit_message_text(RULES_HELP, reply_markup=IKM(CMD))
