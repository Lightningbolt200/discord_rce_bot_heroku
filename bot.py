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
    await ctx.send(data)
    """
    a=data['rating']
    b=a[0]
    for x in c:
        d=d+x
        d=d+','
        h=(d[:-1])
    await ctx.send("\n"+"Name:"+data['name']+"\n"+"Country:"+data['country'])
    for x in e:
        for y in x.values():
            g[0]=y['organizer_points']
            g[1]=y['rating_points']
            g[2]=y['rating_place']
            await ctx.send("\norganizer_points:\t\t"+str(y['organizer_points'])+"\nrating_points:\t\t"+str(y['rating_points'])+"\nrating_place:\t\t"+str(y['rating_place']))
"""
client.run(os.environ['DBToken'])
