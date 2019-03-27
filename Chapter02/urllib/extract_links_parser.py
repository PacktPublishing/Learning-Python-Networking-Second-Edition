#!/usr/bin/env python3

from html.parser import HTMLParser
import urllib.request

class myParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        if (tag == "a"):
            for a in attrs:
                if (a[0] == 'href'):
                    link = a[1]
                    if (link.find('http') >= 0):
                        print(link)
                        newParse = myParser()
                        newParse.feed(link)


url = "http://www.packtpub.com"
request = urllib.request.urlopen(url)
parser = myParser()
parser.feed(request.read().decode('utf-8'))

