from pyrogram import Client, filters
from Spoiled.Database.approve import *
from . import get_id, verify
from config import DEV
from pyrogram.types import InlineKeyboardButton as IKB, InlineKeyboardMarkup as IKM

DEV_USERS = DEV.SUDO_USERS + [DEV.OWNER_ID]

@Client.on_message(filters.command("approve"))
async def approve_user(_, m):
    user_id = m.from_user.id
    x, y = await verify(_, m)
    if not x:
        return await m.reply(y)
    try:
        id = await get_id(_, m)
    except:
        return await m.reply("Atleast reply to user or provide id !")
    if id in DEV_USERS:
        return await m.reply("Sudo users are already free from locks, blacklists, floods etc..!")
    j = await _.get_chat_member(m.chat.id, id)
    if j.status in ["creator", "administrator"]:
        return await m.reply("Admins are already free from locks, blacklists, flood etc..!")
    c = await is_approved(m.chat.id, id)
    fn = (await _.get_users(id)).first_name
    if c:
        return await m.reply(f"**{fn}** is already approved in **{m.chat.title}**")
    await approve(m.chat.id, id)
    await m.reply(f"**{fn}** is now approved in **{m.chat.title}**, they got no limitations !")

@Client.on_message(filters.command("disapprove"))
async def disapprove_user(_, m):
    user_id = m.from_user.id
    x, y = await verify(_, m)
    if not x:
        return await m.reply(y)
    try:
        id = await get_id(_, m)
    except:
        return await m.reply("Atleast reply to user or provide id !")
    lol = await is_approved(id)
    fn = (await _.get_users(id)).first_name
    if not lol:
        return await m.reply(f"**{fn}** wasn't approved in **{m.chat.title}**")
    await disapprove(m.chat.id, id)
    await m.reply(f"**{fn}** disapproved in **{m.chat.title}** !")

markup = IKM(
         [
         [
         IKB("Disapprove all", callback_data="disapprove_all")
         ]
         ]
         )

@Client.on_message(filters.command("approved"))
async def approved(_, m):
    x, y = await verify(_, m)
    if not x:
        return await m.reply(y)
    g = await get_approved(m.chat.id)
    if not g:
        return await m.reply(f"No approved users in **{m.chat.title}**")
    txt = f"**Approved users in {m.chat.title}**"
    txt += "\n\n"
    for j in g:
        txt += f"- `{j}`\n"
    await m.reply(txt, reply_markup=markup)
