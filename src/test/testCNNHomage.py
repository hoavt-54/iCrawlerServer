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

CNN_HOMPAGE_ROOT = "http://edition.cnn.com"
cnn_homepage = requests.get(CNN_HOMPAGE_ROOT)
html_tree = html.fromstring(cnn_homepage.text)
article_urls = html_tree.xpath('//a/@href')
for url in article_urls:
    url = CNN_HOMPAGE_ROOT + url
    print(url)