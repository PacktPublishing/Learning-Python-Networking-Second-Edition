#!/usr/bin/python3

import concurrent.futures
import requests

DOMAINS = ['http://www.foxnews.com/',
           'http://www.cnn.com/',
           'http://www.bbc.co.uk/',
        'http://some-made-up-domainn.com/']


# Retrieve a single page with requests module
def load_requests(domain):
    with requests.get(domain, timeout=10) as connection:
        return connection.text

with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
    future_executor = {executor.submit(load_requests, domain): domain for domain in DOMAINS}
    for domain_future in concurrent.futures.as_completed(future_executor):
        domain = future_executor[domain_future]
        try:
            data = domain_future.result()
            print('%r page is %d bytes' % (domain, len(data)))
        except Exception as exception:
            print('%r generated an exception: %s' % (domain, exception))