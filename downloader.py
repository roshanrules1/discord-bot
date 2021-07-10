import os
from convert_to_mkv import convert_to_mp4
from format import format_check, audio_format


def ytdl(url, file_format=None):
    if file_format == "video" or file_format is None:
        if (format_id := format_check(url)).isnumeric():
            os.system(f"youtube-dl -f {format_id} -o some.%(ext)s {url}")
            if "some.mp4" in os.listdir():
                print("already mp4.")
                return [1, "already mp4"]
            elif "some.mkv" in os.listdir():
                convert_to_mp4("some.mkv")
                os.remove("some.mkv")
                print("converted to mp4.")
                return [2, "converted from mkv to mp4"]
            else:
                convert_to_mp4("some.webm")
                os.remove("some.webm")
                print("converted to mp4.")
                return [3, "converted from webm to mp4"]
        else:
            return [5, "File too big"]
    elif file_format == "audio":
        if (format_id := audio_format(url)).isnumeric():
            os.system(f"youtube-dl  -f {format_id} -o some.mp3 {url}")
            return [4, "downloaded mp3"]
        else:
            return [5, "File too big"]
