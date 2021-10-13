import discord
from discord.ext import commands
from .GamesUtil.clashcode import startClash

class Games(commands.Cog):
   """A collection of fun and interesting games!!"""
   def __init__(self, client):
       self.client = client

   @commands.group(name='clashcode', pass_context=True)
   async def clashcode_group(self, ctx):
        """game: clash of codes, to know how to play write .help coc"""
        if ctx.invoked_subcommand is None:
            await ctx.send('invalid arguments passed, to know more about this command please do *.help coc*')

   @clashcode_group.group(name='start', pass_context=True)
   async def clashcode_group_start(self, ctx):
       if ctx.invoked_subcommand is None:
           message = await ctx.send('Starting game with default settings [Public Lobby]')
           await startClash(ctx, message, ['default'])
