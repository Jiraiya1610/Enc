import os
from pyrogram.types import Message
from utils import progress_bar
from config import DOWNLOAD_DIR

async def download_file(bot, message: Message, status_msg):
    os.makedirs(DOWNLOAD_DIR, exist_ok=True)
    file_path = await bot.download_media(
        message,
        file_name=os.path.join(DOWNLOAD_DIR, "input.mp4"),
        progress=progress_bar,
        progress_args=(status_msg, "📥 Downloading...")
    )
    return file_path
