#!/usr/bin/env python3

import requests
from bs4 import BeautifulSoup

def get_front_page():
    target = "https://news.ycombinator.com"
    frontpage = requests.get(target)
    if not frontpage.ok:
        raise RuntimeError("Can't access hacker news, you should go outside")
    news_soup = BeautifulSoup(frontpage.text,"lxml")
    return news_soup


def find_interesting_links(soup):
    items = soup.findAll('td', {'align': 'right', 'class': 'title'}) 
    links = []
    for i in items:
        try:
            siblings = list(i.next_siblings)
            post_id  = siblings[1].find('a')['id']
            link     = siblings[2].find('a')['href']
            title    = siblings[2].text
            links.append({'link': link, 'title': title,'post_id':post_id})
        except Exception as e:
            pass
        
    return links


if __name__ == '__main__':
	soup = get_front_page()
	results = find_interesting_links(soup)
	for r in results:
            if r is not None:
                print(r['link'] +" "+(r['title']))
