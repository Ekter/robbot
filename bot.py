import discord
from discord.ext import commands
import random
import base64
# import pandas as pd
from settings import *


description = '''Bot pour le serv discord de robotique de PNS'''
with open("../whatisthis.txt","r") as f:
    token=f.readline()
    # token=base64.b64decode(f.readline()).decode("utf-8")

intents = discord.Intents.default()
intents.members = True
intents.message_content = True
intents.reactions = True

bot = commands.Bot(command_prefix=PREFIX, description=description, intents=intents)


@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')
    print('------')

# @bot.event
# async def on_message(message:commands.context.Context):
#     df=pd.read_csv("data.csv")
#     print(df)
#     print(message.author.name)
#     if message.author.name in df["user"].values:
#         df.loc[df["user"]==message.author.name,"messages"]+=1
#     else:
#         df.loc[len(df)]=[message.author.name,1,0]
#     df.to_csv("data.csv",index=False)

# @bot.event
# async def on_raw_reaction_add(payload:discord.RawReactionActionEvent):
#     df=pd.read_csv("data.csv")
#     print(df)
#     print(payload.member.name)
#     if payload.member.name in df["user"].values:
#         df.loc[df["user"]==payload.member.name,"reactions"]+=1
#     else:
#         df.loc[len(df)]=[payload.member.name,0,1]
#     df.to_csv("data.csv",index=False)

@bot.command()
async def ajoute(ctx:commands.context.Context, left: int, right: int):
    """Ajoute deux nombres ensemble, si jamais vous avez la flemme de le calculer vous même."""
    await ctx.send(str(left + right))
    await ctx.message.add_reaction(REACTION_WHEN_DONE)


@bot.command()
async def lance(ctx:commands.context.Context, dice: str):
    """Lance des dés, au format NdN."""
    try:
        rolls, limit = map(int, dice.split('d'))
    except Exception:
        await ctx.send('Vérifiez le format! ça doit être NdN.')
        return
    result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
    await ctx.send(result)
    await ctx.message.add_reaction(REACTION_WHEN_DONE)


@bot.command(description="Choix aléatoire parmi une liste")
async def choose(ctx:commands.context.Context, *choices: str):
    """Choix aléatoire parmi une liste."""
    await ctx.send(random.choice(choices))
    await ctx.message.add_reaction(REACTION_WHEN_DONE)

@bot.command()
async def ben(ctx: commands.context.Context):
    """Ben."""
    await ctx.send(random.choice(["Oui","Non","Peut-être","Arghh"]))
    await ctx.message.add_reaction(REACTION_WHEN_DONE)

@bot.command()
async def repete(ctx:commands.context.Context, times: int=5, content='-Pete et Repete sont sur un bateau... Pete tombe à l\'eau, qui il reste?   -Repete!'):
    """Repete un message plusieurs fois."""
    for i in range(times):
        await ctx.send(content)
    await ctx.message.add_reaction(REACTION_WHEN_DONE)

@bot.command(name="exec")
async def eval_(ctx:commands.context.Context,command:str):
    r"""Execute une commande(ex:"random.randint(0,10)", ou "\"abc\".upper()"). Faites pas crash le bot!"""
    await ctx.send("J'execute: `"+command+"`")
    try:
        await ctx.send("Output: "+str(eval(command)))
        await ctx.message.add_reaction(REACTION_WHEN_DONE)
    except Exception as e:
        await ctx.send("Le processus a crash! Erreur: "+str(e))
        await ctx.message.add_reaction("❌")

@bot.command()
async def joined(ctx:commands.context.Context, member: discord.Member):
    """Dit quand un membre a rejoint le serveur."""
    try:
        await ctx.send(f'{member.name} joined {discord.utils.format_dt(member.joined_at)}')
        await ctx.message.add_reaction(REACTION_WHEN_DONE)
    except Exception as e:
        await ctx.message.add_reaction("❌")

# @bot.command(name="stats")
# async def stats(ctx):
#     """Donne les stats actuelles"""
#     df=pd.read_csv("data.csv")
#     await ctx.send("```"+df.to_string()+"```")
#     await ctx.message.add_reaction(REACTION_WHEN_DONE)

@bot.command(name="addrole",aliases="+r")
@commands.has_role("Admin")
async def addrole(ctx:commands.context.Context, member: discord.Member, role: discord.Role):
    """Ajoute un role."""
    await member.add_roles(role)
    await ctx.send(f'Added {role.name} to {member.name}')
    await ctx.message.add_reaction(REACTION_WHEN_DONE)

@bot.command(name="removerole",aliases="-r")
@commands.has_role("Admin")
async def removerole(ctx:commands.context.Context, member: discord.Member, role: discord.Role):
    """Enleve un role."""
    await member.remove_roles(role)
    await ctx.send(f'Removed {role.name} from {member.name}')

bot.run(token)