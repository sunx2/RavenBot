#discord.py imports

import discord
import asyncio
import requests
from bs4 import BeautifulSoup
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

@bot.command(pass_context=True,description=" Search for a video on YouTube ")
async def youtube(ctx):
	r = requests.get("https://www.youtube.com/results?search_query={0}".format(ctx.message.content.replace("r.youtube ", "")))
	soup = BeautifulSoup(r.text, "html.parser")
	res = soup.select("a.yt-uix-tile-link")[0]
	link = re.search(r"href\S+", str(res))[0][6:-1]
	await bot.say(":video_camera: | https://www.youtube.com{0}".format(link))
	return

#member commands


# bot message event
@bot.listen()
async def on_message(message):
	print("working")

# bot mention event


bot.run('')
