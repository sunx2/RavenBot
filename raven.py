#discord.py imports

import discord
import asyncio
from discord.ext import commands

#needed imports
import os,sys,ast
import random
# scripts import
import profile as prof


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
@bot.command(pass_context=True,description=" Eggs , completed")
async def eggs(ctx):
	if len(ctx.message.mentions) == 0:
		eggs = prof.Profile(ctx.message.author.id).have_eggs()
		await bot.say(":egg: | You have {0} eggs!".format(eggs))
	else:
		eggs = prof.Profile(ctx.message.mentions[0].id).have_eggs()
		await bot.say(":egg: | {0} have {1} eggs!".format(ctx.message.mentions[0].name,eggs))
@bot.command(pass_context=True,description = " generate your profile ! beta0.1 ")
async def profile(ctx):
	if len(ctx.message.mentions) == 0:
		p = prof.Profile(ctx.message.author.id).profiler()
		await bot.say("Name = *{0}*\nEggs = {1}\n Bio= {2}\n Title = {3}".format(ctx.message.author.name,p[1],p[3],p[4]))
	else:
		eggs = prof.Profile(ctx.message.mentions[0].id).profiler()
				await bot.say("Name = *{0}*\nEggs = {1}\n Bio= {2}\n Title = {3}".format(ctx.message.mentions[0].name,p[1],p[3],p[4]))
				


'''

 Full profile model is ready but dropping for now as cheeze wants [ beta 0.1 ]

'''


# bot message event
@bot.listen()
async def on_message(message):
	print("working")

# bot mention event


bot.run('token')
