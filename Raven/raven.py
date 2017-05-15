#discord.py imports

import discord
import asyncio
from discord.ext import commands

#needed imports
import os,sys,ast
import random
import re
import requests
import goslate
from bs4 import BeautifulSoup
# scripts import
import profile as prof

#Lunar, cheeze, Kaoru ids
owner_ids=["196115225651576832","215139959865081856","270125856679002113"]

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
#Loading extensions with cogs inside of them from the Extensions folder
bot.load_extension("Extensions.Debugging")
bot.load_extension("Extensions.Moderation")
bot.load_extension("Extensions.Fun")
bot.load_extension("Extensions.Economy")

bot.run("MzEyNjE3NjkwNzE4MTQyNDY0.C_gNog.284XXYw5bsthlIAKNiTgTHkODJA")

