import discord
from discord.ext import commands
from .loadToken import loadToken

import os
from pretty_help import PrettyHelp

from .COG.Games import Games
from .ErrorHandling.ErrorHandler import ErrorHandler


client = commands.Bot(command_prefix=commands.when_mentioned_or("."), help_command=PrettyHelp())
token = loadToken()

client.add_cog(Games(client))
client.add_cog(ErrorHandler(client))

@client.event
async def on_ready() :
    await client.change_presence(status = discord.Status.idle, activity = discord.Game("Listening to .help"))
    print("Clashbot is online.")

@client.event
async def on_message(message):
    if client.user.mentioned_in(message):
        await message.channel.send("Why was I called again?")

    await client.process_commands(message)


clashbot = client.start(token)