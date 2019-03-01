#!/usr/bin/python3

import asyncio
import os
import requests
import time

files = ['https://docs.python.org/3/archives/python-3.7.2-docs-pdf-letter.zip',
	'https://docs.python.org/3/archives/python-3.7.2-docs-pdf-a4.zip']
	
async def download_file(url):

	response = requests.get(url)
	filename = os.path.basename(url)
	print('Downloading {filename}'.format(filename=filename))
	open(filename, 'wb').write(response.content)
	msg = 'Finished downloading {filename}'.format(filename=filename)
	return msg
 
async def main(files):
	coroutines = [download_file(file) for file in files]
	completed, pending = await asyncio.wait(coroutines)
	for item in completed:
		print(item.result())
 
 
if __name__ == '__main__':
	
	t1 = time.time()
	event_loop = asyncio.get_event_loop()
	try:
		event_loop.run_until_complete(main(files))
	finally:
		event_loop.close()
	print(time.time() - t1, 'seconds passed')