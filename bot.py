import discord
from discord.ext import commands
import discordRebot.tryrebot as rebot
from discordRebot import *

import json
import os
import subprocess

client = commands.Bot(command_prefix ='')
Convert = Converter(bot=client)

from bot.discordRebot_anywhere import Anywhere
Anywhere.bot = client

rebot.add_rshell(auth=Anywhere(Roles['Rshell']))
rebot.add_rpy(auth=Anywhere(Roles['Rpy']), globals=globals())
mybot = Manager(rebot.P2F)

@client.event
async def on_ready():
    print("bot is ready")

@client.event
async def on_member_join(member):
    print(f"{member} has joined this server.")

@client.event
async def on_member_remove(member):
    print(f"{member} has left this server.")

##############################################################################
# Other Commands

@client.command(name="!ourteam")
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
    i=""
    l=0
    k=[]
    for x in a:
        for y in x.keys():
            k.append(y)
    for x in a:
        for y in x.values():
            i=i+"\n\n\nYear:\t\t"+str(k[l])+"\norganizer_points:\t\t"+str(y['organizer_points'])+"\nrating_points:\t\t"+str(y['rating_points'])+"\nrating_place:\t\t"+str(y['rating_place'])
            l=l+1
    await ctx.send(e+i)

                                                                             #
##############################################################################

@client.command(name="$", brief="For Rshell")
async def rshell(ctx, *args):
    await mybot.on_message(ctx.message)

@client.command(name=">>", brief="For Rpy")
async def rpy(ctx, *args):
    await mybot.on_message(ctx.message)

@client.command(name="!exit", brief="To exit the bot")
async def Exit(ctx):
    await ctx.send("Bye Bye")
    await client.close()

client.run(os.environ['DBToken'])
