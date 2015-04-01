'''
Created on Feb 25, 2015

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
import babel.dates
from crawlerApp.utils import convert_vn_date

normalized_url = 'http://doisong.vnexpress.net/tin-tuc/suc-khoe/vi-ba-c-si-ho-i-sinh-ha-ng-nghi-n-nu-cuo-i-tre-tho-3150567.html'
thumbnail_url = None
time_string = None

short_description = None
category_id = None
title = None
article_page = requests.get(normalized_url)
#html_tree = html.fromstring(article.html)
html_tree = html.fromstring(article_page.text)






try:
    time_string = html_tree.xpath('//meta[@itemprop="datePublished"]')[0].attrib['content']
    time_string = time_string.replace (' + ', 'GMT+')
    #time_string = '2015-02-25 04:43 GMT+07:00'
    print(time_string)
except BaseException as dateE:
    print("problem with time: {}".format(dateE))
    
try:
    time_string = html_tree.xpath('//div[@class="block_timer left txt_666"]/text()')
    time_string = time_string[0] + time_string[1]
    print(time_string)
#     time_string = time_string.replace (' + ', 'GMT+')
#     #time_string = '2015-02-25 04:43 GMT+07:00'
    #time_string = 'Thứ năm, 26/2/2015 04:00 GMT+7'
    time_string = convert_vn_date(time_string)
    print(time_string)
except BaseException as dateE:
    print("problem with time: {}".format(dateE))
    

    
# date_time = parse(time_string)
# published_time = calendar.timegm(date_time.utctimetuple())
 
# print(published_time)



try:
    title = html_tree.xpath('//meta[@property="og:title"]')[0].attrib['content']
except Exception as e:
    print("Title not found")

try:
    if(title is None):
        title = html_tree.xpath('//title/text()')[0].split('|')[0]
except Exception as e:
    print("Title not found {}".format(e))
title = title.split(' - VnExpress')[0]
print(title)

# get thumbnail
try:
    thumbnail_url = html_tree.xpath('//meta[@itemprop="thumbnailUrl"]')[0].attrib['content']
    print(thumbnail_url)
except Exception as e:
    print('Thumbnaill not found.'.format(e))
try:
    if(thumbnail_url is None):
        thumbnail_url = html_tree.xpath('//meta[@itemprop="image"]')[0].attrib['content']
        print(thumbnail_url)
except Exception as e:
    print('Thumbnaill not found again'.format(e))
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