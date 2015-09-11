'''
Created on Feb 28, 2015

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

normalized_url = 'http://www.latimes.com/science/la-he-walks-charlton-flats-20150523-story.html'
thumbnail_url = None
short_description = None
time_string = None
category_id = None
title = None
article_page = requests.get(normalized_url)
#html_tree = html.fromstring(article.html)
html_tree = html.fromstring(article_page.text)


try:
    time_string = html_tree.xpath('//meta[@itemprop="datePublished"]')[0].attrib['content']
except BaseException as dateE:
    print("problem with time: {}".format(dateE))
try:
    time_string = html_tree.xpath('//meta[@name="date"]')[0].attrib['content']
except BaseException as dateE:
    print("problem with time: {}".format(dateE))
date_time = parse(time_string)
published_time = calendar.timegm(date_time.utctimetuple())
 
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
    thumbnail_url = html_tree.xpath('//div[@class="trb_allContentWrapper "]')[0].attrib['data-content-thumbnail']
    print(thumbnail_url)
except Exception as e:
    print('Thumbnaill not found.'.format(e))
try:
    if(thumbnail_url is None):
        thumbnail_url = html_tree.xpath('//meta[@property="og:image"]')[0].attrib['content']
        print(thumbnail_url)
except Exception as e:
    print('Thumbnaill not found again'.format(e))
try:
    if(thumbnail_url is None):
        thumbnail_url = html_tree.xpath('//meta[@name="thumbnail"]')[0].attrib['content']
        print(thumbnail_url)
except Exception as e:
    print('Thumbnaill not found again'.format(e))

    
    

# get description
try:
    short_description = html_tree.xpath('//meta[@name="Description"]')[0].attrib['content']
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
    if category_id is None:
        category_id = html_tree.xpath('//div[@class="trb_allContentWrapper" ]')[0].attrib['data-content-section']
except Exception as e:
    print('Category not found again'.format(e))
try:
    if category_id is not None and category_id == 'Business' and 'com/business/technology/' in normalized_url:
        category_id = 'technology'
except Exception as e:
    print('')       
    
    
if (category_id is not None):
    category_id = category_id.split(",")[0]
print(category_id)