#!/usr/bin/python3

from concurrent.futures import ThreadPoolExecutor
import requests
import itertools
import time

docs = [
    'https://docs.python.org/3/archives/python-3.7.2-docs-pdf-letter.zip',
    'https://docs.python.org/3/archives/python-3.7.2-docs-pdf-a4.zip',
    'https://docs.python.org/3/archives/python-3.7.2-docs-html.zip',
    'https://docs.python.org/3/archives/python-3.7.2-docs-text.zip',
    'https://docs.python.org/3/archives/python-3.7.2-docs.epub'
]

def download_documents(documents, workers=4):

    def get_document(url):
        response = requests.get(url)
        filename = url.split("/")[5]
        print('Downloading '+ filename)
        open(filename, 'wb').write(response.content)
        return url

    message = 'Downloading docs from https://docs.python.org/3/archives'
    symbol = itertools.cycle('\|/-')
    executor = ThreadPoolExecutor(max_workers=workers)
    mydocs = [executor.submit(get_document, url) for url in documents]
    while not all([doc.done() for doc in mydocs]):
        print(message + next(symbol), end='\r')
        time.sleep(0.1)
    return mydocs

if __name__ == '__main__':
	t1 = time.time()
	print(download_documents(docs, workers=4))
	print(time.time() - t1, 'seconds passed')
	