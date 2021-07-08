from discord.ext import commands
import discord
import os
from dotenv import load_dotenv
from tts import Text_to_speech
from youtube_dl import ytdl

load_dotenv()


bot = commands.Bot(command_prefix="~", help_command=None)


@bot.command(name="help")
async def help(ctx):
    embed = discord.Embed(
        title="Fox-y Pluggin Commands",
        url="https://youtu.be/dQw4w9WgXcQ",
        color=discord.Color.from_rgb(191, 187, 188),
    )
    embed.set_author(
        name="Fox-y",
        icon_url="https://cdn.discordapp.com/attachments/853168510440439821/862710006151118848/gojo.jpg",
    )
    embed.set_thumbnail(
        url="https://cdn.discordapp.com/attachments/853168510440439821/862710006151118848/gojo.jpg"
    )
    embed.add_field(name="**Say**", value="`~say <message>`", inline=True)
    embed.add_field(
        name="**Talk**",
        value="`~talk <message>`",
        inline=True,
    )
    embed.add_field(
        name="**Download**",
        value="`~download <url> <audio/video>`",
        inline=False,
    )
    await ctx.send(embed=embed)


@bot.command(name="say")
async def say(ctx, *args):
    await ctx.send(f"{' '.join(args)}")


@bot.command(name="talk")
async def talk(ctx, *args):
    if "nigger" in args:
        Text_to_speech("i won't say that word.")
    else:
        Text_to_speech(" ".join(args))
    await ctx.send(file=discord.File("tts.mp3"))
    os.remove("tts.mp3")


@bot.command(name="download")
async def download(ctx, url, arg):
    await ctx.send("Processing request...")
    format_ = arg
    case = ytdl(url, format_)
    print(case)
    if case[0] == 1 or case[0] == 2 or case[0] == 3:
        await ctx.send(file=discord.File("some.mp4"))
        await ctx.send("Process completed, mp4!")
        os.remove("some.mp4")
    elif case[0] == 5:
        await ctx.send(file=discord.File("some.mp3"))
        await ctx.send("Process completed, mp3!")
        os.remove("some.mp3")
    else:
        await ctx.send("File too big, converted to mp3")
        await ctx.send(file=discord.File("some.mp3"))
        await ctx.send("Process completed, mp3!")
        os.remove("some.mp3")


bot.run(os.getenv("TOKEN"))
