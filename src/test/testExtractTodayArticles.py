'''
Created on Feb 24, 2015

@author: hoavu
'''

import calendar
from datetime import datetime
from dateutil.parser import parse
from lxml import html
import newspaper
from newspaper.article import Article
from pytz import timezone
import requests
import queue
import json
import re

normalized_url = 'http://www.usatoday.com/story/sports/ufc/2015/12/10/ronda-rousey-holly-holm-rematch-july/77092136/'
thumbnail_url = None
short_description = None
category_id = None
title = None
article_page = requests.get(normalized_url)
#html_tree = html.fromstring(article.html)
html_tree = html.fromstring(article_page.text)
try:
    time_string = html_tree.xpath('//meta[@itemprop="datePublished"]')[0].attrib['content']
except BaseException as dateE:
    print("problem with time: {}".format(dateE))
    time_string = html_tree.xpath('//meta[@property="article:published_time"]')[0].attrib['content']
''' handle case when no time zone on ISO format time'''
try:
    time_part = time_string.split('T')[1]
    if (time_part is not None and '+' not in time_part and '-' not in time_part):
        time_string = re.sub(r'((?=\.).+)', '', time_string)
        time_string = time_string + '-04:00'
except BaseException as dateE:
    print("")
print("extracted time: " + time_string)
date_time = parse(time_string)
published_time = calendar.timegm(date_time.utctimetuple())
print("time saved: ")
print(datetime.fromtimestamp(published_time))
print(published_time)
try:
    title = html_tree.xpath('//meta[@property="og:tfdsitle"]')[0].attrib['content']
except Exception as e:
    print("Title not found")

try:
    if(title is None):
        title = html_tree.xpath('//title/text()')[0].split('|')[0]
except Exception as e:
    print("Title not found {}".format(e))
print(title)

# get thumbnail
try:
    thumbnail_url = html_tree.xpath('//meta[@itemprop="image"]')[0].attrib['content']
    print(thumbnail_url)
except Exception as e:
    print('Thumbnaill not found.'.format(e))
    
    
try:
    if(thumbnail_url is None):
        thumbnail_url = html_tree.xpath('//meta[@name="twitter:image:src"]')[0].attrib['content']
        print(thumbnail_url)
except Exception as e:
    print('Thumbnaill not found again'.format(e))
try:
    if(thumbnail_url is None):
        thumbnail_url = html_tree.xpath('//meta[@property="og:image"]')[0].attrib['content']
        print(thumbnail_url)
except Exception as e:
    print('Thumbnaill not found again'.format(e))    

try:
    if('files.wordpress.com' in thumbnail_url):
        thumbnail_url = thumbnail_url.replace("?w=640","?w=400")
except Exception as e:
    print('resize thumbnail error'.format(e))   
print(thumbnail_url)
# get description
try:
    short_description = html_tree.xpath('//meta[@itemprop="description"]')[0].attrib['content']
    print(short_description)
except Exception as e:
    print('Description not found'.format(e))    
try:
    if(short_description is None):
        short_description = html_tree.xpath('//meta[@name="description"]')[0].attrib['content']
        print(short_description)
except Exception as e:
    print('Description not found again'.format(e))
try:
    if(short_description is None):
        short_description = html_tree.xpath('//meta[@property="og:description"]')[0].attrib['content']
        print(short_description)
except Exception as e:
    print('Description not found again'.format(e))   

# get category
try:
    category_id = html_tree.xpath('//meta[@itemprop="articleSection"]')[0].attrib['content']
except Exception as e:
    print('Category not found'.format(e))
    category_id = 'others'   
if (category_id is not None):
    category_id = category_id.split(",")[0]
print(category_id)