# Copyright (c) 2025 devgagan : https://github.com/devgaganin.  
# Licensed under the GNU General Public License v3.0.  
# See LICENSE file in the repository root for full license text.

import os
from dotenv import load_dotenv

load_dotenv()

# VPS --- FILL COOKIES 🍪 in """ ... """ 

INST_COOKIES = """
# wtite up here insta cookies
"""

YTUB_COOKIES = """
# write here yt cookies
"""

API_ID = os.getenv("API_ID", "22844653")
API_HASH = os.getenv("API_HASH", "9a656406da0a7a661348cd56a824f076")
BOT_TOKEN = os.getenv("BOT_TOKEN", "7009285082:AAEtuj2aLvlaebPQ3G0zKbU3CLWhgS3F2X8")
MONGO_DB = os.getenv("MONGO_DB", "oes23.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
OWNER_ID = list(map(int, os.getenv("OWNER_ID", "8048617293").split())) # list seperated via space
DB_NAME = os.getenv("DB_NAME", "ajflixhubsssssssss")
STRING = os.getenv("STRING", None) # optional
LOG_GROUP = int(os.getenv("LOG_GROUP", "-1002796162256")) # optional with -100
FORCE_SUB = int(os.getenv("FORCE_SUB", "-1002667336999")) # optional with -100
MASTER_KEY = os.getenv("MASTER_KEY", "gK8HzLfT9QpViJcYeB5wRa3DmN7P2xUq") # for session encryption
IV_KEY = os.getenv("IV_KEY", "s7Yx5CpVmE3F") # for decryption
YT_COOKIES = os.getenv("YT_COOKIES", YTUB_COOKIES)
INSTA_COOKIES = os.getenv("INSTA_COOKIES", INST_COOKIES)
FREEMIUM_LIMIT = int(os.getenv("FREEMIUM_LIMIT", "1500"))
PREMIUM_LIMIT = int(os.getenv("PREMIUM_LIMIT", "5000000"))
JOIN_LINK = os.getenv("JOIN_LINK", "https://t.me/Aj_Flix_Hub") # this link for start command message
ADMIN_CONTACT = os.getenv("ADMIN_CONTACT", "https://t.me/ajaytrams")

