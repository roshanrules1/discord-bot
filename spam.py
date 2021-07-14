from discord.ext import commands
import discord
from dotenv import load_dotenv
from os import getenv

load_dotenv()

bot = commands.Bot(
    command_prefix="|",
    help_command=None,
    activity=discord.Game(name="|help since 2021"),
)

dms = {}


@bot.event
async def on_ready():
    print(f"{bot.user} has connected to Discord!")


@bot.event
async def on_message(message: discord.Message):
    user = message.author.name + "#" + message.author.discriminator
    if message.guild is None and not message.author.bot:
        if user not in dms.keys():
            dms[user] = [message.content]
        else:
            dms[user].append(message.content)
    await bot.process_commands(message)


@bot.command(name="dms")
async def checkdms(ctx):
    for key, values in dms.items():
        await ctx.send(f"{key} sent: {values}")
    print("done")


bot.run(getenv("TOKEN"))
