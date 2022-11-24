from telegram.ext import ApplicationBuilder
from config import TOKENS

Yashu = ApplicationBuilder().token(TOKENS.BOT_TOKEN).build()
