import base64
from discord.ext import commands


with open("whatisthis.txt","r") as f:
    token=base64.b64decode(f.readline())
print(base64.b64encode(b'MTAxNDU2MjU3ODA3ODM4NDI3MA.GEwkDF.Bpn4zjDHXFCfTmLFqZSdc6Tbm1C6fvaR9J9rpE').decode('utf-8'),end="")
# bot = commands.Bot(command_prefix=["§", "rb"])
# 
# @bot.event
# async def on_ready():
    # print(f"{bot.user.name} has connected to Discord!")
# 
# 
# bot.run(token)
