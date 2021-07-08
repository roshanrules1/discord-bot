import os


def ytdl(url):
    os.system(
        f'youtube-dl -f "bestvideo[filesize<=8M][height<=?480]+bestaudio/best" -o some.%(ext)s {url}'
    )
    os.system(f"ffmpeg -i some.mkv -codec copy some.mp4")
    os.remove("some.mkv")
    if os.path.getsize("some.mp4") > (8 * 10 ** 6):
        os.remove("some.mp4")
        os.system(f"youtube-dl -x --audio-format mp3 -o some.mp3 {url}")


ytdl("https://www.youtube.com/watch?v=ip759vjqWZU&ab_channel=BiggZimCh")
