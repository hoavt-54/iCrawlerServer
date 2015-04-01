'''
Created on Mar 5, 2015

@author: hoavu
'''
from apt.progress.text import long
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


normalized_url = 'http://www.buzzfeed.com/jimdalrympleii/two-police-officers-reportedly-shot-at-ferguson-protest'
thumbnail_url = None
short_description = None
category_id = None
title = None
time_string=None
article_page = requests.get(normalized_url)
#html_tree = html.fromstring(article.html)
html_tree = html.fromstring(article_page.text)


# article_home = Article(normalized_url)
# article_home.download()
# article_home.parse()
# print(article_home.publish_date)
#print(article_page.text)

try:
    time_span_tag = html_tree.xpath('//span[@class="buzz_datetime converted_buzz_datetime"]')[0]
    time_script_tag= time_span_tag.xpath('//script[@type="text/javascript"]')[0]
    result_regex = re.search(r"formatted_date\(([A-Za-z0-9_\./\\-]*)\);", time_span_tag.text_content())
    time_string = result_regex.group(1)
    print("extracted_time: " + time_string)
    #time_string = time_string + " UTC-0400"
except BaseException as dateE:
    print("problem with time: {}".format(dateE))
print(long(time_string))


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
        thumbnail_url = html_tree.xpath('//link[@rel="image_src"]')[0].attrib['href']
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
    category_id = html_tree.xpath('//meta[@property="article:section"]')[0].attrib['content']
except Exception as e:
    print('Category not found'.format(e))
    
try:
    if category_id is None:
        category_id = html_tree.xpath('//meta[@name="category"]')[0].attrib['content']
except Exception as e:
    print('Category not found again'.format(e))
    
print(category_id)