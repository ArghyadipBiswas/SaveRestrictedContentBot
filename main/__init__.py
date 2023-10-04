#Github.com/Vasusen-code

from pyrogram import Client

from telethon.sessions import StringSession
from telethon.sync import TelegramClient

from decouple import config
import logging, time, sys

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# variables
API_ID = 6235351
API_HASH = "f68fde1378da8f85a243f2ae57f2fcf9"
BOT_TOKEN = 5378163079:AAHhtCs9RPaEmux-UAiQOo7KVDmFRwMnd4o
SESSION = "BABfJNcAECJA_2mE1graeYTqIO2cQTe26JkE0VuKCGljRFV3_92UmLhdV7LbhJFBFfTvwARMS3aGzSGL6wA0XitmnnEYDVhXzF3oIzdpDcXIQmD2DfDdY2uCPO7qsKJthjkvRcPzkXwWQDDqE1S_UJtvxYApt2ypNMlFmOIGmahxqfSFU0maoaDGGgDqh6gOj1xTG2Jy_DIShdMtz4P77elfVJdgijBaLMi-HILApZ2qV-u5ctP8nmhhtOLOYE5W0aRN9cN2KTJjQJNHo0Kq471FXj8IZu4yQf--C0iCWi2MlVRAaMLBsFiYT7dG9QR8iR7NYnz-7jw8xrRTadBM_soTxFy7RgAAAAEsjtP5AA"
FORCESUB = "nub696"
AUTH = 5042525177

bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN) 

userbot = Client("saverestricted", session_string=SESSION, api_hash=API_HASH, api_id=API_ID) 

try:
    userbot.start()
except BaseException:
    print("Userbot Error ! Have you added SESSION while deploying??")
    sys.exit(1)

Bot = Client(
    "SaveRestricted",
    bot_token=BOT_TOKEN,
    api_id=int(API_ID),
    api_hash=API_HASH
)    

try:
    Bot.start()
except Exception as e:
    print(e)
    sys.exit(1)
