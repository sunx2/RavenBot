#discord.py imports
import discord
import asyncio
from discord.ext import commands
#needed imports
import os,sys,ast
import random
# scripts import
import profile as prof

#Lunar, cheeze, Kaoru ids
owner_ids=["196115225651576832","215139959865081856","270125856679002113"]
class Economy:
    def __init__(self, bot):
        self.bot = bot
		
		
    @commands.command(pass_context=True,description=" Eggs , completed")
    async def eggs(self,ctx):
        """Shows how many eggs you have."""
        if len(ctx.message.mentions) == 0:
           eggs = prof.Profile(ctx.message.author.id).have_eggs()
           await self.bot.say(":egg: | You have {0} eggs!".format(eggs))
        else:
            eggs = prof.Profile(ctx.message.mentions[0].id).have_eggs()
            await self.bot.say(":egg: | {0} have {1} eggs!".format(ctx.message.mentions[0].name,eggs))
    @commands.command(pass_context=True,description = " generate your profile ! beta0.1 ")
    async def profile(self,ctx):
        """Shows a profile of you or someone else."""
        if len(ctx.message.mentions) == 0:
            p = prof.Profile(ctx.message.author.id).profiler()
            em = discord.Embed(title = "{0}'s Profile".format(ctx.message.author.name.title()), description = "Name = {0}\nEggs = {1}\nBio = {2}\nTitle = {3}".format(ctx.message.author.name,p[1],p[3],p[4]))
            await self.bot.say(embed = em )
        else:
            p = prof.Profile(ctx.message.mentions[0].id).profiler()
            em = discord.Embed(title = "{0}'s Profile".format(ctx.message.mentions[0].name), description = "Name = {0}\nEggs = {1}\nBio = {2}\nTitle = {3}".format(ctx.message.mentions[0].name,p[1],p[3],p[4]))
            await self.bot.say(embed = em )

    @commands.command(pass_context=True)
    async def setbio(self,ctx):
        """Sets yout profile bio."""
        msg = ctx.message.content.replace("r.setbio",'')
        a=prof.Profile(ctx.message.author.id).set_bio(msg)
        await self.bot.say(":check: Successfully updated")

    @commands.command(pass_context=True)
    async def settitle(self,ctx):
        """Sets your profile title."""
        msg = ctx.message.content.replace("r.settitle",'')
        a=prof.Profile(ctx.message.author.id).set_title(msg)
        await self.bot.say(":check: Successfully updated")
    '''

	 Full profile model is ready but dropping for now as cheeze wants [ beta 0.1 ]

    '''

def setup(bot):
    bot.add_cog(Economy(bot))