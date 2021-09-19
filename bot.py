from discord.ext import commands
import discord
import os
from dotenv import load_dotenv
from tts import Text_to_speech
from downloader import ytdl
from random import choice
from youtube import youtube
<<<<<<< HEAD
import json
import aiohttp
import random

print(
    """  
   /\   /\   
  //\\\_//\\\     ____
  \_     _/    /   /
   / * * \    /^^^]
   \_\O/_/    [   ]
    /   \_    [   /
    \     \_  /  /
     [ [ /  \/ _/
    _[ [ \  /_/)"""
)
print(".\n.\n.\nStarting up fox-y...🦊")
=======
from google_ import google
from image import get_google_img

>>>>>>> 6189bca42932e93e54700cee3d10df1d28d70a00

load_dotenv()

bot = commands.Bot(
    command_prefix="|",
    help_command=None,
    activity=discord.Game(name="|help since 2021"),
)


@bot.event
async def on_ready():
    print(f"{bot.user} has connected to Discord!")


@bot.command(name="help")
async def help(ctx):
    embed = discord.Embed(
        title="Fox-y Pluggin Commands",
        url="https://youtu.be/dQw4w9WgXcQ",
        color=discord.Color.from_rgb(51, 104, 133),
    )
    embed.set_author(
        name="Fox-y",
        icon_url="https://cdn.discordapp.com/attachments/853168510440439821/888317583848255518/fox-y.png",
    )
    embed.set_thumbnail(
        url="https://cdn.discordapp.com/attachments/853168510440439821/888317583848255518/fox-y.png"
    )
    embed.add_field(name="**Say**", value="`|say <message>`", inline=True)
    embed.add_field(
        name="**Talk**",
        value="`|talk <message>`",
        inline=True,
    )
<<<<<<< HEAD
=======
    embed.add_field(name="**Google**", value="`|google <query>`", inline=True)
    embed.add_field(name="**Images**", value="`|image <query>`", inline=True)
>>>>>>> 6189bca42932e93e54700cee3d10df1d28d70a00
    embed.add_field(name="**Youtube**", value="`|youtube <query>`", inline=True)
    embed.add_field(name="**Emoji**", value="`|emoji <emote name>`", inline=True)
    embed.add_field(name="**Hug**", value="`|hug <person>`", inline=True)
    embed.add_field(name="**Gif**", value="`|gif <query>`", inline=True)
    embed.add_field(
        name="**Download**",
        value="`|download <url> <audio/video>`",
        inline=False,
    )

    await ctx.send(embed=embed)


@bot.event
async def on_message(message):
    if bot.user.mentioned_in(message) and "@!862927269822464040" in message.content:
        await message.channel.send(
            ":ramukiss: My prefix here is | " + message.author.mention
        )
    await bot.process_commands(message)


<<<<<<< HEAD
@bot.command(name="hug")
async def hug(ctx, arg=""):

    embed = discord.Embed(colour=discord.Color.from_rgb(51, 104, 133))
    session = aiohttp.ClientSession()
    response = await session.get(
        "http://api.giphy.com/v1/gifs/search?q="
        + "+hug"
        + f"&api_key={os.getenv('giphytoken')}&limit=10"
    )
    data = json.loads(await response.text())
    gif_choice = random.randint(0, 9)
    embed.set_image(url=data["data"][gif_choice]["images"]["original"]["url"])

    await session.close()

    await ctx.send(f"{ctx.message.author.mention} hugs {arg}")
    await ctx.send(embed=embed)


@bot.command()
async def emoji(ctx, emojiname):
    for i in bot.guilds:
        emoji = discord.utils.get(i.emojis, name=emojiname)
        if emoji is not None:
            await ctx.message.delete()
            await ctx.send(emoji)


=======
>>>>>>> 6189bca42932e93e54700cee3d10df1d28d70a00
@bot.command(name="say")
async def say(ctx, *args):
    if args[0][2:-1].isnumeric():
        channel = await bot.fetch_channel(args[0][2:-1])
        if channel:
            embed = discord.Embed(
                title=" ".join(args[1:]), color=discord.Color.from_rgb(51, 104, 133)
            )
            await channel.send(embed=embed)
    else:
        channel = discord.utils.get(ctx.guild.text_channels, name=args[0])
        if channel:
            embed = discord.Embed(
                title=" ".join(args[1:]), color=discord.Color.from_rgb(51, 104, 133)
            )
            await channel.send(embed=embed)
        else:
            await ctx.send(" ".join(args))


@bot.command(name="talk")
async def talk(ctx, *args):

    if "nigger" in args:
        Text_to_speech("i won't say that word.")

    else:
        Text_to_speech(" ".join(args))

    await ctx.send(file=discord.File("tts.mp3"))
    os.remove("tts.mp3")


@bot.command(name="download")
@commands.cooldown(1, 30, commands.BucketType.user)
async def download(ctx, url, arg=None):
<<<<<<< HEAD
    try:
        await ctx.send("Processing request...")
        format_ = arg
        case = ytdl(url, format_)
        print(case[1])
        if case[0] == 1 or case[0] == 2 or case[0] == 3:
            await ctx.send("Downloading be slow :sweat_smile:")
            await ctx.send(file=discord.File("some.mp4"))
            await ctx.send("Process completed, mp4!")
            os.remove("some.mp4")
        elif case[0] == 4:
            await ctx.send(file=discord.File("some.mp3"))
            await ctx.send("Process completed, mp3!")
            os.remove("some.mp3")
        elif case[0] == 5:
            await ctx.send("Sorry, file too big!")
    except Exception as _:
        embed = discord.Embed(
            title="You are on cooldown. Try again in 30s",
            color=discord.Color.from_rgb(51, 104, 133),
        )
        embed.add_field(
            name="_unlock premium for lowered cooldown times ;)_",
            value="ples",
            inline=True,
        )
        await ctx.send(embed=embed)
=======
    await ctx.send("Processing request...")
    await ctx.send("Downloading be slow :sweat_smile:")
    format_ = arg
    case = ytdl(url, format_)
    print(case)
    if case[0] == 1 or case[0] == 2 or case[0] == 3:
        await ctx.send(file=discord.File("some.mp4"))
        await ctx.send("Process completed, mp4!")
        os.remove("some.mp4")
    elif case[0] == 4:
        await ctx.send(file=discord.File("some.mp3"))
        await ctx.send("Process completed, mp3!")
        os.remove("some.mp3")
    elif case[0] == 5:
        await ctx.send("Sorry, file too big!")
>>>>>>> 6189bca42932e93e54700cee3d10df1d28d70a00


@bot.command(name="youtube")
async def youtube_(ctx, *args):
    await ctx.send(youtube(" ".join(args)))


@bot.command(name="gif", pass_context=True)
async def giphy(ctx, *, search="random"):
    embed = discord.Embed(colour=discord.Color.from_rgb(51, 104, 133))
    session = aiohttp.ClientSession()

    search.replace(" ", "+")
    response = await session.get(
        "http://api.giphy.com/v1/gifs/search?q="
        + search
        + f"&api_key={os.getenv('giphytoken')}&limit=10"
    )
    data = json.loads(await response.text())
    gif_choice = random.randint(0, 9)
    embed.set_image(url=data["data"][gif_choice]["images"]["original"]["url"])

    await session.close()

    await ctx.send(embed=embed)


bot.run(os.getenv("TOKEN"))
