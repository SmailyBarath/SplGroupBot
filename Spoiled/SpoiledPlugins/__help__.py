from pyrogram.types import InlineKeyboardButton as IKB, InlineKeyboardMarkup as IKM
from Strings.help import * 
from pyrogram import Client

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

TEXT = "Help section !, choose from below buttons."

@Client.on_callback_query(filters.regex("help"))
async def helper_cbq(_, q):
    await q.answer()
    await q.edit_message_text(TEXT)
    await q.edit_message_reply_markup(reply_markup=IKM(MAIN))
