import discord
from discord.ext import commands

from COG.Misc import getImFeeling

import random
from config import FEELING_HORNY_LIST
from config import BURN_LIGHT_LIST

class Naughty_Fun(commands.Cog):
    """Ahh we got some fun commands for ya!"""
    def __init__(self, client):
        self.client = client


    @commands.command(name="givekiss")
    async def givekiss(self,ctx, *, member: discord.Member = None) :
        """Gives you a sweet kiss! Yummy"""
        member = member or ctx.author
        await ctx.send(f"Awww I Love You {member.name}, Here Take A Kiss *Smootch*")



    @commands.command(name="imfeelinghorny")
    async def imfeelinghorny(self,ctx, *, member: discord.Member = None) :
        """Are you feeling little outta control? Ask me!"""

        member = member or ctx.author
        await ctx.send(random.choice(FEELING_HORNY_LIST).format(member.name))


    @commands.command(name="burn")
    async def burn(self,ctx, *, member: discord.Member = None) :
        """You might get a roast, or a praise.. Who knows!!"""

        member = member or ctx.author
        await ctx.send(random.choice(BURN_LIGHT_LIST).format(member.name))
