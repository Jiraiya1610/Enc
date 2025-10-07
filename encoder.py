import os
import subprocess
from config import BITRATES, ENCODE_DIR

async def encode_video(input_path, resolution):
    os.makedirs(ENCODE_DIR, exist_ok=True)
    output_path = os.path.join(ENCODE_DIR, f"encoded_{resolution}.mp4")
    bitrate = BITRATES.get(resolution, "1000k")

    cmd = [
        "ffmpeg", "-i", input_path,
        "-vf", f"scale=-1:{resolution[:-1]}",
        "-b:v", bitrate,
        "-c:a", "aac", "-preset", "medium", "-y", output_path
    ]
    subprocess.run(cmd, check=True)
    return output_path
