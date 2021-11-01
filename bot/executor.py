import asyncio

from Mayabot.maya import Mayabot
from Clashbot.clashbot import clashbot

loop = asyncio.get_event_loop()
loop.create_task(Mayabot)
#loop.create_task(clashbot)
loop.run_forever()
