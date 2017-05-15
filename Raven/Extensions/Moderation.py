#discord.py imports
import discord
import asyncio
from discord.ext import commands
#Owner ID's just in case
owner_ids=["196115225651576832","215139959865081856","270125856679002113"]

class Moderation:
    def __init__(self,bot):
        self.bot = bot
    @commands.command(pass_context=True,description="Kicks a member.")
    async def kick(self,ctx,member:discord.Member=None):
        """Kicks a member."""
        author=ctx.message.author
        if author.server_permissions.kick_members:
            if member is None:
                await self.bot.say("You must specify a member to kick!")
                return
            else:
                await self.bot.kick(member)
                await self.bot.say("I have kicked **{}**.".format(member.name))
        else:
            await self.bot.say("You don't have permission to use this!!")
    
	
    @commands.command(pass_context=True,description="Bans a member.")
    async def ban(self,ctx,member:discord.Member=None):
        """Bans a member."""
        author=ctx.message.author
        if author.server_permissions.ban_members:
            if member is None:
                await self.bot.say("You must specify a member to kick!")
                return
            else:
                await self.bot.ban(member,delete_message_days=14)
                await self.bot.say("I have banned **{}**.".format(member.name))
        else:
            await self.bot.say("You don't have permission to use this!!")

    @commands.command(pass_context=True, description="Clears chat messages.")
    async def purge(self,ctx,amount:int):
        """Clears chat messages."""
        author=ctx.message.author
        await self.bot.delete_message(ctx.message)
        if author.server_permissions.manage_messages:
            purged=await self.bot.purge_from(ctx.message.channel, limit=amount, check=None)
            await self.bot.say("I have purged {} messages.".format(len(purged)))
        else:
            await self.bot.say("You don't have permission to use this!")
def setup(bot):
    bot.add_cog(Moderation(bot))