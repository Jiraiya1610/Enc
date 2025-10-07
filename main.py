import os
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import API_ID, API_HASH, BOT_TOKEN, OWNER_ID
from downloader import download_file
from encoder import encode_video
from uploader import upload_file
from utils import clean_dirs, progress_bar

bot = Client("encoding_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

@bot.on_message(filters.command("start") & filters.private)
async def start_cmd(client, message):
    await message.reply_text(
        "🎬 **Welcome to Video Encoding Bot!**\n\n"
        "Send me a video or media file to encode it to your desired resolution.",
        quote=True
    )

@bot.on_message(filters.video | filters.document)
async def handle_video(client, message):
    if message.from_user.id != OWNER_ID:
        return await message.reply_text("🚫 You are not authorized to use this bot!")

    file_name = message.video.file_name if message.video else message.document.file_name
    msg = await message.reply_text(f"📥 Downloading **{file_name}** ...")
    file_path = await download_file(bot, message, msg)

    # Choose resolution
    buttons = [
        [InlineKeyboardButton("360p", callback_data=f"enc_360p_{file_path}")],
        [InlineKeyboardButton("480p", callback_data=f"enc_480p_{file_path}")],
        [InlineKeyboardButton("720p", callback_data=f"enc_720p_{file_path}")],
        [InlineKeyboardButton("1080p", callback_data=f"enc_1080p_{file_path}")]
    ]
    await msg.edit_text("🎚 **Choose output resolution:**", reply_markup=InlineKeyboardMarkup(buttons))

@bot.on_callback_query(filters.regex(r"^enc_"))
async def encode_callback(client, callback_query):
    data = callback_query.data.split("_")
    resolution, file_path = data[1], "_".join(data[2:])
    await callback_query.message.edit_text(f"⚙️ Encoding to **{resolution}**...")

    output_path = await encode_video(file_path, resolution)
    await callback_query.message.edit_text("📤 Uploading encoded file...")
    await upload_file(bot, callback_query.message.chat.id, output_path)

    await callback_query.message.edit_text("✅ Done! Encoding complete.")
    clean_dirs()

print("Bot is running...")
bot.run()
