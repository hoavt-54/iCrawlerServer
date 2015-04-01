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


foxnews_category = {'us' : 'news',
                'industries' : 'business',
                'markets' : 'business',
                'world' : 'World',
                'businessweek-magazine' : 'business',
                'science-energy' : 'science',
                }

normalized_url = 'http://www.foxnews.com/sports/2015/03/12/mason-sho-wasted-as-blues-nip-flyers-1-0-in-so/'
thumbnail_url = None
short_description = None
category_id = None
time_string = None
title = None
article_page = requests.get(normalized_url)
#html_tree = html.fromstring(article.html)
html_tree = html.fromstring(article_page.text)


try:
    time_string = html_tree.xpath('//meta[@name="dcterms.created"]')[0].attrib['content']
    print("extracted time: " + time_string)
except BaseException as dateE:
    print("problem with time: {}".format(dateE))
try:
    if time_string is None:
        time_string = html_tree.xpath('//time[@itemprop="datePublished"]')[0].attrib['datetime']
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
    thumbnail_url = html_tree.xpath('//link[@rel="image_src"]')[0].attrib['href']
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
try:
    category_id = html_tree.xpath('//meta[@name="prism.section" ]')[0].attrib['content']
except Exception as e:
    print('Category not found'.format(e))
    
try:
    if category_id is not None and category_id =='video':
        category_tag_set = html_tree.xpath('//meta[@name="video_category"]')
        category_set = []
        for tag in category_tag_set:
            category_set.append(tag.attrib['content'])
        print(len(category_set))
        intersection = [i for i in category_set if i in foxnews_category]
        if (intersection is not None and len(intersection) > 0):
            category_id = intersection[0]
except Exception as e:
    print('Category not found again{}'.format(e))
    
    
if (category_id is not None):
    category_id = category_id.split(",")[0]
print(category_id)