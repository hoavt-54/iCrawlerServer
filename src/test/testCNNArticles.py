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


normalized_url = 'http://www.cnn.com/2015/03/14/us/connecticut-sandy-hook-lawsuits/'
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






''' money cnn format different '''
if 'http://money.cnn.com' in normalized_url:
    time_string = html_tree.xpath('//meta[@name="date"]')[0].attrib['content']
    print("extracted time: " + time_string)
    datetime_obj = datetime.strptime(time_string, "%Y-%m-%d %H:%M:%S")
    datetime_obj_tz = datetime_obj.replace(tzinfo=timezone('EST'))
    update_time = calendar.timegm(datetime_obj_tz.utctimetuple())
    print("time saved: ")
    print(datetime.fromtimestamp(update_time, pytz.timezone('America/Los_Angeles')))
    category_id = 'business'
else:
    time_string = html_tree.xpath('//meta[@property="og:pubdate"]')[0].attrib['content']
    date_time = parse(time_string)
    print("extracted time: " + time_string)
    update_time = calendar.timegm(date_time.utctimetuple())
    print("time saved: ")
    print(datetime.fromtimestamp(update_time))
print(update_time)


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