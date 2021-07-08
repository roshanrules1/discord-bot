from discord.ext import commands
import discord
import os
from dotenv import load_dotenv
from tts import Text_to_speech

load_dotenv()

client = discord.Client()

bot = commands.Bot(command_prefix="$")

@client.event
async def on_ready():
    print(f"We have logged in as {client.user}"")

@bot.command(name="say")
async def say(ctx, *args):
    await ctx.send(f"{' '.join(args)}")


@bot.command(name="talk")
async def talk(ctx, *args):
    Text_to_speech(" ".join(args))
    await ctx.send(file=discord.File("tts.mp3"))
    os.remove("tts.mp3")


bot.run(os.getenv("TOKEN"))
