#!/usr/bin/env python3

import urllib.request, urllib.parse, urllib.error

URL = 'https://www.github.com'

# By Googling free proxy server
PROXY_ADDRESS = "165.24.10.8:8080" 

if __name__ == '__main__':

    proxy = urllib.request.ProxyHandler({"http" : PROXY_ADDRESS})
    opener = urllib.request.build_opener(proxy)
    urllib.request.install_opener(opener)
    resp = urllib.request.urlopen(URL)
    print ("Proxy server returns response headers: %s " %resp.headers)

