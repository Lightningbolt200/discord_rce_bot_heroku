import discord
from discord.ext import commands


import os




client = commands.Bot(command_prefix ='$')

@client.event
async def on_ready():
    print("bot is ready")

@client.event
async def on_member_join(member):
    print(f"{member} has joined this server.")

@client.event
async def on_member_remove(member):
    print(f"{member} has left this server.")

@client.command()
async def cmd(ctx,*arg):
    print(arg)
    a = ' '.join(arg)
    b=os.popen(a).read()
    await ctx.send(b)

client.run(os.environ['DBToken'])
