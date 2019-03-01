#!/usr/bin/python3

import requests

WEBSITE_LIST = ['http://www.foxnews.com/',
                'http://www.cnn.com/',
				'http://www.bbc.co.uk/',
				'http://some-other-domain.com/']

class WebsiteException(Exception):
    pass

def ping_website(address, timeout=6000):
    try:
        response = requests.get(address)
        print("Website %s returned status_code=%s" % (address, response.status_code))
        if response.status_code >= 400:
            print("Website %s returned status_code=%s" % (address, response.status_code))
            raise WebsiteException()
    except requests.exceptions.RequestException:
        print("Timeout expired for website %s" % address)
        raise WebsiteException()


def check_website(address):
    try:
        ping_website(address)      
    except WebsiteException:
        pass