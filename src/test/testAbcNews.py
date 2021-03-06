'''
Created on Mar 5, 2015

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
import queue
import re
import requests
import time


normalized_url = 'http://abcnews.go.com/Politics/amid-biggest-nh-protests-trump-downplays-controversy/story?id=35707504'
thumbnail_url = None
short_description = None
category_id = None
time_string = None
title = None
article_page = requests.get(normalized_url)
#html_tree = html.fromstring(article.html)
html_tree = html.fromstring(article_page.text)


try:
    time_string = html_tree.xpath('//meta[@itemprop="datepublished"]')[0].attrib['content']
    #time_string = time_string + " UTC -5:00"
except BaseException as dateE:
    print("problem with time: {}".format(dateE))
try:
    if (time_string is None):
        time_string = html_tree.xpath('//meta[@name="Last-Modified"]')[0].attrib['content']
        time_string = time_string + " -5:00"
        
        print(time_string)
except BaseException as dateE:
    print("problem with time: {}".format(dateE))
try:
    if (time_string is None):
        time_string = html_tree.xpath('//meta[@itemprop="uploadDate"]')[0].attrib['content']
except BaseException as dateE:
    print("problem with time: {}".format(dateE))
date_time = parse(time_string)
published_time = calendar.timegm(date_time.utctimetuple())
print("time saved: ")
print(datetime.fromtimestamp(published_time))
print(published_time)


try:
    title = html_tree.xpath('//meta[@property="og:title"]')[0].attrib['content']
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
    print('Thumbnaill not found.'.format(e))
try:
    if(thumbnail_url is None):
        thumbnail_url = html_tree.xpath('//meta[@itemprop="thumbnailurl"]')[0].attrib['content']
        print(thumbnail_url)
except Exception as e:
    print('Thumbnaill not found again'.format(e))
try:
    if(thumbnail_url is None):
        thumbnail_url = html_tree.xpath('//meta[@property="twitter:image"]')[0].attrib['content']
        print(thumbnail_url)
except Exception as e:
    print('Thumbnaill not found again'.format(e))


    
    

# get description
try:
    short_description = html_tree.xpath('//meta[@twitter:description"]')[0].attrib['content']
    print(short_description)
except Exception as e:
    print('Description not found'.format(e))
try:
    if(short_description is None):
        short_description = html_tree.xpath('//meta[@name="description""]')[0].attrib['content']
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
    category_id = html_tree.xpath('//a[@itemprop="articleSection"]/text()')[0]
except Exception as e:
    print('Category not found'.format(e))
    
try:
    if category_id is None:
        result = re.search('abcnews\.go\.com/((?:[^/])*)/', normalized_url)
        category_id = result.group(1)
except Exception as e:
    print('Category not found again'.format(e))
    
print(category_id)