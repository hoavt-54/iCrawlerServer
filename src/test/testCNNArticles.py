'''
Created on Feb 24, 2015

@author: hoavu
'''

import calendar
from datetime import datetime
from dateutil.parser import parse
import json
from lxml import html
import newspaper
from newspaper.article import Article
from pytz import timezone
import pytz
import queue
import re
import requests


normalized_url = 'http://edition.cnn.com/2015/05/07/news/economy/moldova-stolen-billion/index.html'
thumbnail_url = None
short_description = None
category_id = None
title = None
article_page = requests.get(normalized_url)
#html_tree = html.fromstring(html)
html_tree = html.fromstring(article_page.text)

update_time = None
category_id = None
title = None
time_string = None
published_time= None


cnn_body_tag = html_tree.xpath('//section[@data-zn-id="body-text"]')

print(len(cnn_body_tag))

''' money cnn format different '''
''' money cnn format different '''
try:
    time_string = html_tree.xpath('//meta[@property="og:pubdate"]')[0].attrib['content']
except Exception as e:
    print('time string not found {}.'.format(e))
try:
    if(time_string is None):
        time_string = html_tree.xpath('//meta[@name="pubdate"]')[0].attrib['content']
except Exception as e:
    print('time string not found again{}.'.format(e)) 
try:
    if(time_string is None):
        time_string = html_tree.xpath('//span[@class="cnnDateStamp"]/text()')[0]
        time_string = time_string.replace('2015:', '2015')
        time_string = time_string.replace('2016:', '2016')
        time_string = time_string.replace('2017:', '2017')
        time_string = time_string.replace('2018:', '2018')
        time_string = time_string.replace('ET', '-4:00')
except Exception as e:
    print('time string not found again{}.'.format(e))
print("etracted time: " + time_string)
date_time = parse(time_string)
published_time = calendar.timegm(date_time.utctimetuple())
    
print("time saved: ")
print(datetime.fromtimestamp(published_time))
print(published_time)


title = html_tree.xpath('//meta[@property="og:title"]')[0].attrib['content']
title = title.split(" - CNN.com")[0]
print(title)

try:
    thumbnail_url = html_tree.xpath('//meta[@property="og:image"]')[0].attrib['content']
    print(thumbnail_url)
except Exception as e:
    print('Thumbnaill not found once.'.format(e))
    #thumbnail_url = top_img
    print(thumbnail_url)
short_description = html_tree.xpath('//meta[@property="og:description"]')[0].attrib['content']
print(short_description)


try:
    category_id = html_tree.xpath('//meta[@name="section"]')[0].attrib['content']
    print(category_id)
    if category_id is not None:
        category_id = category_id
except Exception as e:
    print("cannot get category {}".format(e))

if not category_id and 'http://money.cnn.com' in normalized_url:
    category_id = 'business'