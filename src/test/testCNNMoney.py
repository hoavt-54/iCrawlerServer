'''
Created on Feb 8, 2015

@author: hoavu
'''
import calendar
from datetime import datetime
from dateutil.parser import parse
from lxml import html
import newspaper
from pytz import timezone
import requests


article = newspaper.Article('http://money.cnn.com/2015/02/06/news/companies/kalashnikov-profits/index.html')
page = requests.get('http://money.cnn.com/2015/02/06/news/companies/kalashnikov-profits/index.html')
html_tree = html.fromstring(page.text)
time_string = html_tree.xpath('//meta[@name="date"]')[0].attrib['content']
datetime_obj = datetime.strptime(time_string, "%Y-%m-%d %H:%M:%S")
datetime_obj_tz = datetime_obj.replace(tzinfo=timezone('EST'))
print (datetime_obj_tz.strftime("%Y-%m-%d %H:%M:%S %Z%z"))
article.update_time = calendar.timegm(datetime_obj_tz.utctimetuple())
print(article.update_time)
article.title = html_tree.xpath('//meta[@property="og:title"]')[0].attrib['content']
print(article.title)
article.thumbnail_url = html_tree.xpath('//meta[@property="og:image"]')[0].attrib['content']
print(article.thumbnail_url)
article.short_description = html_tree.xpath('//meta[@property="og:description"]')[0].attrib['content']
print(article.short_description)
article.category_id = html_tree.xpath('//meta[@name="section"]')[0].attrib['content']
article.category_id = 'business'
print(article.category_id)