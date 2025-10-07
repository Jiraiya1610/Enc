import os

# Telegram API credentials (replace with your real ones later)
API_ID = int(os.getenv("API_ID", "25874070"))
API_HASH = os.getenv("API_HASH", "f1522f0124b736b5eb4df95291d4139c")
BOT_TOKEN = os.getenv("BOT_TOKEN", "your_bot_token_here")

# Owner ID (only you can use the bot)
OWNER_ID = int(os.getenv("OWNER_ID", "123456789"))

# Paths
DOWNLOAD_DIR = "downloads"
ENCODE_DIR = "encoded"

# FFmpeg settings (adjust bitrate if needed)
BITRATES = {
    "360p": "700k",
    "480p": "1000k",
    "720p": "1800k",
    "1080p": "3000k"
}
