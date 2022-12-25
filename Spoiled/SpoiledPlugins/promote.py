from config import DEV
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton as IKB, InlineKeyboardMarkup as IKM, ChatPrivileges
from . import get_id

DEV_USERS = DEV.SUDO_USERS + [DEV.OWNER_ID]

PRIVILEGES = []

BUTTONS = []

STATUS = ["❌", "❌", "❌", "❌", "❌", "❌", "❌"]

oper = None

target = None

def make():
    global BUTTONS
    BUTTONS = []
    a = 1
    for y in PRIVILEGES:
        if a == 8:
            break
        temp = []
        temp.append(IKB(y, callback_data=f"answer_{a}"))
        temp.append(IKB(STATUS[a-1], callback_data=f"right_{a}"))
        BUTTONS.append(temp)
        a += 1
    BUTTONS.append([IKB("Close 🗑️", callback_data="promote_close"), IKB("Save ✅", callback_data="promote_save")])
    return BUTTONS

@Client.on_message(filters.command("promote") & filters.group)
async def promote(_, m):
    global PRIVILEGES, BUTTONS, oper, STATUS, target
    PRIVILEGES = []
    BUTTONS = []
    STATUS = ["❌", "❌", "❌", "❌", "❌", "❌", "❌"]
    id = m.from_user.id
    if not id in DEV_USERS:
        x = await _.get_chat_member(m.chat.id, id)
        if not x.privileges:
            return await m.reply("You got no rights to do this !")
        if not x.privileges.can_promote_members:
            return await m.reply("You got no rights to do this !")
    oper = id
    id = (await _.get_me()).id
    x = await _.get_chat_member(m.chat.id, id)
    if not x.privileges:
        return await m.reply("I got no rights to do this !")
    if not x.privileges.can_promote_members:
        return await m.reply("I got no rights to do this !")
    try:
        id = await get_id(_, m)
        target = id
    except:
        return await m.reply("Either reply or give username !")
    x = x.privileges
    PRIVILEGES.append("Change Group Info")
    PRIVILEGES.append("Delete Messages")
    PRIVILEGES.append("Ban Users")
    PRIVILEGES.append("Invite Users")
    PRIVILEGES.append("Pin Messages")
    PRIVILEGES.append("Manage Video Chats")
    PRIVILEGES.append("Add New Admins")
    name = (await _.get_users(id)).first_name
    try:
        plate = m.text.split()[1]
    except:
        plate = "admin"
    buttons = make()
    txt = f"User : **{name}**\n\nTag : **{plate}**"
    await m.reply(txt, reply_markup=IKM(buttons))
  
@Client.on_callback_query(filters.regex("answer_1") | filters.regex("answer_2") | filters.regex("answer_3") | filters.regex("answer_4") | filters.regex("answer_5") | filters.regex("answer_6") | filters.regex("answer_7"))
async def answer_query(_, q):
    if q.data[0:6] == "answer":
        return await q.answer("Use buttons beside to toggle !", show_alert=True)

@Client.on_callback_query(filters.regex("right_1") | filters.regex("right_2") | filters.regex("right_3") | filters.regex("right_4") | filters.regex("right_5") | filters.regex("right_6") | filters.regex("right_7"))
async def right_query(_, q):
    global STATUS
    if q.from_user.id != oper:
        return await q.answer("This is not for you !")
    await q.answer()
    if q.data == "right_1":
        status = STATUS[0]
        if status == "❌":
            STATUS[0] = "✅"
        else:
            STATUS[0] = "❌"
        return await q.edit_message_reply_markup(reply_markup=IKM(make()))
    elif q.data == "right_2":
        status = STATUS[1]
        if status == "❌":
            STATUS[1] = "✅"
        else:
            STATUS[1] = "❌"
        return await q.edit_message_reply_markup(reply_markup=IKM(make()))
    elif q.data == "right_3":
        status = STATUS[2]
        if status == "❌":
            STATUS[2] = "✅"
        else:
            STATUS[2] = "❌"
        return await q.edit_message_reply_markup(reply_markup=IKM(make()))
    elif q.data == "right_4":
        status = STATUS[3]
        if status == "❌":
            STATUS[3] = "✅"
        else:
            STATUS[3] = "❌"
        return await q.edit_message_reply_markup(reply_markup=IKM(make()))
    elif q.data == "right_5":
        status = STATUS[4]
        if status == "❌":
            STATUS[4] = "✅"
        else:
            STATUS[4] = "❌"
        return await q.edit_message_reply_markup(reply_markup=IKM(make()))
    elif q.data == "right_6":
        status = STATUS[5]
        if status == "❌":
            STATUS[5] = "✅"
        else:
            STATUS[5] = "❌"
        return await q.edit_message_reply_markup(reply_markup=IKM(make()))
    elif q.data == "right_7":
        status = STATUS[7]
        if status == "❌":
            STATUS[7] = "✅"
        else:
            STATUS[7] = "❌"
        return await q.edit_message_reply_markup(reply_markup=IKM(make()))

@Client.on_callback_query(filters.regex("promote_close"))
async def closer(_, q):
    if q.from_user.id != oper:
        return await q.answer()
    await q.answer()
    await q.message.delete()

@Client.on_callback_query(filters.regex("promote_save"))
async def saver(_, q):
    if q.from_user.id != oper:
        return await q.answer()
    await q.answer()
    NOW = []
    for t in STATUS:
        h = True if t == "✅" else False
        NOW.append(h)
    try:
        await _.promote_chat_member(q.message.chat.id, target, ChatPrivileges(can_change_info=NOW[0], can_delete_messages=NOW[1], can_restrict_members=NOW[2], can_invite_users=NOW[3], can_pin_messages=NOW[4], can_manage_video_chats=NOW[5], can_promote_members=NOW[6]))
        await q.edit_message_text("Promoted successfully !")
    except Exception as e:
        await q.edit_message_text(e)
    
