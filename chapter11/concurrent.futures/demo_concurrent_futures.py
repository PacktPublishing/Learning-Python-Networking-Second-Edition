#!/usr/bin/python3

import concurrent.futures
import requests

URLS = ['http://www.foxnews.com/',
        'http://www.cnn.com/',
        'http://www.bbc.co.uk/',
        'http://some-made-up-domain.com/']


# Retrieve a single page with requests module
def load_url_requests(url):
    with requests.get(url, timeout=60) as connection:
        return connection.text

# We can use a with statement to ensure threads are cleaned up
with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
    # Start the load operations and mark each future with its URL
    future_to_url = {executor.submit(load_url_requests, url): url for url in URLS}
    for future in concurrent.futures.as_completed(future_to_url):
        url = future_to_url[future]
        try:
            data = future.result()
        except Exception as exception:
            print('%r generated an exception: %s' % (url, exception))
        else:
            print('%r page is %d bytes' % (url, len(data)))