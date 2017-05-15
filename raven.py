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

#bot commands 
#utility commands
class Stuff:
    @commands.command(pass_context=True,description="Tests the bot's latency.")
    async def ping(self,ctx):
        """Test the latency of the bot."""
        pongmsg = await bot.send_message(ctx.message.channel, "**Pong!**")
        await bot.edit_message(pongmsg, new_content="**Pong! Pinging...**")
        def t_ms(td):
            return td.days*86400000 + td.seconds*1000 + td.microseconds/1000
        await bot.edit_message(pongmsg, new_content="**Pong! Took:  {}ms**".format(int(t_ms(pongmsg.timestamp-ctx.message.timestamp))))
    
    @commands.command(pass_context=True,description="Loads an extension.",hidden=True)
    async def load(self,ctx,extension):
        if not ctx.message.author.id in owner_ids:
            return
        try:
            bot.load_extension(extension)
            await bot.say("**Module loaded.**")
        except Exception as e:
            await bot.say("{}:{}".format(type(e).__name__, e))
    
    @commands.command(pass_context=True,description="Loads an extension.",hidden=True)
    async def unload(self,ctx,extension):

        if not ctx.message.author.id in owner_ids:
            return
        try:
            bot.unload_extension(extension)
            await bot.say("**Module unloaded.**")
        except Exception as e:
            await bot.say("{}:{}".format(type(e).__name__, e))
    
    @commands.command(pass_context=True,description="Repeats your message.")
    async def say(self,ctx):
        """Repeat what you said."""
        msg = ctx.message.content.replace("r.say",'')
        await bot.say(msg)
        return
		
    @commands.command(pass_context=True,description="Say hello to the bot.")
    async def hi(self,ctx):
        """Say hello to the bot."""
        await bot.say("{0} {1}".format(random.choice(['Hello',"Hi"]),ctx.message.author.name))
        return
    
    @commands.command(pass_context=True,description="Search for a video on YouTube.")
    async def youtube(self,ctx):
        """Search for something on YouTube."""
        r = requests.get("https://www.youtube.com/results?search_query={0}".format(ctx.message.content.replace("r.youtube ", "")))
        soup = BeautifulSoup(r.text, "html.parser")
        res = soup.select("a.yt-uix-tile-link")[0]
        link = re.search(r"href\S+", str(res))[0][6:-1]
        await bot.say(":video_camera: | https://www.youtube.com{0}".format(link))
        return
	
    @commands.command(pass_context=True,description="Search for a keyword on Google.")
    async def google(self,ctx):
        """Search for something on Google."""
        r = requests.get("http://google.com/search?q={0}".format(ctx.message.content.replace("r.google ", "")))
        soup = str(BeautifulSoup(r.text, "html.parser").find_all("cite")[0])
        await bot.say(":mag: | {0}".format(re.sub(r"<[^>]*>", "", soup)))
        return

    @commands.command(pass_context=True)
    async def gif(self,ctx,*,search_term:str):
        r=requests.get("http://api.giphy.com/v1/gifs/search?q={}&api_key=dc6zaTOxFJmzC".format(search_term.replace(" ", "+")))
        data=eval(r.text)
        url=data["data"][random.randint(0,10)]["url"].replace("\\", "")
        await bot.say(url)
	return
	
    @commands.command(pass_context=True,description="Translate an english word to Japanese.")
    async def jisho(self,ctx):
	"""Translate an english word to Japanese."""
	a = goslate.Goslate()
	b = ctx.message.content
	await bot.say(":closed_book: | {0} {1}".format(b.replace("r.jisho ", ""), a.translate(b, "ja")))
	return
        
#moderation commands

class Moderation:
    @commands.command(pass_context=True,description="Kicks a member.")
    async def kick(self,ctx,member:discord.Member=None):
        """Kicks a member."""
        author=ctx.message.author
        if author.server_permissions.kick_members:
            if member is None:
                await bot.say("You must specify a member to kick!")
                return
            else:
                await bot.kick(member)
                await bot.say("I have kicked **{}**.".format(member.name))
        else:
            await bot.say("You don't have permission to use this!!")
    
	
    @commands.command(pass_context=True,description="Bans a member.")
    async def ban(self,ctx,member:discord.Member=None):
        """Bans a member."""
        author=ctx.message.author
        if author.server_permissions.ban_members:
            if member is None:
                await bot.say("You must specify a member to kick!")
                return
            else:
                await bot.ban(member,delete_message_days=14)
                await bot.say("I have banned **{}**.".format(member.name))
        else:
            await bot.say("You don't have permission to use this!!")
            
    @commands.command(pass_context=True, description="Clears chat messages.")
    async def purge(self,ctx,amount:int):
        """Clears chat messages."""
        author=ctx.message.author
        await bot.delete_message(ctx.message)
        if author.server_permissions.manage_messages:
            purged=await bot.purge_from(ctx.message.channel, limit=amount, check=None)
            await bot.say("I have purged {} messages.".format(len(purged)))
        else:
            await bot.say("You don't have permission to use this!")
#member commands
class Economy:
    @commands.command(pass_context=True,description=" Eggs , completed")
    async def eggs(self,ctx):
        """Shows how many eggs you have."""
        if len(ctx.message.mentions) == 0:
           eggs = prof.Profile(ctx.message.author.id).have_eggs()
           await bot.say(":egg: | You have {0} eggs!".format(eggs))
        else:
            eggs = prof.Profile(ctx.message.mentions[0].id).have_eggs()
            await bot.say(":egg: | {0} have {1} eggs!".format(ctx.message.mentions[0].name,eggs))
    @commands.command(pass_context=True,description = " generate your profile ! beta0.1 ")
    async def profile(self,ctx):
        """Shows a profile of you or someone else."""
        if len(ctx.message.mentions) == 0:
            p = prof.Profile(ctx.message.author.id).profiler()
            em = discord.Embed(title = "{0}'s Profile".format(ctx.message.author.name.title()), description = "Name = {0}\nEggs = {1}\nBio = {2}\nTitle = {3}".format(ctx.message.author.name,p[1],p[3],p[4]))
            await bot.say(embed = em )
        else:
            p = prof.Profile(ctx.message.mentions[0].id).profiler()
            em = discord.Embed(title = "{0}'s Profile".format(ctx.message.mentions[0].name), description = "Name = {0}\nEggs = {1}\nBio = {2}\nTitle = {3}".format(ctx.message.mentions[0].name,p[1],p[3],p[4]))
            await bot.say(embed = em )

    @commands.command(pass_context=True)
    async def setbio(self,ctx):
        """Sets yout profile bio."""
        msg = ctx.message.content.replace("r.setbio",'')
        a=prof.Profile(ctx.message.author.id).set_bio(msg)
        await bot.say(":check: Successfully updated")

    @commands.command(pass_context=True)
    async def settitle(self,ctx):
        """Sets your profile title."""
        msg = ctx.message.content.replace("r.settitle",'')
        a=prof.Profile(ctx.message.author.id).set_title(msg)
        await bot.say(":check: Successfully updated")
    '''

	 Full profile model is ready but dropping for now as cheeze wants [ beta 0.1 ]

    '''


# bot message event
#Keep this commented out because it was interfering with the r.eval command
#@bot.listen()
#async def on_message(message):
	#print("working")

	
	
#adding cogs and cog extensions

bot.load_extension("Debugging")

bot.add_cog(Moderation())
bot.add_cog(Stuff())
bot.add_cog(Economy())


