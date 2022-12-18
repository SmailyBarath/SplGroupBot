from .chatbot import aiohttpsession as session
import speedtest
import datetime
from pytube import YouTube
from yashu import spoil as app
from typing import List, Optional, Union
import pyrogram
from pyrogram import raw, types, utils
from pyrogram.file_id import DOCUMENT_TYPES, PHOTO_TYPES, FileId, FileType
from pyrogram.types import InlineQueryResult
from asyncio import Lock, create_task
from time import time
from pyrogram import filters
from pyrogram.types import Message
from pykeyboard import InlineKeyboard
from pyrogram.types import InlineKeyboardButton as Ikb
from re import findall

def is_url(text: str) -> bool:
    regex = r"""(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]
                [.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(
                \([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\
                ()<>]+\)))*\)|[^\s`!()\[\]{};:'".,<>?«»“”‘’]))""".strip()
    return [x[0] for x in findall(regex, str(text))]

def keyboard(buttons_list, row_width: int = 2):
    """
    Buttons builder, pass buttons in a list and it will
    return pyrogram.types.IKB object
    Ex: keyboard([["click here", "https://google.com"]])
    if theres, a url, it will make url button, else callback button
    """
    buttons = InlineKeyboard(row_width=row_width)
    data = [
        (
            Ikb(text=str(i[0]), callback_data=str(i[1]))
            if not is_url(i[1])
            else Ikb(text=str(i[0]), url=str(i[1]))
        )
        for i in buttons_list
    ]
    buttons.add(*data)
    return buttons


def ikb(data: dict, row_width: int = 2):
    """
    Converts a dict to pyrogram buttons
    Ex: dict_to_keyboard({"click here": "this is callback data"})
    """
    return keyboard(data.items(), row_width=row_width)

n = "\n"
w = " "

bold = lambda x: f"**{x}:** "
bold_ul = lambda x: f"**--{x}:**-- "

mono = lambda x: f"`{x}`{n}"

def section(
        title: str,
        body: dict,
        indent: int = 2,
        underline: bool = False,
) -> str:
    text = (bold_ul(title) + n) if underline else bold(title) + n

    for key, value in body.items():
        text += (
                indent * w
                + bold(key)
                + ((value[0] + n) if isinstance(value, list) else mono(value))
        )
    return text

tasks = {}
TASKS_LOCK = Lock()
arrow = lambda x: (x.text if x else "") + "\n`→`"


def all_tasks():
    return tasks


async def add_task(
        taskFunc,
        task_name,
        *args,
        **kwargs,
):
    async with TASKS_LOCK:
        global tasks

        task_id = (list(tasks.keys())[-1] + 1) if tasks else 0

        task = create_task(
            taskFunc(*args, **kwargs),
            name=task_name,
        )
        tasks[task_id] = task, int(time())
    return task, task_id


async def rm_task(task_id=None):
    global tasks

    async with TASKS_LOCK:
        for key, value in list(tasks.items()):
            if value[0].done() or value[0].cancelled():
                del tasks[key]

        if (task_id is not None) and (task_id in tasks):
            task = tasks[task_id][0]

            if not task.done():
                task.cancel()

            del tasks[task_id]


async def _get_tasks_text():
    await rm_task()  # Clean completed tasks
    if not tasks:
        return f"{arrow('')} No pending task"

    text = bold("Tasks") + "\n"

    for i, task in enumerate(list(tasks.items())):
        indent = w * 4

        t, started = task[1]
        elapsed = round(time() - started)
        info = t._repr_info()

        id = task[0]
        text += section(
            f"{indent}Task {i}",
            body={
                "Name": t.get_name(),
                "Task ID": id,
                "Status": info[0].capitalize(),
                "Origin": info[2].split("/")[-1].replace(">", ""),
                "Running since": f"{elapsed}s",
            },
            indent=8,
        )
    return text

class InlineQueryResultCachedDocument(InlineQueryResult):
    def __init__(
            self,
            file_id: str,
            title: str = None,
            id: str = None,
            description: str = None,
            caption: str = "",
            parse_mode: Optional[str] = object,
            caption_entities: List["types.MessageEntity"] = None,
            reply_markup: "types.InlineKeyboardMarkup" = None,
            input_message_content: "types.InputMessageContent" = None,
    ):
        super().__init__("file", id, input_message_content, reply_markup)

        self.file_id = file_id
        self.title = title
        self.description = description
        self.caption = caption
        self.caption_entities = caption_entities
        self.parse_mode = parse_mode
        self.reply_markup = reply_markup
        self.input_message_content = input_message_content

    async def write(self, client: "pyrogram.Client"):
        document = get_input_file_from_file_id(self.file_id)

        message, entities = (
            await utils.parse_text_entities(
                client,
                self.caption,
                self.parse_mode,
                self.caption_entities,
            )
        ).values()

        return raw.types.InputBotInlineResultDocument(
            id=self.id,
            type=self.type,
            title=self.title,
            description=self.description,
            document=document,
            send_message=(
                await self.input_message_content.write(
                    client, self.reply_markup
                )
                if self.input_message_content
                else raw.types.InputBotInlineMessageMediaAuto(
                    reply_markup=await self.reply_markup.write(client)
                    if self.reply_markup
                    else None,
                    message=message,
                    entities=entities,
                )
            ),
        )

def download_youtube_audio(arq_resp):
    r = arq_resp.result[0]

    title = r.title
    performer = r.channel

    m, s = r.duration.split(":")
    duration = int(
        datetime.timedelta(minutes=int(m), seconds=int(s)).total_seconds()
    )

    if duration > 1800:
        return

    thumb = get(r.thumbnails[0]).content
    with open("thumbnail.png", "wb") as f:
        f.write(thumb)
    thumbnail_file = "thumbnail.png"

    url = f"https://youtube.com{r.url_suffix}"
    yt = YouTube(url)
    audio = yt.streams.filter(only_audio=True).get_audio_only()

    out_file = audio.download()
    base, _ = os.path.splitext(out_file)
    audio_file = base + ".mp3"
    os.rename(out_file, audio_file)

    return [title, performer, duration, audio_file, thumbnail_file]

async def post(url: str, *args, **kwargs):
    async with session.post(url, *args, **kwargs) as resp:
        try:
            data = await resp.json()
        except Exception:
            data = await resp.text()
    return data

BASE = "https://batbin.me/"

async def paste(content: str):
    resp = await post(f"{BASE}api/v2/paste", data=content)
    if not resp["success"]:
        return
    return BASE + resp["message"]

def test_speedtest():
    def speed_convert(size):
        power = 2 ** 10
        zero = 0
        units = {0: "", 1: "Kb/s", 2: "Mb/s", 3: "Gb/s", 4: "Tb/s"}
        while size > power:
            size /= power
            zero += 1
        return f"{round(size, 2)} {units[zero]}"

    speed = speedtest.Speedtest()
    info = speed.get_best_server()
    download = speed.download()
    upload = speed.upload()
    return [speed_convert(download), speed_convert(upload), info]

async def get_user_info(user, already=False):
    if not already:
        user = await app.get_users(user)
    if not user.first_name:
        return ["Deleted account", None]
    user_id = user.id
    username = user.username
    first_name = user.first_name
    mention = user.mention("Link")
    dc_id = user.dc_id
    photo_id = user.photo.big_file_id if user.photo else None
    is_gbanned = await is_gbanned_user(user_id)
    is_sudo = user_id in SUDOERS
    karma = await user_global_karma(user_id)
    body = {
        "ID": user_id,
        "DC": dc_id,
        "Name": [first_name],
        "Username": [("@" + username) if username else "Null"],
        "Mention": [mention],
        "Sudo": is_sudo,
        "Karma": karma,
        "Gbanned": is_gbanned,
    }
    caption = section("User info", body)
    return [caption, photo_id]


async def get_chat_info(chat, already=False):
    if not already:
        chat = await app.get_chat(chat)
    chat_id = chat.id
    username = chat.username
    title = chat.title
    type_ = chat.type
    is_scam = chat.is_scam
    description = chat.description
    members = chat.members_count
    is_restricted = chat.is_restricted
    link = f"[Link](t.me/{username})" if username else "Null"
    dc_id = chat.dc_id
    photo_id = chat.photo.big_file_id if chat.photo else None
    body = {
        "ID": chat_id,
        "DC": dc_id,
        "Type": type_,
        "Name": [title],
        "Username": [("@" + username) if username else "Null"],
        "Mention": [link],
        "Members": members,
        "Scam": is_scam,
        "Restricted": is_restricted,
        "Description": [description],
    }
    caption = section("Chat info", body)
    return [caption, photo_id]
