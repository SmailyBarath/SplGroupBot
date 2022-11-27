import psutil as p
from pyrogram import Client, filters

CPU = p.cpu_percent(3)
RAM_USED = str(p.virtual_memory()[3] / 10000000000)[0:4]
TOTAL_RAM = str(p.virtual_memory().total / 10000000000)[0:4]
RAM_USEDP = p.virtual_memory()[2]
IMG = "https://te.legra.ph/file/70ef0b7a6c8fece1a13c0.jpg"

txt = "\n"
txt += f"• **SYS NAME : Alpha's VPS**"
txt += "\n\n"
txt += f"• **OS : Linux's Ubuntu**"
txt += "\n\n"
txt += f"**• CPU : {CPU}%**"
txt += "\n\n"
txt += f"**• MEMORY USED : {RAM_USED}GB ({RAM_USEDP}%)**"
txt += "\n\n"
txt += f"**• MEMORY TOTAL (RAM) : {TOTAL_RAM}GB**"

@Client.on_message(filters.command("sysinfo"))
async def sysinfo(_, m):
    await m.reply_photo(IMG, caption=txt)
