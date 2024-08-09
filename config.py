import re
import os
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# Get this value from my.telegram.org/apps
API_ID = int(getenv("25064357"))
API_HASH = getenv("cda9f1b3f9da4c0c93d1f5c23ccb19e2")

# Get your token from @BotFather on Telegram.
BOT_TOKEN = getenv("7262095494:AAFclA3a3SDbyFkedrnQcg5g2lZF87vTUI8")

# Get your mongo url from cloud.mongodb.com
MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://tanjiro1564:tanjiro1564@cluster0.pp5yz4e.mongodb.net/?retryWrites=true&w=majorit")
MUSIC_BOT_NAME = getenv("MUSIC_BOT_NAME", "𝐒𝐎𝐔𝐋 𝐒𝐔𝐏𝐑𝐄𝐌𝐄『 魂 』")
PRIVATE_BOT_MODE = getenv("PRIVATE_BOT_MODE", None)

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 900))

# Chat id of a group for logging bot's activities
LOGGER_ID = int(getenv("LOGGER_ID", "-1002125082441)"))
LOG_GROUP_ID = int(getenv("LOG_GROUP_ID", "-1002125082441"))

# Get this value from @BRANDRD_ROBOT on Telegram by /id
OWNER_ID = int(getenv("1886390680"))

## Fill these variables if you're deploying on heroku.
# Your heroku app name
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
# Get it from http://dashboard.heroku.com/account
HEROKU_API_KEY = getenv("HEROKU_API_KEY")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/SARKAROP123/BRANDEDUPDATE-",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "main")
GIT_TOKEN = getenv(
    "GIT_TOKEN", None
)  # Fill this variable if your upstream repository is private

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/SOUL_NETWORKS")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/+ccW-DeShJpw4OWZl")

# Set this to True if you want the assistant to automatically leave chats after an interval
AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", False))

# Auto Gcast/Broadcast Handler (True = broadcast on , False = broadcast off During Hosting, Dont Do anything here.)
AUTO_GCAST = os.getenv("AUTO_GCAST")

# Auto Broadcast Message That You Want Use In Auto Broadcast In All Groups.
AUTO_GCAST_MSG = getenv("AUTO_GCAST_MSG", "")

# Get this credentials from https://developer.spotify.com/dashboard
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", "bcfe26b0ebc3428882a0b5fb3e872473")
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", "907c6a054c214005aeae1fd752273cc4")


# Maximum limit for fetching playlist's track from youtube, spotify, apple links.
SERVER_PLAYLIST_LIMIT = int(getenv("SERVER_PLAYLIST_LIMIT", "50"))
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", "25"))

SONG_DOWNLOAD_DURATION = int(getenv("SONG_DOWNLOAD_DURATION_LIMIT", "180"))
SONG_DOWNLOAD_DURATION_LIMIT = int(getenv("SONG_DOWNLOAD_DURATION_LIMIT", "2000"))

# Telegram audio and video file size limit (in bytes)
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 104857600))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 1073741824))
# Checkout https://www.gbmb.org/mb-to-bytes for converting mb to bytes


# Get your pyrogram v2 session from @BRANDEDSTRINGSESSION_BOT on Telegram
STRING1 = getenv("STRING_SESSION", "BAGDgkYAtVEAp0Ii6l1FxkVG-52T3tc6yX_MYHnlQQwx7ZKee9DWOMisG0JjdGEKaxysSUCn1zRg5ukuwMxmrIwyuvNtyd8rYaHgDVlKm8TpU647ap9_leb93-1j_eGdWs4mBfiePA7jbtCVNSCrOwpn-Ms99QmrCMVM_FrJOYdWaJ1unHqbP60XkpAs0Om5YW8DjqohGHByWOcGpokL6eJoneeh7x0bS2OPHC33g9QjhVM-evImWVtYIBkgdKMdFHeTa7DPDn3Yx92zF30LsVlUP8Io1-XhwF54qhuWSn9X49E0OlE3d8-JyJ07GBes3XRhhIyLoOxtAxugFhMfw4SvGGKJpwAAAAG6HIryAA")
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)


BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}


START_IMG_URL = getenv(
    "START_IMG_URL", "https://telegra.ph//file/919714d04904fae43ffd0.jpg"
)
PING_IMG_URL = getenv(
    "PING_IMG_URL", "https://telegra.ph//file/466d670a36728a36283c9.jpg"
)
PLAYLIST_IMG_URL = "https://telegra.ph/file/f4395ca92239d6de6df8b.jpg"
STATS_IMG_URL = "https://telegra.ph/file/a44534c784f1eac464d85.jpg"
TELEGRAM_AUDIO_URL = "https://telegra.ph/file/d03b8bbec0af13849e031.jpg"
TELEGRAM_VIDEO_URL = "https://telegra.ph/file/5767b8e5619d616c7bf71.jpg"
STREAM_IMG_URL = "https://telegra.ph/file/d83a2cf2bd0dd868f37ae.jpg"
SOUNCLOUD_IMG_URL = "https://telegra.ph/file/f4395ca92239d6de6df8b.jpg"
YOUTUBE_IMG_URL = "https://telegra.ph/file/35b034fe2cdc2effdd02e.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://telegra.ph/file/45abf960687cff85f5855.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://telegra.ph/file/35b034fe2cdc2effdd02e.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://telegra.ph/file/f4395ca92239d6de6df8b.jpg"


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))


if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_CHAT:
    if not re.match("(?:http|https)://", SUPPORT_CHAT):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHAT url is wrong. Please ensure that it starts with https://"
        )
