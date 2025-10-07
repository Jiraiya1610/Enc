import os
from pyrogram.types import Message
from utils import progress_bar

async def upload_file(bot, chat_id, file_path):
    caption = os.path.basename(file_path)
    await bot.send_video(
        chat_id,
        video=file_path,
        caption=f"🎬 Encoded File: `{caption}`",
        progress=progress_bar,
        progress_args=("📤 Uploading...",)
    )
