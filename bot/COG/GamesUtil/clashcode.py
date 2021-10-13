import asyncio
import os, json, requests, sys
import discord

from .ClashCodeAPI import ClashCodeAPI

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

    timeSecs = data["msBeforeStart"] / 1000
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

async def startClash(ctx, message, args):
    if(not validate(args)):
        return

    async with ClashCodeAPI() as api:
        if(not api.isLogged()):
            return await quickEdit(message, 'error, cannot start coding game, reason: If this is a bug then contact developer')

        if('default' in args):
            return await _defaultStart(api, ctx, message, args)

    await ctx.send('Wrong args?')