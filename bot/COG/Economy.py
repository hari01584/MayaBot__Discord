import discord
from discord.ext import commands

class Economy(commands.Cog):
   """Economic Commands And Maya Coins!!"""
   @commands.command()
   async def bank(self, ctx):
       """Show your current balance!"""
       await ctx.send("Pong!")
