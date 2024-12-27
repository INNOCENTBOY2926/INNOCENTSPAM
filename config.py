import logging

from telethon import TelegramClient

from os import getenv
from AltBots.data import ALTRON


logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s', level=logging.WARNING)


# VALUES REQUIRED FOR XBOTS
API_ID = "17763538"
API_HASH = "babad31b4b434fc53d8bd13370c556c3"
CMD_HNDLR = getenv("CMD_HNDLR", default=".")

HEROKU_APP_NAME = getenv("HEROKU_APP_NAME", None)
HEROKU_API_KEY = getenv("HEROKU_API_KEY", None)

BOT_TOKEN = getenv("BOT_TOKEN", default=6389757539:AAH76tc3ciBYp5mwVKLhgGaikIMGxuB6BLU)
BOT_TOKEN2 = getenv("BOT_TOKEN2", default=7161092813:AAGYddMKYdPNScDc8SEaAw9__Gs_A4jfwyI)
BOT_TOKEN3 = getenv("BOT_TOKEN3", default=7088474629:AAHtRuDXtrZv4l66Op6aAAzLv5z80TzfKZ0)
BOT_TOKEN4 = getenv("BOT_TOKEN4", default=6956089230:AAH8SEYTPMgTZ_to22NB79x7wnkaNbbksc8)
BOT_TOKEN5 = getenv("BOT_TOKEN5", default=7029167424:AAGdndM9LsvQGewRYaYghEczt7dMDUbD9ak)
BOT_TOKEN6 = getenv("BOT_TOKEN6", default=7103801898:AAEq7mEfQzspoVm-sx_EymJ418ipE043y5U)
BOT_TOKEN7 = getenv("BOT_TOKEN7", default=6422267508:AAEBgbHrBiAj7pgxrPHntb6W6rJll_po4F4)
BOT_TOKEN8 = getenv("BOT_TOKEN8", default=7071102149:AAEESaHQgwVwrDmP53QXB88tgm6V6xFMr8Q)
BOT_TOKEN9 = getenv("BOT_TOKEN9", default=6511740403:AAHGJoyxJngS_ewWEPCpzl4-zch8mDRVj9Q)
BOT_TOKEN10 = getenv("BOT_TOKEN10", default=7048430778:AAG_O7YmnLGd2cCqUTtrkpMV68dn3Cmpnvw)

SUDO_USERS = list(map(lambda x: int(x), getenv("SUDO_USERS", default="7493386583").split()))
for x in ALTRON:
    SUDO_USERS.append(x)
OWNER_ID = int(getenv("OWNER_ID", default="6961211249"))
SUDO_USERS.append(OWNER_ID)


# ------------- CLIENTS -------------

X1 = TelegramClient('X1', API_ID, API_HASH).start(bot_token=BOT_TOKEN)
X2 = TelegramClient('X2', API_ID, API_HASH).start(bot_token=BOT_TOKEN2)
X3 = TelegramClient('X3', API_ID, API_HASH).start(bot_token=BOT_TOKEN3)
X4 = TelegramClient('X4', API_ID, API_HASH).start(bot_token=BOT_TOKEN4)
X5 = TelegramClient('X5', API_ID, API_HASH).start(bot_token=BOT_TOKEN5)
X6 = TelegramClient('X6', API_ID, API_HASH).start(bot_token=BOT_TOKEN6)
X7 = TelegramClient('X7', API_ID, API_HASH).start(bot_token=BOT_TOKEN7)
X8 = TelegramClient('X8', API_ID, API_HASH).start(bot_token=BOT_TOKEN8)
X9 = TelegramClient('X9', API_ID, API_HASH).start(bot_token=BOT_TOKEN9)
X10 = TelegramClient('X10', API_ID, API_HASH).start(bot_token=BOT_TOKEN10)
