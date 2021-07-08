from discord.ext import commands
import discord
import os
from dotenv import load_dotenv
from tts import Text_to_speech
from youtube_dl import ytdl

load_dotenv()

client = discord.Client()

bot = commands.Bot(command_prefix="$")


@client.event
async def on_ready():
    print(f"We have logged in as {client.user}")


@bot.command(name="say")
async def say(ctx, *args):
    await ctx.send(f"{' '.join(args)}")


@bot.command(name="talk")
async def talk(ctx, *args):
    Text_to_speech(" ".join(args))
    await ctx.send(file=discord.File("tts.mp3"))
    os.remove("tts.mp3")


@bot.command(name="download")
async def download(ctx, url):
    case = ytdl(url)
    print(case)
    if case[0] == 1 or case[0] == 2 or case[0] == 3:
        await ctx.send(file=discord.File("some.mp4"))
        os.remove("some.mp4")
    else:
        await ctx.send("File too big, converted to mp3")
        await ctx.send(file=discord.File("some.mp3"))
        os.remove("some.mp3")


bot.run(os.getenv("TOKEN"))
