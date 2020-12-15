import discord
from discord.ext import commands

class Utility(commands.Cog):
    """Utilities That May Serve You"""
    def __init__(self, client):
        self.client = client


    @commands.command(name="ping")
    async def ping(self,ctx) :
        """Check your server latency"""
        await ctx.send(f"🏓 Pong with {str(round(self.client.latency, 2))}")



    @commands.command(name="givekiss")
    async def givekiss(self,ctx) :
        """Gives you a sweet kiss! Yummy"""
        await ctx.send(f"Awww I Love You {ctx.message.author.name}, Here Take A Kiss *Smootch*")



    @commands.command(name="whoami")
    async def whoami(self,ctx) :
        """feeling lost? let me tell your identity"""
        await ctx.send(f"You are {ctx.message.author.name}")



    @commands.command()
    async def clear(self,ctx, amount=3) :
        """Clears your sneaky beeky messages"""
        await ctx.channel.purge(limit=amount)
