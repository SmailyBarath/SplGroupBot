# MODULE VERIFIED BY @NORTH_YANKTON

from Spoiled.Database.couples import get_couple, save_couple, del_couple
from pyrogram import filters, Client as app
import random
from datetime import datetime
from . import log, SUPPORT_CHAT_MARKUP
from config import DEV

YASHUALPHA = DEV.SUDO_USERS + [DEV.OWNER_ID]

# Date and time
def dt():
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M")
    dt_list = dt_string.split(" ")
    return dt_list


def dt_tom():
    a = (
        str(int(dt()[0].split("/")[0]) + 1)
        + "/"
        + dt()[0].split("/")[1]
        + "/"
        + dt()[0].split("/")[2]
    )
    return a


today = str(dt()[0])
tomorrow = str(dt_tom())

@app.on_message(filters.command("delcouple") & filters.user(YASHUALPHA))
async def delc(_, m):
    try:
        id = int(m.text.split()[1])
    except Exception as e:
        await m.reply(e)
        return
    try:
        await del_couple(id)
        await m.reply("DELETED !")
    except Exception as e:
        await m.reply(e)

@app.on_message(filters.command("setcouple") & filters.user(YASHUALPHA))
async def sec(_, m):
    try:
        chat_id = int(m.text.split()[3])
    except Exception as e:
        return await m.reply(e)
    is_selected = await get_couple(chat_id, today)
    if not is_selected:
        try:
            c1_id = int(m.text.split()[1])
            c2_id = int(m.text.split()[2])
        except:
            try:
                c1_un = m.text.split()[1]
                c2_un = m.text.split()[2]
                c1_id = (await _.get_users(c1_un)).id
                c2_id = (await _.get_users(c2_un)).id
            except Exception as e:
                return await m.reply(e)
        
        
        c1_mention = (await _.get_users(c1_id)).mention
        c2_mention = (await _.get_users(c2_id)).mention

        couple_selection_message = f"""**Couple of the day:**

{c1_mention} + {c2_mention} = ❤️
__New couple of the day may be chosen at 12AM {tomorrow}__"""
        await _.send_message(m.chat.id, text=couple_selection_message)
        couple = {"c1_id": c1_id, "c2_id": c2_id}
        await save_couple(chat_id, today, couple)
    else:
        await m.reply("TODAY'S COUPLE SELECTED {}".format("ALPHA" if m.from_user.id == YASHUALPHA[0] else "YASHU"))

@app.on_message(filters.command("couples"))
async def couple(_, message):
    if message.chat.type == "private":
        await message.reply_text("This command only works in groups.")
        return
    try:
        chat_id = message.chat.id
        is_selected = await get_couple(chat_id, today)
        if not is_selected:
            list_of_users = []
            async for i in _.get_chat_members(message.chat.id):
                if not i.user.is_bot:
                    list_of_users.append(i.user.id)
            if len(list_of_users) < 2:
                await message.reply_text("Not enough users")
                return
            c1_id = random.choice(list_of_users)
            c2_id = random.choice(list_of_users)
            while c1_id == c2_id:
                c1_id = random.choice(list_of_users)
            c1_mention = (await _.get_users(c1_id)).mention
            c2_mention = (await _.get_users(c2_id)).mention

            couple_selection_message = f"""**Couple of the day:**

{c1_mention} + {c2_mention} = ❤️
__New couple of the day may be chosen at 12AM {tomorrow}__"""
            await _.send_message(message.chat.id, text=couple_selection_message)
            couple = {"c1_id": c1_id, "c2_id": c2_id}
            await save_couple(chat_id, today, couple)

        elif is_selected:
            c1_id = int(is_selected["c1_id"])
            c2_id = int(is_selected["c2_id"])
            c1_name = (await _.get_users(c1_id)).mention
            c2_name = (await _.get_users(c2_id)).mention
            couple_selection_message = f"""**Couple of the day:**

{c1_name} + {c2_name} = ❤️
__New couple of the day may be chosen at 12AM {tomorrow}__"""
            await _.send_message(message.chat.id, text=couple_selection_message)
    except Exception as e:
        await message.reply("An exception occurred, consider support !", reply_markup=SUPPORT_CHAT_MARKUP)
        await log(_, e)
        
