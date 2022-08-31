import base64
from discord.ext import commands


with open("whatisthis.txt","r") as f:
    token=base64.b64decode(f.readline())
# bot = commands.Bot(command_prefix=["§", "rb"])
# 
# @bot.event
# async def on_ready():
    # print(f"{bot.user.name} has connected to Discord!")
# 
# 
# bot.run(token)
