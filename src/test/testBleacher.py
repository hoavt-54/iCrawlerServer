'''
Created on Mar 14, 2015

@author: hoavu
'''
'''
Created on Mar 10, 2015

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
import time


normalized_url = 'http://bleacherreport.com/articles/2397148-notre-dame-vs-unc-score-twitter-reaction-for-acc-championship-2015'
thumbnail_url = None
short_description = None
time_string = None
category_id = None
title = None
article_page = requests.get(normalized_url)
#html_tree = html.fromstring(article.html)
html_tree = html.fromstring(article_page.text)


try:
    time_string = html_tree.xpath('//meta[@name="pubdate"]')[0].attrib['content']
    print("extracted time: " + time_string)
    #time_string = time_string + " UTC-0400"
except BaseException as dateE:
    print("problem with time: {}".format(dateE))
    

date_time = parse(time_string)
published_time = calendar.timegm(date_time.utctimetuple())
print("time saved: ")
print(datetime.fromtimestamp(published_time))
print(published_time)


try:
    title = html_tree.xpath('//h1[@class="article_title"]/text()')[0]
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
    thumbnail_url = html_tree.xpath('//meta[@property="og:image"]')[0].attrib['content']
    print(thumbnail_url)
except Exception as e:
    print('Thumbnaill not found. {}'.format(e))
try:
    if(thumbnail_url is None):
        thumbnail_url = html_tree.xpath("//meta[@name='twitter:image']")[0].attrib['content']
        print(thumbnail_url)
except Exception as e:
    print('Thumbnaill not found.'.format(e))
try:
    if(thumbnail_url is None):
        thumbnail_url = html_tree.xpath("//meta[@name='sailthru.image.full']")[0].attrib['content']
        print(thumbnail_url)
except Exception as e:
    print('Thumbnaill not found.'.format(e))
    
    

# get description
try:
    short_description = html_tree.xpath('//meta[@property="og:description"]')[0].attrib['content']
    print(short_description)
except Exception as e:
    print('Description not found'.format(e))    
try:
    if(short_description is None):
        short_description = html_tree.xpath('//meta[@"twitter:description"]')[0].attrib['content']
        print(short_description)
except Exception as e:
    print('Description not found again'.format(e))



# get category

try:
    category_id = html_tree.xpath('//meta[@property="article:section"]')[0].attrib['content']
except Exception as e:
    print('Category not found'.format(e))
    
print(category_id)