'''
Created on Feb 24, 2015

@author: hoavu
'''
import calendar
from datetime import datetime
from dateutil.parser import parse
from lxml import html
import newspaper
from pytz import timezone
import requests

USATODAY_HOME_ROOT = 'http://www.usatoday.com'
usatoday_homepage = requests.get(USATODAY_HOME_ROOT)
html_tree = html.fromstring(usatoday_homepage.text)
article_urls = html_tree.xpath('//a/@href')
for url in article_urls:
    if ('http://' not in url and 'https://' not in url):
        url = USATODAY_HOME_ROOT + url
    print(url)