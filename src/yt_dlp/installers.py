from yt_dlp import YoutubeDL
import os

def install_from_name(name: str):
    ydl_opts = {
        "format": "m4a/bestaudio/best",
        "outtmpl": os.path.join(os.path.expanduser("~"), "Music", "smi", "%(title)s.%(ext)s"),
        "postprocessors": [{
            "key": "FFmpegExtractAudio",
            "preferredcodec": "m4a"
        }]
    }

    with YoutubeDL(ydl_opts) as ydl:
        try:
            ydl.download(f"ytsearch1:{name}")
        except PermissionError:
            print("No permission.")
