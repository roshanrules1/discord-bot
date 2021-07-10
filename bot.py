from discord.ext import commands
import discord
import os
from dotenv import load_dotenv
from tts import Text_to_speech
from some import ytdl
from random import choice

photo = [
    "chump.png",
    "clap.gif",
    "creep.png",
    "headshake.gif",
    "heheboi.png",
    "ohno.png",
    "ramu.png",
    "whaat.png",
    "woah.png",
    "ooo.jpeg",
]

load_dotenv()

bot = commands.Bot(
    command_prefix="|",
    help_command=None,
    activity=discord.Game(name="|help since 2021"),
)


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
    embed.add_field(name="**Say**", value="`|say <message>`", inline=True)
    embed.add_field(
        name="**Talk**",
        value="`|talk <message>`",
        inline=True,
    )
    embed.add_field(name="**Ramu**", value="`|ramu`", inline=True)

    embed.add_field(
        name="**Download**",
        value="`|download <url> <audio/video>`",
        inline=False,
    )

    await ctx.send(embed=embed)


@bot.event
async def on_message(message):
    if bot.user.mentioned_in(message):
        await message.channel.send("My prefix here is | " + message.author.mention)
    await bot.process_commands(message)


@bot.command(name="say")
async def say(ctx, *args):
    if args[0][2:-1].isnumeric():
        channel = await bot.fetch_channel(args[0][2:-1])
        if channel:
            embed = discord.Embed(
                title=" ".join(args[1:]), color=discord.Color.from_rgb(191, 187, 188)
            )
            await channel.send(embed=embed)
    else:
        channel = discord.utils.get(ctx.guild.text_channels, name=args[0])
        if channel:
            embed = discord.Embed(
                title=" ".join(args[1:]), color=discord.Color.from_rgb(191, 187, 188)
            )
            await channel.send(embed=embed)
        else:
            embed = discord.Embed(
                title=" ".join(args), color=discord.Color.from_rgb(191, 187, 188)
            )
            await ctx.send(embed=embed)


@bot.command(name="talk")
async def talk(ctx, *args):
    if "nigger" in args:
        Text_to_speech("i won't say that word.")
    else:
        Text_to_speech(" ".join(args))
    await ctx.send(file=discord.File("tts.mp3"))
    os.remove("tts.mp3")


@bot.command(name="download")
async def download(ctx, url, arg=None):
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


@bot.command(name="ramu")
async def ramu(ctx):
    image = choice(photo)
    embed = discord.Embed(
        color=discord.Color.from_rgb(191, 187, 188),
    )
    file = discord.File(image)
    embed.set_image(url=f"attachment://{image}")
    await ctx.send(file=file, embed=embed)


bot.run(os.getenv("TOKEN"))
