import discord
from discord.ext import commands

class Economy(commands.Cog):
   """Economic Commands And Maya Coins!!"""
   def __init__(self, client):
       self.client = client


   @commands.command()
   async def bank(self, ctx):
       """Show your current balance!"""
       await ctx.send("Coming soon..")
