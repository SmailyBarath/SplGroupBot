from config import TOKENS
from aiohttp import ClientSession
from Python_ARQ import ARQ

ARQ_API_KEY = TOKENS.ARQ_API_KEY
ARQ_API_URL = "https://arq.hamker.in"

aiohttpsession = ClientSession()

arq = ARQ(ARQ_API_URL, ARQ_API_KEY, aiohttpsession)
