#discord.py imports

import discord
import asyncio
from discord.ext import commands

#needed imports
import os,sys,ast
import random

#server imports

    #leave server to me

#----------------------------------------------------------

#bot description
description= " Raven "

bot = commands.Bot(command_prefix="r.",description=description)

#bot active event
@bot.event
async def on_ready():
	print("Activated ...bot ",bot.user.name)

#----------------------------------------------------------------

#bot commands 
#utility commands
@bot.command(pass_context=True,description="")
async def say(ctx):
	msg = ctx.message.content.replace("r.say",'')
	await bot.say(msg)
	return
	
@bot.command(pass_context=True,description="")
async def hi(ctx):
	await bot.say("{0} {1}".format(random.choice(['Hello',"Hi"]),ctx.message.author.name))
	return



#member commands


# bot message event
@bot.listen()
async def on_message(message):
	print("working")

# bot mention event


bot.run('MzEyNjE3NjkwNzE4MTQyNDY0.C_dsLA.DmaEewiIylnDlVEw1APREx4Ukbs')
