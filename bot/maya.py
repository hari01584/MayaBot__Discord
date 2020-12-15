import discord
from discord.ext import commands
from loadToken import loadToken

import os
from pretty_help import PrettyHelp


from COG.Economy import Economy
from COG.Utility import Utility

client = commands.Bot(command_prefix=".",help_command=PrettyHelp())
token = loadToken();

# TODO: ADD ALL COG HERE!!

client.add_cog(Economy())
client.add_cog(Utility())

#

@client.event
async def on_ready() :
    await client.change_presence(status = discord.Status.idle, activity = discord.Game("Listening to .help"))
    print("I am online")



client.run(token)
