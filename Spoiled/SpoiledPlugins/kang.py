from telegram import Update
from telegram.ext import CallbackContext, CommandHandler
from . import SUPPORT_CHAT_MARKUP as support_markup, single_button_maker, triple_button_maker
from PIL import Image
from Spoiled import Yashu
from . import log
from config import CHATS

def resize(kangsticker):
     im = Image.open(kangsticker)
     maxsize = (512, 512)
     if (im.width and im.height) < 512:
         size1 = im.width
         size2 = im.height
         if im.width > im.height:
             scale = 512 / size1
             size1new = 512
             size2new = size2 * scale
         else:
             scale = 512 / size2
             size1new = size1 * scale
             size2new = 512
         size1new = math.floor(size1new)
         size2new = math.floor(size2new)
         sizenew = (size1new, size2new)
         im = im.resize(sizenew)
     else:
         im.thumbnail(maxsize)
     im.save(kangsticker, "PNG")

async def kang(u: Update, c: CallbackContext):
    try:
        m = u.effective_message
        user = u.effective_user
        mark_name = "YashuAlpha_{}_{}1_by_" + c.bot.username
        pack_link = f"https://t.me/addstickers/{mark_name}"
        kang_markup = triple_button_maker(["Static pack", pack_link.format(user.id, "normal")], ["Animated pack", pack_link.format(user.id, "animated")], ["Video pack", pack_link.format(user.id, "video")])
        emoji = m.text.split()[1] if c.args else "💭"
        title = f"{user.first_name}'s pack by @{c.bot.username}"
        if not m.reply_to_message:
            return await m.reply_text("Reply to an image or sticker !", reply_markup=kang_markup)
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
            markup = single_button_maker("Pack ✨💭", f"https://t.me/addstickers/{name}")
            await m.reply_text(f"Sticker is added to set\n\nEmoji : {emoji}", reply_markup=markup)

    except Exception as e:
        if "blocked" in str(e):
            return await m.reply_text("Start me in pm !", reply_markup=single_button_maker("Start !", f"https://t.me/{c.bot.username}"))
        await m.reply_text("An unknown error occurred, consider support !", reply_markup=support_markup)
        print(e)
                
      
async def del_sticker(u: Update, c: CallbackContext):
    m = u.effective_message
    user = u.effective_user
    if not user.id in SUDO_USERS:
        return
    if not m.reply_to_message:
        return await m.reply_text("reply to a stixker vruh! ")
    if not m.reply_to_message.sticker:
        return await m.reply_text("reply to a stixker vruh! ")
    try:
        await c.bot.delete_sticker_from_set(m.reply_to_message.sticker.file_id)
        await m.reply_text("deleted !")
    except Exception as e:
        await m.reply_text(f"can't delete.. \n\n{e}")

Yashu.add_handler(CommandHandler("kang", kang))
Yashu.add_handler(CommandHandler("delsticker", del_sticker))
