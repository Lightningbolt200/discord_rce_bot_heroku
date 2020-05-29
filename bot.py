import discord
from discord.ext import commands
import json

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

@client.command()
async def ourteam(ctx):
    a='curl "https://ctftime.org/api/v1/teams/87448/" | cat > down.json'
    b=subprocess.Popen(a, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE, shell=True).communicate()
    j = open("/app/down.json","r")
    data = json.load(j)
    c=data['rating']
    d=a[0]
    await ctx.send(str("Team:"+'\t\t\t'+data["name"],'\n',"Country:",'\t\t',data["country"],'\n',"Academic:",'\t\t',data["academic"],'\n',"ID:",'\t\t\t',data["id"],'\n',"Aliases:",'\t\t',data["aliases"],'\n',"Current Year data:",'\t',d['2020']))
    

client.run(os.environ['DBToken'])
