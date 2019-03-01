#!/usr/bin/python3

import asyncio
import aiohttp

url = 'http://httpbin.org/headers'

@asyncio.coroutine
def get_page():
    resp = yield from aiohttp.ClientSession().get(url)
    text = yield from resp.read()
    return text

if __name__ == '__main__':
	loop = asyncio.get_event_loop()
	content = loop.run_until_complete(get_page())
	print(content)
	loop.close()
