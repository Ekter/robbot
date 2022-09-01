import base64
from discord.ext import commands
import discord


with open("whatisthis.txt","r") as f:
    token=base64.b64decode(f.readline()).decode("utf-8")

intents = discord.Intents(members=True,messages=True,reactions=True)
bot = commands.Bot(command_prefix=["robbot", "rb"], intents=discord.Intents.all())

@bot.event
async def on_ready():
    print(f"{bot.user.name} has connected to Discord!")

@bot.command(name="color", aliases=["colour"])
async def color(ctx, *, color: discord.Color):
    """
    Sets the color of the embed.
    """
    print("a")
    await ctx.send("a")
    embed = discord.Embed(color=color)
    await ctx.send(embed=embed)

@bot.command(name="ping")
async def some_crazy_function_name(ctx):
	await ctx.channel.send("pong")

bot.run(token)
