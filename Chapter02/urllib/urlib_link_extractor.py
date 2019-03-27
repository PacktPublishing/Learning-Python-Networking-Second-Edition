#!/usr/bin/env python3

from urllib.request import urlopen
import re

def download_page(url):
	return urlopen(url).read().decode('utf-8')

def extract_links(page):
	link_regex = re.compile('<a[^>]+href=["\'](.*?)["\']',re.IGNORECASE)
	return link_regex.findall(page)

if __name__ == '__main__':
	target_url = 'http://www.packtpub.com'
	packtpub = download_page(target_url)
	links = extract_links(packtpub)
	for link in links:
		print(link)