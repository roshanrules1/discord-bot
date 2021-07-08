import discord
import os
import random
from dotenv import load_dotenv


client = discord.Client()


load_dotenv()


@client.event
async def on_ready():
    print(f"We have logged in as {client.user}")


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith("!download"):
        mess_ = message.content.split()
        url = mess_[1]
        print(mess_[1])
        await message.channel.send("processing request...")
        os.system(
            f'youtube-dl -f "bestvideo[filesize<=8M][height<=?480]+bestaudio/best" -o some.%(ext)s {url}'
        )
        if "some.mkv" in os.listdir():
            os.system(f"ffmpeg -i some.mkv -codec copy some.mp4")
        else:
            os.system(f"ffmpeg -i some.webm -codec copy some.mp4")
        os.remove("some.mkv")
        if "some.mp4" in os.listdir():
            await message.channel.send("process completed!")
            try:
                await message.channel.send(file=discord.File("some.mp4"))
                os.remove("some.mp4")
            except Exception:
                await message.channel.send("file too large! downloading audio...")
                os.remove("some.mp4")
                os.system(f"youtube-dl -x --audio-format mp3 -o some.mp3 {url}")
                try:
                    await message.channel.send(file=discord.File("some.mp3"))
                    await message.channel.send("There you go :)")
                    os.remove("some.mp3")
                except Exception:
                    await message.channel.send("apolpgies")
                    os.remove("some.mp3")

        else:
            await message.channel.send("request failed")


client.run(os.getenv("TOKEN"))
