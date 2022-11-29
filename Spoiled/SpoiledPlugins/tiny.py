import os
import cv2
from PIL import Image
from pyrogram import Client, filters


@Client.on_message(filters.command("tiny"))
async def tiny_rvrnt(_, m):
    if not m.reply_to_message:
        return await m.reply(f"**Reply to a sticker !**")
    if not m.reply_to_message.sticker:
        return await m.reply(f"**Reply to a sticker !**")
    kontol = await m.reply("`Processing tiny...`")
    ik = await m.reply_to_message.download()
    im1 = Image.open("Assets/ken.PNG")
    if ik.endswith(".tgs"):
        await _.download_media(m.reply_to_message, file_name="ken.tgs")
        os.system("lottie_convert.py downloads/ken.tgs json.json")
        json = open("json.json", "r")
        jsn = json.read()
        jsn = jsn.replace("512", "2000")
        open = ("json.json", "w").write(jsn)
        os.system("lottie_convert.py json.json downloads/ken.tgs")
        file = "downloads/ken.tgs"
        os.remove("json.json")
    elif ik.endswith((".gif", ".mp4")):
        iik = cv2.VideoCapture(ik)
        busy = iik.read()
        cv2.imwrite("i.png", busy)
        fil = "i.png"
        im = Image.open(fil)
        z, d = im.size
        if z == d:
            xxx, yyy = 200, 200
        else:
            t = z + d
            a = z / t
            b = d / t
            aa = (a * 100) - 50
            bb = (b * 100) - 50
            xxx = 200 + 5 * aa
            yyy = 200 + 5 * bb
        k = im.resize((int(xxx), int(yyy)))
        k.save("k.png", format="PNG", optimize=True)
        im2 = Image.open("k.png")
        back_im = im1.copy()
        back_im.paste(im2, (150, 0))
        back_im.save("o.webp", "WEBP", quality=95)
        file = "o.webp"
        os.remove(fil)
        os.remove("k.png")
    else:
        im = Image.open(ik)
        z, d = im.size
        if z == d:
            xxx, yyy = 200, 200
        else:
            t = z + d
            a = z / t
            b = d / t
            aa = (a * 100) - 50
            bb = (b * 100) - 50
            xxx = 200 + 5 * aa
            yyy = 200 + 5 * bb
        k = im.resize((int(xxx), int(yyy)))
        k.save("k.png", format="PNG", optimize=True)
        im2 = Image.open("k.png")
        back_im = im1.copy()
        back_im.paste(im2, (150, 0))
        back_im.save("o.webp", "WEBP", quality=95)
        file = "o.webp"
        os.remove("k.png")
    await m.reply_sticker(file)
    await kontol.delete()
    os.remove(file)
    os.remove(ik)
