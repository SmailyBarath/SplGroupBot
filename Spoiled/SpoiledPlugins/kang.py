from telegram import Update
from telegram.ext import CallbackContext, CommandHandler

async def kang(u: Update, c: CallbackContext):
    try:
        m = u.effective_message
        user = u.effective_user
        emoji = m.text.split()[1] if len(m.command) > 1 else "💭"
        title = f"{m.from_user.first_name}'s pack by @{c.bot.username}"
        if not m.reply_to_message:
            return await m.reply_text("Reply to an image or sticker !")
        if not m.reply_to_message.photo and not m.reply_to_message.sticker:
            return await m.reply_text("Reply to an image or a sticker !")
        if m.reply_to_message.photo:
            file_id = m.reply_to_message.photo[-1].file_id
            get_file = await c.bot.get_file(file_id)
            await get_file.download("yashu.png")
            resize("yashu.png")
            x = "yashu.png"
            format = "normal"
            png = True
        else:
            png = False
            if m.reply_to_message.sticker.is_video:
                format = "video"
            elif m.reply_to_message.sticker.is_animated:
                format = "animated"
            else:
                format = "normal"
            sticid = m.reply_to_message.sticker.file_id
            if format == "video" or format == "animated":
                get_file = await c.bot.get_file(sticid)
                x = await get_file.download()
            
            alpha = True   
            pack = 1
            name = f"YashuAlpha_{user.id}_{format}{pack}_by_{c.bot.username}"
            try:
                while alpha:
                    v = await c.bot.get_sticker_set(name)
                    stics = len(v.stickers)
                    if format == "video" or format == "animated":
                        if stics == 50:
                            pack += 1
                    else:
                        if stics == 120:
                            pack += 1
                    if stics > 0:
                        if format == "video":
                            await c.bot.add_sticker_to_set(user_id=user.id, name=pack_name, emojis=emoji, webm_sticker=open(x, "rb"))
                        elif format == "animated":
                            await c.bot.add_sticker_to_set(user_id=user.id, name=pack_name, emojis=emoji, tgs_sticker=open(x, "rb"))
                        else:
                            await c.bot.add_sticker_to_set(user_id=user.id, name=pack_name, emojis=emoji, png_sticker=open(x, "rb") if png else sticid)                                  
            except:
                if format == "video":
                    await c.bot.create_new_sticker_set(user_id=user.id, name=name, title=title, emojis=emoji, webm_sticker=open(x, "rb"))
                elif format == "animated":
                    await c.bot.create_new_sticker_set(user_id=user.id, name=name, title=title, emojis=emoji, tgs_sticker=open(x, "rb"))
                else:
                    await c.bot.create_new_sticker_set(user_id=user.id, name=name, title=title, emojis=emoji, png_sticker=open(x, "rb") if png else sticid)

            await m.reply_text(f"Sticker is added to set\n\nEmoji : {emoji}", reply_markup=markup)

    except Exception as e:
        await m.reply_text("An unknown error occurred, 
                
            
