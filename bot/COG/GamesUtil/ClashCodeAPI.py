import requests
import aiohttp
import random

# from .bot_accs import BOT_ACCS_LIST

BOT_ACCS_LIST = [
    ["botacc01251@botacc.com", "botacc01251"],
]
ENDPOINT_LOGINSITE = "https://www.codingame.com/services/CodinGamer/loginSite"

ENDPOINT_CLASH_PUBLIC = "https://www.codingame.com/services/ClashOfCode/playClash"
ENDPOINT_CLASH_LEAVE = "https://www.codingame.com/services/ClashOfCode/leaveClashByHandle"

class ClashCodeAPI():    
    def __init__(self):
        self.userId = None
        self.session = aiohttp.ClientSession()

    def isLogged(self):
        return self.userId is not None

    async def login(self):
        acc = random.choice(BOT_ACCS_LIST)
        data = f'["{acc[0]}","{acc[1]}",true,"CODINGAME"]'
        async with self.session.post(ENDPOINT_LOGINSITE, data=data) as resp:
            res = await resp.json()
            try:
                self.userId = res['codinGamer']['userId']
            except Exception:
                pass

    async def getClashPublic(self):
        data = f'[{self.userId}, null]'
        async with self.session.post(ENDPOINT_CLASH_PUBLIC, data=data) as resp:
            res = await resp.json()
            try:
                handle = res["publicHandle"]
                await self.leaveClashPublic(handle)
                return res
            except Exception:
                print(resp)
                print("error debag data")

    async def leaveClashPublic(self, handle):
        data = f'[{self.userId}, "{handle}"]'
        async with self.session.post(ENDPOINT_CLASH_LEAVE, data=data) as resp:
            pass

    async def close(self):
        await self.session.close()

    async def __aenter__(self):
        await self.login()
        return self

    async def __aexit__(self, *args):
        await self.close()