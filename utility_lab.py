#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  5 16:10:09 2022

@author: mikemoore26
"""

import argparse
import requests
import bs4
from datetime import datetime

parser = argparse.ArgumentParser(description='takes URL')

parser.add_argument('-u', '--url',metavar='url', required=True,
 dest='url', action='append', help='url to be scraped')



args = parser.parse_args()

print(args.url)

url = 'https://gaminggorilla.com/most-popular-video-games-now/'
res = requests.get(args.url[0])

#print(datetime.now().strftime("%-d_%B_%Y_%I:%M:%S"))
if  res:
    soup = bs4.BeautifulSoup(res.text,'lxml')
    res_text = soup.text
    filename = f'{datetime.now().strftime("%-d_%B_%Y_%I:%M:%S")}.py'
    with open(filename,'w') as f:
        f.write(res_text)
else:
    print('Invalid  URL  ')
    