import discord
from discord.ext import commands
from .GamesUtil.clashcode import startClash

class Games(commands.Cog):
   """A collection of fun and interesting games!!"""
   def __init__(self, client):
       self.client = client

   @commands.group(name='clashcode', pass_context=True)
   async def clashcode_group(self, ctx):
        """game: clash of codes, to know how to play write .help clashcode"""
        if ctx.invoked_subcommand is None:
            await ctx.send('invalid arguments passed, to know more about this command please do *.help clashcode*')

   @clashcode_group.group(name='start', pass_context=True)
   async def clashcode_group_start(self, ctx):
       """start subcommands: do *.help clashcode start* for all commands"""
       if ctx.invoked_subcommand is None:
           await ctx.send('cannot run this group of command directly, please specify a subcommand. do *.help clashcode start* to get all commands under this group')

   @clashcode_group_start.command(name='public', pass_context=True)
   async def clashcode_group_start_public(self, ctx):
        """Starts a public game with default settings! This might fail due to captcha problems, so you might need to login manually and solve recaptcha for this to work."""
        message = await ctx.send('Starting game with default settings [Public Lobby]')
        await startClash(ctx, message, ['default'])

   @clashcode_group_start.command(name='private', pass_context=True)
   async def clashcode_group_start_private(self, ctx, arg1: str=None, arg2: str=None):
        """Starts a private game, pass arguments in form *.clashcode start private C#,python,javascript SHORTEST* or simply *.clashcode start private*, You can even do *.clashcode start private default SHORTEST* to give default parameters, here default is a wildcard entry"""
        if(arg1 == "default"): arg1 = None
        if(arg2 == "default"): arg2 = None

        langs = [] if arg1 is None else arg1.split(',')
        modes = [] if arg2 is None else arg2.split(',')
        if ctx.invoked_subcommand is None:
            message = await ctx.send('Starting game with private settings [Private Lobby]')
            await startClash(ctx, message, ['private', langs, modes])
            

   @clashcode_group.command(name='challenge', pass_context=True)
   async def clashcode_group_challenge(self, ctx, members: commands.Greedy[discord.Member], arg1: str=None, arg2: str=None):
        """Challenge multiple users for a fun private clash! *.clashcode challenge @User1 @User2 ... <langs, optional> <mode, optional>"""
        await self.clashcode_group_start_private(ctx, arg1, arg2)