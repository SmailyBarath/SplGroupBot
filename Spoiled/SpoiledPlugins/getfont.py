from pyrogram import filters, Client as pbot

ALPHABETS = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

SERIF = "𝐀𝐁𝐂𝐃𝐄𝐅𝐆𝐇𝐈𝐉𝐊𝐋𝐌𝐍𝐎𝐏𝐐𝐑𝐒𝐓𝐔𝐕𝐖𝐗𝐘𝐙"

ALLCAPS = "ᴀʙᴄᴅᴇғɢʜɪᴊᴋʟᴍɴᴏᴘǫʀsᴛᴜᴠᴡxʏᴢ"

@pbot.on_message(filters.command("getfont"))
async def fg(_, m):
    if len(m.command) < 2:
        return await m.reply("give some text bruh !🥲")
    s = m.text.split(None, 1)[1]
    x = []
    for y in s:
        for z in y:
            if z.lower() in ALPHABETS:
                x.append(y)
    txt = ""
    for z in x:
        cnt = 0
        for a in z:
            ind = ALPHABETS.index(a)
            if cnt == 0:
                txt += SERIF[ind]
                cnt += 1
            else:
                txt += ALLCAPS[ind]
                cnt += 1

    await m.reply(txt)
