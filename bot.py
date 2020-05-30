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
    x='curl "https://ctftime.org/api/v1/teams/87448/" | cat > down.json'
    y=subprocess.Popen(x, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE, shell=True).communicate()
    j = open("/app/down.json","r")
    data = json.load(j)
    a=data['rating']
    c=data['aliases']
    d=""
    for x in c:
        d=d+x
        d=d+','
    h=(d[:-1])
    e="Team:"+'\t\t\t'+data["name"]+'\n'+"Country:"+'\t\t'+data["country"]+'\n'+"Academic:"+'\t\t'+str(data["academic"])+'\n'+"ID:"+'\t\t\t'+str(data["id"])+"\nAliases:\t\t"+str(h)   
    g=[1,2,3]
    for x in a:
        for y in x.values():
            g[0]=y['organizer_points']
            g[1]=y['rating_points']
            g[2]=y['rating_place']
            await ctx.send(e+"\norganizer_points:\t\t"+str(y['organizer_points'])+"\nrating_points:\t\t"+str(y['rating_points'])+"\nrating_place:\t\t"+str(y['rating_place']))
client.run(os.environ['DBToken'])
