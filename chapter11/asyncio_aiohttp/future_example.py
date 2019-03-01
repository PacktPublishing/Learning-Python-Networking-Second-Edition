#!/usr/local/bin/python3

import asyncio
from aiohttp import ClientSession
import time

async def fetch(url, session):
    async with session.get(url) as response:
        # async operation must be preceded by await 
        return await response.read()

async def execute(loop):
    url = "http://httpbin.org/{}"
    tasks = []
    sites = ['headers','ip','user-agent']
    # Fetch all responses within one Client session,
    # keep connection alive for all requests.
    async with ClientSession() as session:
        for site in sites:
            task = asyncio.ensure_future(fetch(url.format(site), session))
            tasks.append(task)
        # async operation must be preceded by await 
        responses = await asyncio.gather(*tasks)
        # you now have all response bodies in this variable
        for response in responses:
            print(response.decode())

if __name__ == '__main__':
	t1 = time.time()
	loop = asyncio.get_event_loop()
	future = asyncio.ensure_future(execute(loop))
	loop.run_until_complete(future)
	print(time.time() - t1, 'seconds passed')