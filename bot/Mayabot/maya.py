import discord
from discord.ext import commands
from .loadToken import loadToken

import os
from pretty_help import PrettyHelp


from .COG.Economy import Economy
from .COG.Utility import Utility
from .COG.Naughty_Fun import Naughty_Fun

from .ErrorHandling.ErrorHandler import ErrorHandler

from .Maxon.primitive import getResponse

client = commands.Bot(command_prefix=commands.when_mentioned_or("."),help_command=PrettyHelp())
token = loadToken()

client.add_cog(Economy(client))
#client.add_cog(Games(client))
client.add_cog(Utility(client))
client.add_cog(Naughty_Fun(client))

client.add_cog(ErrorHandler(client))

@client.event
async def on_ready() :
    await client.change_presence(status = discord.Status.idle, activity = discord.Game("Listening to .help"))
    print("Maya is online.")

@client.event
async def on_message(message):
    if client.user.mentioned_in(message):
        text = message.clean_content.replace("@Maya Maxon","")
        await message.channel.send(getResponse(text))

    await client.process_commands(message)


Mayabot = client.start(token)