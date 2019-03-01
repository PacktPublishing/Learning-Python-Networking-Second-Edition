#!/usr/local/bin/python3

import asyncio
from aiohttp import ClientSession
import time

async def request():
    async with ClientSession() as session:
        async with session.get("http://httpbin.org/headers") as response:
            response = await response.read()
            print(response.decode())

if __name__ == '__main__':
	t1 = time.time()
	loop = asyncio.get_event_loop()
	loop.run_until_complete(request())
	print(time.time() - t1, 'seconds passed')