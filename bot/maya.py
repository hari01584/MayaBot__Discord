import discord
from discord.ext import commands
from loadToken import loadToken

import os
from pretty_help import PrettyHelp


from COG.Economy import Economy
from COG.Utility import Utility
from COG.Naughty_Fun import Naughty_Fun

from ErrorHandling.ErrorHandler import ErrorHandler

import spacy
spacy.cli.download("en")
spacy.load('en_core_web_sm')

from Maxon.model import maxon

import Maxon.train

client = commands.Bot(command_prefix=commands.when_mentioned_or("."),help_command=PrettyHelp())
token = loadToken();

# TODO: ADD ALL COG HERE!!

client.add_cog(Economy(client))
client.add_cog(Utility(client))
client.add_cog(Naughty_Fun(client))

client.add_cog(ErrorHandler(client))
#

@client.event
async def on_ready() :
    await client.change_presence(status = discord.Status.idle, activity = discord.Game("Listening to .help"))
    print("I am online")

@client.event
async def on_message(message):
    if client.user.mentioned_in(message):
        text = message.clean_content.replace("@Maya Maxon","")
        await message.channel.send(maxon.get_response(text))


    await client.process_commands(message)

        
client.run(token)
