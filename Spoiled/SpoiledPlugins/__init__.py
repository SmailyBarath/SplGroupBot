async def get_id(_, m):
    try:
        if m.reply_to_message:
            id = m.reply_to_message.from_user.id
        else:
            txt = m.text.split()
            if txt[1][0] == "@":
                id = (await _.get_users(txt[1])).id
            else:
                id = int(txt[1])
    except:
        pass

async def log(_, id, message):
    try:
        await _.send_message(id, f"#LOGS\n\n{message}")
    except:
        pass
