import discord
from discord.ext import commands
import discordRebot.tryrebot as rebot
from discordRebot import *

import json
import os
import inspect
import subprocess
import asyncio

client = commands.Bot(command_prefix ='')
client.remove_command('help')

@client.command(name="!help", brief="Shows this message")
async def Help(ctx, *, command=None):
    """ Shows this message """
    if command is None:
        await ctx.send_help()
    else:
        await ctx.send_help(command)

Convert = Converter(bot=client)

from discordRebot_anywhere import Anywhere
Anywhere.bot = client

rebot.add_rshell(auth=Anywhere(Roles['Rshell']))
rebot.add_rpy(auth=Anywhere(Roles['Rpy']), globals=globals())
mybot = Manager(rebot.P2F)

##############################################################################
# Other Commands and Events

@client.event
async def on_ready():
    print("bot is ready")

@client.event
async def on_member_join(member):
    print(f"{member} has joined this server.")

@client.event
async def on_member_remove(member):
    print(f"{member} has left this server.")


import pycurl_requests as curlreqs

@client.command(name="!ourteam")
async def ourteam(ctx):
    x = 'https://ctftime.org/api/v1/teams/87448/'
    r = curlreqs.get(x)
    data = json.loads(r.content)
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
async def rshell(ctx_, *args):
    global ctx
    ctx = ctx_
    await mybot.on_message(ctx_.message)

@client.command(name=">>", brief="For Rpy")
async def rpy(ctx_, *args):
    global ctx
    ctx = ctx_
    await mybot.on_message(ctx_.message)

@client.command(name="!exit", brief="To exit the bot")
async def Exit(ctx):
    await ctx.send("Bye Bye")
    await client.close()

client.run(os.environ['DBToken'])
