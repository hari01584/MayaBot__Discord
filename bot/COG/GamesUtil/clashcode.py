import asyncio
import os, json, requests, sys
import discord
import argparse

from .ClashCodeAPI import ClashCodeAPI
from .ClashCodeAPI import InvalidLangException
from .ClashCodeAPI import InvalidModeException

from .ClashCodeAPI import VALID_CLASH_LANGS
from .ClashCodeAPI import VALID_CLASH_MODES


def validate(args):
    return True #TODO Verify args

async def sendEmbed(ctx, data):
    embed=discord.Embed(
        title="A Match Found, Click here to open", 
        url=f'https://www.codingame.com/clashofcode/clash/{data["publicHandle"]}', 
        description="Coding game match found! Click on embed to open the link!", 
        color=discord.Color.blue()
    )
    embed.set_author(name=f'Requested by: {ctx.message.author.name}', icon_url=f'{ctx.message.author.avatar_url}')
    embed.set_thumbnail(url="https://pbs.twimg.com/profile_images/502136610922586112/4oetBz_5.png")

    timeSecs = data["msBeforeStart"] if 'msBeforeStart' in data else 300000 / 1000
    timeMins = timeSecs / 60
    timeSecs %= 60
    embed.add_field(name="time: ", value=f'{int(timeMins)}min {int(timeSecs)}secs', inline=True)
    embed.add_field(name="clash type: ", value=f'{"public" if data["publicClash"] else "private"}', inline=True)
    embed.add_field(name="players: ", value=f'{len(data["players"])}/{data["nbPlayersMax"]}', inline=True)

    embed.set_footer(text="Did you like this clashcode feature? Give your feedbacks to original developer (Agent_Orange#9852)")

    await ctx.send(embed=embed)

async def quickEdit(baseMessage, content):
    await baseMessage.edit(content=content)

async def _defaultStart(api, ctx, message, args):
    data = await api.getClashPublic()
    try:
        await sendEmbed(ctx, data)
    except Exception:
        return await quickEdit(message, 'error, cannot start coding game, reason: most prolly captcha problem, Contact developer')

    await quickEdit(message, 'Match found (See embed)')

async def _getInvalidLangRes(message):
    h = "invalid one or more language supplied, avaliable languages:\n```"
    h += ', '.join(VALID_CLASH_LANGS)
    h+="```"
    await quickEdit(message, h)

async def _getInvalidModesRes(message):
    h = "invalid one or more modes supplied, avaliable modes:\n```"
    h += ', '.join(VALID_CLASH_MODES)
    h+="```"
    await quickEdit(message, h)

async def _startPrivate(api, ctx, message, args):
    try:
        data = await api.getClashPrivate(args[1], args[2])
    except InvalidLangException:
        return await _getInvalidLangRes(message)
    except InvalidModeException:
        return await _getInvalidModesRes(message)
        
    try:
        await sendEmbed(ctx, data)
    except Exception:
        return await quickEdit(message, 'cannot start this private clash, must be some problem somewhere, Contact developer')

    await quickEdit(message, 'Match found (See embed) Please join before bot leaves the room and match discards. (20 secs)')
    await asyncio.sleep(20)
    await api.leaveClashPublic(data["publicHandle"])
    await quickEdit(message, 'Match Made (Bot left), Enjoy your game')


async def startClash(ctx, message, args):
    if(not validate(args)):
        return

    async with ClashCodeAPI() as api:
        if(not api.isLogged()):
            return await quickEdit(message, 'error, cannot start coding game, reason: no_logged_in If this is a bug then contact developer')

        if('default' in args):
            return await _defaultStart(api, ctx, message, args)
        if('private' in args):
            return await _startPrivate(api, ctx, message, args)

    await ctx.send('Wrong args?')