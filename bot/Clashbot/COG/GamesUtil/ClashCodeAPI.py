import requests
import aiohttp
import random
import json
# from .bot_accs import BOT_ACCS_LIST

BOT_ACCS_LIST = [
    ["botacc01251@botacc.com", "botacc01251"],
]
ENDPOINT_LOGINSITE = "https://www.codingame.com/services/CodinGamer/loginSite"

ENDPOINT_CLASH_PUBLIC = "https://www.codingame.com/services/ClashOfCode/playClash"
ENDPOINT_CLASH_PRIVATE = "https://www.codingame.com/services/ClashOfCode/createPrivateClash"

ENDPOINT_CLASH_LEAVE = "https://www.codingame.com/services/ClashOfCode/leaveClashByHandle"

VALID_CLASH_LANGS = ['Bash', 'C', 'C#', 'C++', 'Clojure', 'D', 'Dart', 'F#', 'Go', 'Groovy', 'Haskell', 'Java', 'JavaScript', 'Kotlin', 'Lua', 'Objective-C', 'OCaml', 'Pascal', 'Perl', 'PHP', 'Python 3', 'Ruby', 'Rust', 'Scala', 'Swift', 'TypeScript', 'VB.NET', ]
VALID_CLASH_MODES = ['FASTEST', 'SHORTEST', 'REVERSE']

class InvalidLangException(Exception):
    pass

class InvalidModeException(Exception):
    pass

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
                pass


    async def getClashPrivate(self, langs=[], modes=[]):
        for l in langs:
            if l not in VALID_CLASH_LANGS:
                raise InvalidLangException("invalid_lang")

        for l in modes:
            if l not in VALID_CLASH_MODES:
                raise InvalidModeException("invalid_mode")

        data = []
        data.append(self.userId)
        data.append(langs)
        data.append(modes)

        async with self.session.post(ENDPOINT_CLASH_PRIVATE, data=json.dumps(data)) as resp:
            res = await resp.json()
            try:
                handle = res["publicHandle"]
                return res
            except Exception:
                print(json.dumps(data))
                print(res)
                pass

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