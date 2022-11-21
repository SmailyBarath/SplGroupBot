from config import DEV
from pyrogram import Client as Yashu, filters

from . import get_id

async def ban_user(_, m):
    try:
        x = await get_id(_, m)
        if x in DEV.SUDO_USERS:
            return False, "Sudo user can't get banned !"
        y = await _.get_chat_member(m.chat.id, x)
        if y.status == "creator":
            return False, "Can't ban chat owner !"
        if y.status == "administrator":
            return False, "Can't ban admin !"
        if y.status == "banned":
            return False, "User already banned !"
        await _.ban_user(m.chat.id, x)
        return True, False
    except Exception as e:
        return False, e

async def unban_user(_, m):
    try:
        x = await get_id(_, m)
        y = await _.get_chat_member(m.chat.id, x)
        if y.status != "banned":
            return False, "User is not banned !"
        await _.unban_user(m.chat.id, x)
        return True, False
    except Exception as e:
        return False, e

@Yashu.on_message(filters.command(["ban", "unban"]))
async def ban_unban(_, m):
    try:
        user_id = m.from_user.id
        chat_id = m.chat.id
        is_sudo = True if user_id in DEV.SUDO_USERS else False
        if not is_sudo:
            x = await _.get_chat_member(chat_id, user_id)
            if not x.status in ["creator", "administrator"]:
                return await m.reply("you need to be admin to do this !")
            if not x.can_restrict_members:
                return await m.reply("you don't have to right to perform this action !")
            if m.text.split(0)[1].lower() == "u":
                unbanned, optional = await unban_user(_, m)
                if not unbanned:
                    return await m.reply(optional)
                return await m.reply("User unbanned !")
            banned, optional = await ban_user(_, m)
            if not banned:
                return await m.reply(optional)
            men = (await _.get_users(await get_id(_, m))).mention
            return await m.reply(f"{men} banned !")
        else:
            if m.text.split(0)[1].lower() == "u":
                unbanned, optional = await unban_user(_, m)
                if not unbanned:
                    return await m.reply(optional)
                return await m.reply("User unbanned !")
            banned, optional = await ban_user(_, m)
            if not banned:
                return await m.reply(optional)
            men = (await _.get_users(await get_id(_, m))).mention
            return await m.reply(f"{men} banned !")
