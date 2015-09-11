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


normalized_url = 'http://blogs.reuters.com/great-debate/2015/05/29/vladimir-putin-not-planning-ukraine-annexation-but-diplomacy-is-flailing/'
thumbnail_url = None
short_description = None
time_string = None
category_id = None
title = None
article_page = requests.get(normalized_url)
#html_tree = html.fromstring(article.html)
html_tree = html.fromstring(article_page.text)

    
try:
    meta_data = html_tree.xpath('//script[@type="application/ld+json"]/text()')[0]
    print(meta_data)
    meta_data = json.loads(meta_data)
    print(meta_data['headline'])
    print(meta_data['thumbnailUrl'])
    time_string = meta_data['dateCreated']
    print(meta_data['articleSection'])
except BaseException as dateE:
    print("problem with time: {}".format(dateE))
    
try: 
    meta_data = html_tree.xpath("//meta[@name='parsely-page']")[0].attrib['content']
    print(meta_data)
    meta_data = json.loads(meta_data)
    print(meta_data['title'])
    print(meta_data['thumbnailUrl'])
    time_string = meta_data['pub_date']
    print(meta_data['articleSection'])
except BaseException as dateE:
    print("problem with time: {}".format(dateE))

date_time = parse(time_string)
published_time = calendar.timegm(date_time.utctimetuple())
print("time saved: ")
print(datetime.fromtimestamp(published_time))
print(published_time)


# get description
try:
    short_description = html_tree.xpath('//meta[@name="twitter:description"]')[0].attrib['content']
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
""" we should extract the word between http://www.nbcnews.com/ and the very next / to get category"""
result = re.search('nbcnews\.com/((?:[^/])*)/', normalized_url)
print ("category_id: " + result.group(1))
sub_group = re.search('news/((?:[^/])*)/', normalized_url)
print ("sub category_id: " + sub_group.group(1))

try:
    category_id = html_tree.xpath('//meta[@property="article:section"]')[0].attrib['content']
except Exception as e:
    print('Category not found'.format(e))
    
try:
    if category_id is None:
        category_id = html_tree.xpath('//meta[@name="category"]')[0].attrib['content']
except Exception as e:
    print('Category not found again'.format(e))
    
print(category_id)