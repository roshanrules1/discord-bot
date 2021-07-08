import discord
import os
import random
from dotenv import load_dotenv
from discord.ext import commands, tasks
from tts import Text_to_speech

client = discord.Client()

load_dotenv()


@client.event
async def on_ready():
    print("We have logged in as {0.user}".format(client))


@client.event
async def on_message(message):
    if message.content.startswith(".tts"):
        _ = str(message.content[4:])
        Text_to_speech(_)
        await message.channel.send(file=discord.File("tts.mp3"))
        os.remove("tts.mp3")


client.run(os.getenv("TOKEN"))
