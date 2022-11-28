import os
from asyncio import gather, get_running_loop
from base64 import b64decode
from io import BytesIO
from random import randint
from aiohttp import ClientSession as session
import aiofiles
import requests
from bs4 import BeautifulSoup
from pyrogram import filters, Client as app
from pyrogram.types import InputMediaPhoto, Message
from .chatbot import eor

MESSAGE_DUMP_CHAT = -1001898918828

async def get(url: str, *args, **kwargs):
    async with session.get(url, *args, **kwargs) as resp:
        try:
            data = await resp.json()
        except Exception:
            data = await resp.text()
    return data

def get_file_id_from_message(
        message,
        max_file_size=3145728,
        mime_types=["image/png", "image/jpeg"],
):
    file_id = None
    if message.document:
        if int(message.document.file_size) > max_file_size:
            return

        mime_type = message.document.mime_type

        if mime_types and mime_type not in mime_types:
            return
        file_id = message.document.file_id

    if message.sticker:
        if message.sticker.is_animated:
            if not message.sticker.thumbs:
                return
            file_id = message.sticker.thumbs[0].file_id
        else:
            file_id = message.sticker.file_id

    if message.photo:
        file_id = message.photo.file_id

    if message.animation:
        if not message.animation.thumbs:
            return
        file_id = message.animation.thumbs[0].file_id

    if message.video:
        if not message.video.thumbs:
            return
        file_id = message.video.thumbs[0].file_id
    return file_id

async def get_soup(url: str, headers):
    html = await get(url, headers=headers)
    return BeautifulSoup(html, "html.parser")

@app.on_message(filters.command("reverse"))
async def reverse_image_search(client, message: Message):
    if not message.reply_to_message:
        return await eor(
            message, text="Reply to a message to reverse search it."
        )
    reply = message.reply_to_message
    if (
            not reply.document
            and not reply.photo
            and not reply.sticker
            and not reply.animation
            and not reply.video
    ):
        return await eor(
            message,
            text="Reply to an image/document/sticker/animation to reverse search it.",
        )
    m = await eor(message, text="Searching...")
    file_id = get_file_id_from_message(reply)
    if not file_id:
        return await m.edit("Can't reverse that")
    image = await client.download_media(file_id, f"{randint(1000, 10000)}.jpg")
    async with aiofiles.open(image, "rb") as f:
        if image:
            search_url = "http://www.google.com/searchbyimage/upload"
            multipart = {
                "encoded_image": (image, await f.read()),
                "image_content": "",
            }

            def post_non_blocking():
                return requests.post(
                    search_url, files=multipart, allow_redirects=False
                )

            loop = get_running_loop()
            response = await loop.run_in_executor(None, post_non_blocking)
            location = response.headers.get("Location")
            os.remove(image)
        else:
            return await m.edit("Something wrong happened.")
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:58.0) Gecko/20100101 Firefox/58.0"
    }

    try:
        soup = await get_soup(location, headers=headers)
        div = soup.find_all("div", {"class": "r5a77d"})[0]
        text = div.find("a").text
        text = f"**Result**: [{text}]({location})"
    except Exception:
        return await m.edit(
            f"**Result**: [Link]({location})",
            disable_web_page_preview=True,
        )

    # Pass if no images detected
    try:
        url = "https://google.com" + soup.find_all(
            "a", {"class": "ekf0x hSQtef"}
        )[0].get("href")

        soup = await get_soup(url, headers=headers)

        media = []
        for img in soup.find_all("img"):
            if len(media) == 2:
                break

            if img.get("src"):
                img = img.get("src")
                if "image/gif" in img:
                    continue

                img = BytesIO(b64decode(img))
                img.name = "img.png"
                media.append(img)
            elif img.get("data-src"):
                img = img.get("data-src")
                media.append(img)

        # Cache images, so we can use file_ids
        tasks = [client.send_photo(MESSAGE_DUMP_CHAT, img) for img in media]
        messages = await gather(*tasks)

        await message.reply_media_group(
            [
                InputMediaPhoto(
                    i.photo.file_id,
                    caption=text,
                )
                for i in messages
            ]
        )
    except Exception:
        pass

    await m.edit(
        text,
        disable_web_page_preview=True,
    )
