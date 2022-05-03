#!/usr/bin/env python3

import requests
from bs4 import BeautifulSoup
import time
import colorama

cookies = {
    'polito': '"41aa6f2f1ca6f5bbbca24247bf994563626cd9b6626c2c32ead64ec654ec71b8!"',
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

params = {
    'query': 'hash:65968234',
}

params2 = {
    'query': 'hash:65968234',
    'page': '2',
}


def fetching():
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

        response2 = requests.get('https://beta.shodan.io/search',params=params2, cookies=cookies, headers=headers)
        soup2 = BeautifulSoup(response2.content, 'html.parser')
        data_2 = soup2.findAll(class_="title text-dark")

        for title in data_2:
            time.sleep(0.1)
            data_2 = title
            data_3 = (data_2.get('href'))
            data_4 = data_3.replace('/host/', '')
            f = open("ip.txt", 'a')
            f.write(f'{data_4}\n')
            f.close()
            print("\033[1;31m", data_4)

    except KeyboardInterrupt:
        print("\nEXIT !")

fetching()



