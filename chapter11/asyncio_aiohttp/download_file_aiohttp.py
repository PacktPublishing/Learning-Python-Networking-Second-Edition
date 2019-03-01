#!/usr/bin/python3

import asyncio
import itertools
import aiohttp
import time
import os

async def download_file(url, parts):
    async def get_partial_content(u, i, start, end):
        async with aiohttp.ClientSession().get(
                u, headers={"Range": "bytes={}-{}".format(start, end - 1 if end else "")}) as _resp:
            return i, await _resp.read()

    async with aiohttp.ClientSession().head(url) as resp:
        size = int(resp.headers["Content-Length"])

    ranges = list(range(0, size, size // parts))

    response, _ = await asyncio.wait(
        [get_partial_content(url, i, start, end) for i, (start, end) in
         enumerate(itertools.zip_longest(ranges, ranges[1:], fillvalue=""))])

    final_result = sorted(task.result() for task in response)
    return b"".join(data for _, data in final_result)


if __name__ == '__main__':
    file_url = 'https://docs.python.org/3/archives/python-3.7.2-docs-pdf-letter.zip'
    
    loop = asyncio.get_event_loop()
    t1 = time.time()
    bs = loop.run_until_complete(download_file(file_url, 10))

    filename = os.path.basename(file_url)

    with open(filename, 'wb') as file_handle:
        file_handle.write(bs)
    
    print('Finished downloading {filename}'.format(filename=filename))
        
    print(time.time() - t1, 'seconds passed')