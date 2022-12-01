from pyrogram import Client, filters
from String.start import START_TEXT, START_MARKUP
from config import STUFF
import time
from . import startTime, botname
from .afk import get_readable_time
from Spoiled.Database.users import get_served_users
from Spoiled.Database.pusers import add_served_puser

@Client.on_message(filters.command("start") & filters.group)
async def st(_, m):
    fn = m.from_user.first_name
    Upt = get_readable_time(int(time.time()-startTime))
    x = await get_served_users
    x = len(x)
    await add_served_puser(m.from_user.id)
    await m.reply_photo(STUFF.START_IMG, caption=START_TEXT.format(fn, botname, Upt, x), reply_markup=START_MARKUP)
