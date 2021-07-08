import os


def ytdl(url, file_format):
    if file_format == "video":
        os.system(
            f'youtube-dl -f "bestvideo[filesize<=8M][height<=?480]+bestaudio/best" -o some.%(ext)s {url}'
        )
        if "some.mp4" in os.listdir():
            print("already mp4.")
            if (x := os.path.getsize("some.mp4") / (1024 * 1024)) < 8:
                return [1, "already mp4"]
        elif "some.mkv" in os.listdir():
            os.system(f"ffmpeg -i some.mkv -codec copy some.mp4")
            os.remove("some.mkv")
            print("converted to mp4.")
            if (x := os.path.getsize("some.mp4") / (1024 * 1024)) < 8:
                return [2, "converted from mkv to mp4"]
        else:
            os.system(f"ffmpeg -i some.webm -codec copy some.mp4")
            os.remove("some.webm")
            print("converted to mp4.")
            if (x := os.path.getsize("some.mp4") / (1024 * 1024)) < 8:
                return [3, "converted from webm to mp4"]
        if (x := os.path.getsize("some.mp4") / (1024 * 1024)) > 8:
            print(f"{x}, file size to big...")
            os.remove("some.mp4")
            os.system(f"youtube-dl -x --audio-format mp3 -o some.mp3 {url}")
            print("converted to mp3.")
            return [4, "converted from mp4 to mp3"]
    elif file_format == "audio":
        os.system(f"youtube-dl -x --audio-format mp3 -o some.mp3 {url}")
        return [5, "downloaded mp3"]
