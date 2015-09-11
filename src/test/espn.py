'''
Created on Feb 28, 2015

@author: hoavu
'''
from _collections import defaultdict
import calendar
from datetime import datetime
from dateutil.parser import parse
import json
from lxml import html
import newspaper
from newspaper.article import Article
from pytz import timezone
import queue
import requests
import time
from crawlerApp import utils

#http://espn.go.com/nhl/story/_/id/12649294/vancouver-canucks-sign-derek-dorsett-luca-sbisa-contract-extensions
normalized_url = 'http://espn.go.com/mlb/insider/story/_/id/12653490/steady-criticism-chicago-cubs-ss-starlin-castro-unfair-mlb'
thumbnail_url = None
short_description = None
category_id = None
time_string = None
title = None
article_page = requests.get(normalized_url)
#html_tree = html.fromstring(article.html)
html_tree = html.fromstring(article_page.text)


try:
    article_header_tag = html_tree.xpath('//header[@class="article-header"]')[0]
    print("header tag okay")
    time_string = article_header_tag.xpath('//span[@class="timestamp"]/text()')[0] 
    time_string = time_string
    print("extracted time: " + time_string)
except BaseException as dateE:
    print("problem with time: {}".format(dateE))
    
try:
    if (time_string is None):
        time_string = html_tree.xpath('//div[@class="monthday"]/text()')[0] + " " + html_tree.xpath('//div[@class="time"]/text()')[0] + " " + html_tree.xpath('//div[@class="timeofday"]/text()')[0]
except BaseException as dateE:
    print("problem with time: {}".format(dateE))
    
try:
    if time_string is None:
        time_string = html_tree.xpath('//time[@itemprop="datePublished"]')[0].attrib['datetime']
except BaseException as dateE:
    print("problem with time: {}".format(dateE))

published_time = time.time() - utils.time_from_short_string(time_string)
print("time saved: ")
print(datetime.fromtimestamp(published_time))
print(int(published_time))


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
    thumbnail_url = html_tree.xpath('//meta[@name="twitter:image"]')[0].attrib['content']
    print(thumbnail_url)
except Exception as e:
    print('Thumbnaill not found.'.format(e))
try:
    if(thumbnail_url is None):
        thumbnail_url = html_tree.xpath('//meta[@property="og:image"]')[0].attrib['content']
        print(thumbnail_url)
except Exception as e:
    print('Thumbnaill not found again'.format(e))

    
    

# get description
try:
    short_description = html_tree.xpath('//meta[@name="description"]')[0].attrib['content']
    print(short_description)
except Exception as e:
    print('Description not found'.format(e))    
try:
    if(short_description is None):
        short_description = html_tree.xpath('//meta[@property="og:description"]')[0].attrib['content']
        print(short_description)
except Exception as e:
    print('Description not found again'.format(e))



# get category