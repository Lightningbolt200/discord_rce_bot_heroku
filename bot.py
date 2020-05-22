import discord
from discord.ext import commands


import os
import subprocess




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
    b=subprocess.Popen(a, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE, shell=True).communicate()
    c=b[0].decode()
    d=b[1].decode()
    await ctx.send(c+d)

client.run(os.environ['DBToken'])
