#!/usr/bin/env python3

import requests
from bs4 import BeautifulSoup
import time
import colorama

#coded by g0dmax55

cookies = {
    'polito': '',
}

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:99.0) Gecko/20100101 Firefox/99.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Alt-Used': 'beta.shodan.io',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'none',
    'Sec-Fetch-User': '?1',
    'Cache-Control': 'max-age=0',
}

p1 = {
    'query': 'hash:65968234',
}

p2 = {
    'query': 'hash:65968234',
    'page': '2',
}


def fetching(params):
    try:
        response = requests.get('https://beta.shodan.io/search',params=params, cookies=cookies, headers=headers)
        soup = BeautifulSoup(response.content, 'html.parser')
        data = soup.findAll(class_="title text-dark")


        for title in data:
            time.sleep(0.1)
            data2 = title
            data3 = (data2.get('href'))
            data4 = data3.replace('/host/', '')
            f = open("ip.txt", 'a')
            f.write(f'{data4}\n')
            f.close()
            print("\033[1;31m", data4)

fetching(p1)
fetching(p2)



