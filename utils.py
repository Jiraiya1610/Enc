import os
import shutil
import time

async def progress_bar(current, total, message, text):
    percent = current * 100 / total
    await message.edit_text(f"{text}\n\nProgress: {percent:.2f}%")

def clean_dirs():
    for folder in ["downloads", "encoded"]:
        if os.path.exists(folder):
            shutil.rmtree(folder)
