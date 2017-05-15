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

#Lunar, cheeze, Kaoru ids
owner_ids=["196115225651576832","215139959865081856","270125856679002113"]

#utility commands
class Fun:
    def __init__(self,bot):
        self.bot = bot
		
		
    @commands.command(pass_context=True,description="Tests the bot's latency.")
    async def ping(self,ctx):
        """Test the latency of the bot."""
        pongmsg = await self.bot.send_message(ctx.message.channel, "**Pong!**")
        await self.bot.edit_message(pongmsg, new_content="**Pong! Pinging...**")
        def t_ms(td):
            return td.days*86400000 + td.seconds*1000 + td.microseconds/1000
        await self.bot.edit_message(pongmsg, new_content="**Pong! Took:  {}ms**".format(int(t_ms(pongmsg.timestamp-ctx.message.timestamp))))
    
    @commands.command(pass_context=True,description="Loads an extension.",hidden=True)
    async def load(self,ctx,extension):
        if not ctx.message.author.id in owner_ids:
            return
        try:
            bot.load_extension(extension)
            await self.bot.say("**Module loaded.**")
        except Exception as e:
            await self.bot.say("{}:{}".format(type(e).__name__, e))
    
    @commands.command(pass_context=True,description="Loads an extension.",hidden=True)
    async def unload(self,ctx,extension):

        if not ctx.message.author.id in owner_ids:
            return
        try:
            bot.unload_extension(extension)
            await self.bot.say("**Module unloaded.**")
        except Exception as e:
            await self.bot.say("{}:{}".format(type(e).__name__, e))
    
    @commands.command(pass_context=True,description="Repeats your message.")
    async def say(self,ctx):
        """Repeat what you said."""
        msg = ctx.message.content.replace("r.say",'')
        await self.bot.say(msg)
        return
		
    @commands.command(pass_context=True,description="Say hello to the bot.")
    async def hi(self,ctx):
        """Say hello to the bot."""
        await self.bot.say("{0} {1}".format(random.choice(['Hello',"Hi"]),ctx.message.author.name))
        return
    
    @commands.command(pass_context=True,description="Search for a video on YouTube.")
    async def youtube(self,ctx):
        """Search for something on YouTube."""
        r = requests.get("https://www.youtube.com/results?search_query={0}".format(ctx.message.content.replace("r.youtube ", "")))
        soup = BeautifulSoup(r.text, "html.parser")
        res = soup.select("a.yt-uix-tile-link")[0]
        link = re.search(r"href\S+", str(res))[0][6:-1]
        await self.bot.say(":video_camera: | https://www.youtube.com{0}".format(link))
        return
	
    @commands.command(pass_context=True,description="Search for a keyword on Google.")
    async def google(self,ctx):
        """Search for something on Google."""
        r = requests.get("http://google.com/search?q={0}".format(ctx.message.content.replace("r.google ", "")))
        soup = str(BeautifulSoup(r.text, "html.parser").find_all("cite")[0])
        await self.bot.say(":mag: | {0}".format(re.sub(r"<[^>]*>", "", soup)))
        return

    @commands.command(pass_context=True)
    async def gif(self,ctx,*,search_term:str):
        r=requests.get("http://api.giphy.com/v1/gifs/search?q={}&api_key=dc6zaTOxFJmzC".format(search_term.replace(" ", "+")))
        data=eval(r.text)
        url=data["data"][random.randint(0,10)]["url"].replace("\\", "")
        await self.bot.say(url)
        return
	
    @commands.command(pass_context=True,description="Translate an english word to Japanese.")
    async def jisho(self,ctx):
        """Translate an english word to Japanese."""
        a = goslate.Goslate()
        b = ctx.message.content
        await self.bot.say(":closed_book: | {0} {1}".format(b.replace("r.jisho ", ""), a.translate(b, "ja")))
        return
 


def setup(bot):
    bot.add_cog(Fun(bot))