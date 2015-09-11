'''
Created on Feb 7, 2015

@author: hoavu
'''
'''
handle CNN first, just for now
'''
# cnn_cate_id -> iii_cate_id
'''============================================================================
Start to get url from cnn
==============================================================================='''

import calendar
from datetime import datetime
from dateutil.parser import parse
from lxml import html
import json
from newspaper.article import Article
import os.path
import pytz
import queue
import re
import requests
import sys
import time
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from crawlerApp.PostAndGetFromFbPages import CommentLikeShrareGetterThread, \
    POISON, PostToFacebookPage
from crawlerApp.utils import normalize_url, get_text_html_saulify, \
    normalize_text, hasNumbers, normalize_text_nostop
import html as html_original
import html as true_html
from iiidatabase.DatabaseConnectionLib import IIIDatbaseConnection












cnn_category = {    'sport' : 'sport',
                    'world' : 'world',
                    'tech' : 'tech',
                    'entertainment' : 'entertainment',
                    'opinions' : 'opinions',
                    'more' : 'others',
                    'style': 'style',
                    'travel': 'travel',
                    'money' : 'business',
                    'living' : 'life',
                    'us' : 'news',
                    'news' : 'business',
                    'retirement' : 'life',
                    'pf' : 'business',
                    'politics' : 'politics',
                    'china' : 'world',
                    'asia' : 'world',
                    'middle-east' : 'world',
                    'europe' : 'world',
                    'autos' : 'tech',
                    'technology' : 'tech',
                    'media' : 'business',
                    'investing' : 'business',
                    'smallbusiness' : 'business'
                }
usatoday_category = { 'news' : 'news',
                     'sports': 'sport',
                     'life' : 'life',
                     'tv' : 'entertainment',
                     'movies' : 'entertainment',
                     'people' : 'entertainment',
                    'money' : 'business',
                    'tech' : 'tech',
                    'travel': 'travel',
                    'opinion' : 'opinions',
                     'others' : 'others'
                     }

CNN_HOMPAGE_ROOT = "http://edition.cnn.com"
USATODAY_HOME_ROOT = 'http://www.usatoday.com'
HUFFINGTON_POST_HOME = 'http://www.huffingtonpost.com'
NBC_HOMEPAGE = 'http://www.nbcnews.com/'
ABC_HOMEPAGE = 'http://abcnews.go.com'
LA_TIMES_HOMEPAGE = 'http://www.latimes.com'
NEWYORKTIME_HOME = "http://www.nytimes.com"
WASHINGTON_POST = 'http://www.washingtonpost.com'
CBS_NEWS_HOME = 'http://www.cbsnews.com'
BLOOMBERG_HOME_PAGE = 'http://www.bloomberg.com'
FOX_NEWS_HOME = 'http://www.foxnews.com/'
ESPN_HOME = 'http://espn.go.com/'
BUZZFEED_HOME = 'http://www.buzzfeed.com'
FORBES_HOME = 'http://www.forbes.com'
PEOPLE_HOME = 'http://www.people.com'
VOGUE_HOME = 'http://www.vogue.com/?us_site=y'
EVERYDAY_HEATH_HOME = 'http://www.everydayhealth.com'
EONLINE_HOME = 'http://www.eonline.com';
TECHCRUNCH_HOME = 'http://techcrunch.com'
BLEACH_REPORT = 'http://bleacherreport.com'
UPROXX_HOME = 'http://uproxx.com/'
IFLove_SCIENC_HOME = 'http://www.iflscience.com'
NY_DAILY_NEWS_HOME = "http://www.nydailynews.com"
cnn_source_id = 'cnn_usa'
usatoday_source_id = 'usa_today'
huffington_source_id = 'huffington_usa'
newyorktimes_source_id = 'newyork_times'
nbc_source_id = 'nbc_news'
abc_source_id = 'abc_news'
latimes_source_id = 'la_times'
washington_post_source_id = 'washington_post'
cbs_source_id = 'cbs_news'
bloomberg_source_id = 'bloomberg'
foxnews_source_id = 'fox_news'
espn_source_id = 'espn_usa'
buzzfeed_source_id = 'buzzfeed'
forbes_source_id = 'forbes_usa'
people_source_id = 'people_magazine'
vogue_source_id = 'vogue_magazine'
everydayhealth_source_id = 'everydayhealth'
eonline_source_id = 'eonline_us'
techcrunch_source_id = 'techcrunch'
bleachreport_source_id = 'bleacherreport_us'
uproxx_source_id = 'uproxx'
iflovescience_id = 'iflscience'
nydaily_news_id = "nydailynews"
USA = 'us'


cnn_except = {
                }

cnn_homepages = {'http://edition.cnn.com/tech' : 'tech', 
                 'http://edition.cnn.com/sport' : 'sport',
                 'http://www.cnn.com/living' :  'life', 
                 'http://edition.cnn.com/entertainment': 'entertainment',
                 'http://travel.cnn.com/' : 'travel', 
                 'http://edition.cnn.com/opinions' : 'opinions', 
                 'http://www.cnn.com/politics' : 'politics', 
                 'http://www.cnn.com/us': 'news',
                 'http://edition.cnn.com/world' : 'world', 
                 'http://money.cnn.com/' : 'business', 
                 CNN_HOMPAGE_ROOT : None
                 }
def extract_cnn_article (article, is_on_homepage, predifined_category=None):
    if ('/201' not in article.url or article.url in cnn_except or ".cnn.com/" not in article.url):
        return
    if (db_connect.is_url_existed(article.url) != -1):
        print("url is already existed")
        url_sharelikecomment_queue.put(article.url, True)
        return
    normalized_url = normalize_url(article.url)
    if (db_connect.is_url_existed(normalized_url) != -1):
        print("url is already existed")
        url_sharelikecomment_queue.put(normalized_url, True)
        return
    category_id = None
    time_string = None
    article.download()
    article.category_id = ''
    article.published_time = None
    if (predifined_category is not None):
        article.category_id = predifined_category
    article.thumbnail_url = None
    html_tree = html.fromstring(article.html)
    
    ''' money cnn format different '''
    try:
        time_string = html_tree.xpath('//meta[@property="og:pubdate"]')[0].attrib['content']
    except Exception as e:
        print('time string not found {}.'.format(e))
    try:
        if(time_string is None):
            time_string = html_tree.xpath('//meta[@name="pubdate"]')[0].attrib['content']
    except Exception as e:
        print('time string not found again{}.'.format(e)) 
    try:
        if(time_string is None):
            time_string = html_tree.xpath('//span[@class="cnnDateStamp"]/text()')[0]
            time_string = time_string.replace('2015:', '2015')
            time_string = time_string.replace('2016:', '2016')
            time_string = time_string.replace('2017:', '2017')
            time_string = time_string.replace('2018:', '2018')
            time_string = time_string.replace('ET', '-4:00')
    except Exception as e:
        print('time string not found again{}.'.format(e))
    print("etracted time: " + time_string)
    date_time = parse(time_string)
    published_time = calendar.timegm(date_time.utctimetuple())
        
    print("time saved: ")
    print(datetime.fromtimestamp(published_time))
    article.published_time = published_time
    
    
    
    title = html_tree.xpath('//meta[@property="og:title"]')[0].attrib['content']
    article.title = title.split(" - CNN.com")[0]
    print(article.title)
    
    try:
        article.thumbnail_url = html_tree.xpath('//meta[@name="thumbnail"]')[0].attrib['content']
        print(article.thumbnail_url)
    except Exception as e:
        print('Thumbnaill not found once.'.format(e))
    
    try:
        if (article.thumbnail_url is None):
            article.thumbnail_url = html_tree.xpath('//meta[@property="og:image"]')[0].attrib['content']
            print(article.thumbnail_url)
    except Exception as e:
        print('Thumbnaill not found once. {}'.format(e))
    try:
        article.short_description = html_tree.xpath('//meta[@property="og:description"]')[0].attrib['content']
    except Exception as e:
        print('Description once.{}'.format(e))
        article.short_description = article.title
    print(article.short_description)
    
    
    try:
        category_id = html_tree.xpath('//meta[@name="section"]')[0].attrib['content']
    except Exception as e:
        print("cannot get category {}".format(e))
    try:
        if (category_id is None):
            category_id = html_tree.xpath('//meta[@itemprop="articleSection"]')[0].attrib['content']
    except Exception as e:
        print("cannot get category {}".format(e))
    if (category_id is not None and category_id in cnn_category):
        article.category_id = cnn_category.get(category_id)
    if not category_id and 'http://money.cnn.com' in normalized_url:
        article.category_id = 'business'
    if not article.category_id:
        article.category_id = cnn_category.get('more')
    article.source_name = "CNN"
    
    if (article.published_time is None or article.title is None or article.category_id is None):
        raise Exception("")
    print(article.category_id)
    
    ''' get clean text content '''
    text_html = true_html.escape(get_text_html_saulify(normalized_url), True)
    article.parse()
    text = normalize_text(article.text)
    normalized_title = normalize_text_nostop(article.title)
    article.source_id = cnn_source_id
    ''' insert this article to database, maybe send url to another thread to get count, share, .... or maket it asynchronous'''
    # when no exception, we insert to database
    article.id = db_connect.insert_article3(normalized_url, article.title, cnn_source_id, article.category_id, 
                                     False, is_on_homepage, article.published_time, article.thumbnail_url, article.short_description, USA, text_html, text, normalized_title)
    
    # after insert to database, we put this url to get share, comment, like
    url_sharelikecomment_queue.put(normalized_url, True)
    article.url = normalized_url
    post_queue.put(article, True)


#0169 443 7589



'''
============================================================================================
====================== Start thread to get url statistic, post to page here ================
============================================================================================
'''

print('Start thread get like share comments')
url_sharelikecomment_queue = queue.Queue(100)
share_like_comment_thread = CommentLikeShrareGetterThread(queue=url_sharelikecomment_queue)
share_like_comment_thread.start()

print('Start thread to post to page')
post_queue = queue.Queue(40)
page_poster_thread = PostToFacebookPage(queue=post_queue)
page_poster_thread.start()
'''
============================================================================================
'''   
     
 
             
                    
'''
Here we travel all source article by using article. Take 'CACHING' into account later 
'''
try:
    db_connect = IIIDatbaseConnection()
    db_connect.init_database_cont()
    print('Reading CNN source ...')
                        
                   
    ''' we process homepage sport'''
    for cnn_home in cnn_homepages:
        print("Extracting:  " + cnn_home)
        cnn_homepage = requests.get(cnn_home)
        html_tree = html.fromstring(cnn_homepage.text)
        article_urls = html_tree.xpath('//a/@href')
        for home_url in article_urls:
            if  home_url is not None and len(home_url) > 16: 
                if ('http://' not in home_url and 'https://' not in home_url):
                    if (cnn_home is 'http://money.cnn.com'):
                        home_url = cnn_home + home_url
                    else:
                        home_url = CNN_HOMPAGE_ROOT + home_url
                         
                try:
                    article_home = Article(home_url)
                    extract_cnn_article(article_home, True, cnn_homepages.get(cnn_home))
                except Exception as e:
                    print('Smt wrong when process homepage sport  article:  {}'.format(e) + home_url)
                         
                          
          
                       
                    
                        
#     '''================== we travel to process all articles here ====================='''
#     '''==============================================================================='''
#     cnn_source = newspaper.build('http://edition.cnn.com/sport', memoize_articles=False)
#     print(cnn_source.size())
#     for article in cnn_source.articles:
#         try:
#             extract_cnn_article (article, False)
#         except Exception as e:
#             print('Something went wrong when download and parse article:  {}'.format(e) + article.url)
#              
                                
    db_connect.close_database_cont()   
except Exception as e:        
    print('Something went wrong with database: {}'.format(e))
                    
                        
    '''
    =======================================================================================================================================
    =======================================================================================================================================
    ================================================= CNN Stop here =======================================================================
    =======================================================================================================================================
    =======================================================================================================================================
    '''
                   
                  
                  
                  
                  
                  
                      
                      
                      
                      
                      
                      
                       
                       
                       
                       
'''
=======================================================================================================================================
=======================================================================================================================================
================================================= USA TODAY start =====================================================================
=======================================================================================================================================
=======================================================================================================================================
'''
usatoday_execept = {'http://www.usatoday.com/story/news/2013/01/09/corrections-clarifications/1821023',
                    'http://www.usatoday.com/sports/olympics/2014/'
                                      
                    }
                  
def extract_usatoday_article(article, is_on_homepage, predifined_category=None):
    #print("url to extract: " + article.url)
    if ('/201' not in article.url or article.url in usatoday_execept or article.url + '/' in usatoday_execept or 'usatoday.com' not in article.url ):
        return
    if (db_connect.is_url_existed(article.url) != -1):
        print("url is already existed")
        url_sharelikecomment_queue.put(article.url, True)
        return
    normalized_url = normalize_url(article.url)
    if ('usatoday.com' not in normalized_url):
        return
    if (normalized_url in usatoday_execept or normalized_url + '/' in usatoday_execept):
        return
    if (db_connect.is_url_existed(normalized_url) != -1):
        print("url is already existed")
        url_sharelikecomment_queue.put(normalized_url, True)
        return
                      
    article.category_id = None
    article.thumbnail_url = None
    article.short_description = None
    article.published_time = None
    article.title = None
    article.source_id = None
    article.id = None
    article.source_id = None
    article.id = None
                      
    time_string = None
    title = None
    thumbnail_url = None
    short_description = None
    category_id = None
    if (predifined_category is not None):
        article.category_id = predifined_category
                      
    article.download()
    html_tree = html.fromstring(article.html)
                      
    #get time
    try:
        time_string = html_tree.xpath('//meta[@itemprop="datePublished"]')[0].attrib['content']
    except BaseException as dateE:
        print("problem with time: {}".format(dateE))
    try:
        time_string = html_tree.xpath('//meta[@property="article:published_time"]')[0].attrib['content']
    except BaseException as dateE:
        #print("problem with time: {}".format(dateE))
        print("")
    ''' handle case when no time zone on ISO format time'''
    try:
        time_part = time_string.split('T')[1]
        if (time_part is not None and '+' not in time_part and '-' not in time_part):
            time_string = re.sub(r'((?=\.).+)', '', time_string)
            time_string = time_string + '-04:00'
    except BaseException as dateE:
        print("")
                      
                      
    if (time_string is not None):
        date_time = parse(time_string)
        article.published_time = calendar.timegm(date_time.utctimetuple())
        if (article.published_time > time.time()):
            article.published_time = None
        print(article.published_time)
    print("extracted time: " + time_string)
    print("time saved: ")
    print(datetime.fromtimestamp(article.published_time, pytz.timezone('America/Los_Angeles')))
                      
    #get title
    try:
        title = html_tree.xpath('//meta[@property="og:title"]')[0].attrib['content']
        print(title)
    except Exception as e:
        #print("Title not found {}".format(e))
        print("")
    try:
        if(title is None):
            title = html_tree.xpath('//title/text()')[0].split('|')[0]
    except Exception as e:
        print("Title not found {}".format(e))
    article.title = title
                      
    # get thumbnail
    try:
        thumbnail_url = html_tree.xpath('//meta[@itemprop="image"]')[0].attrib['content']
        print(thumbnail_url)
    except Exception as e:
        #print('Thumbnaill not found. {}'.format(e))
        print("")
    try:
        if(thumbnail_url is None):
            thumbnail_url = html_tree.xpath('//meta[@name="twitter:image:src"]')[0].attrib['content']
            print(thumbnail_url)
    except Exception as e:
        #print('Thumbnaill not found again. {}'.format(e))
        print("")
    try:
        if(thumbnail_url is None):
            thumbnail_url = html_tree.xpath('//meta[@itemprop="thumbnailUrl"]')[0].attrib['content']
            print(thumbnail_url)
    except Exception as e:
        #print('Thumbnaill not found again, {}'.format(e))
        print("")
    try:
        if(thumbnail_url is None):
            thumbnail_url = html_tree.xpath('//meta[@property="og:image"]')[0].attrib['content']
            print(thumbnail_url)
    except Exception as e:
        #print('Thumbnaill not found again. {}'.format(e))
        print("")    
    thumbnail_url = html_original.unescape(thumbnail_url)
    try:
        if('files.wordpress.com' in thumbnail_url):
            thumbnail_url = thumbnail_url.replace("?w=640","?w=400")
    except Exception as e:
        print('resize thumbnail error'.format(e))
    article.thumbnail_url = thumbnail_url
    # get description
    try:
        short_description = html_tree.xpath('//meta[@itemprop="description"]')[0].attrib['content']
        print(short_description)
    except Exception as e:
        #print('Description not found. {}'.format(e))
        print("")    
    try:
        if(short_description is None):
            short_description = html_tree.xpath('//meta[@name="description"]')[0].attrib['content']
            print(short_description)
    except Exception as e:
        #print('Description not found again. {}'.format(e))
        print("")
    try:
        if(short_description is None):
            short_description = html_tree.xpath('//meta[@property="og:description"]')[0].attrib['content']
            print(short_description)
    except Exception as e:
        print('Description not found again. {}'.format(e))   
    article.short_description = short_description
                      
    # get category
    try:
        category_id = html_tree.xpath('//meta[@itemprop="articleSection"]')[0].attrib['content']
    except Exception as e:
        print('Category not found. {}'.format(e))
    if (category_id is not None and len(category_id) < 40):
        print('category: ' + category_id)
        category_id = category_id.split(",")[0]
        article.category_id = usatoday_category.get(category_id)
    if ('ftw.usatoday.com/' in article.url):
        article.category_id = 'sport'
    if (article.category_id is None):
        article.category_id = 'others'
    article.source_name = "USA TODAY"
                      
                      
    if (article.published_time is None or article.title is None or article.category_id is None):
        raise Exception("")
                   
    text_html = true_html.escape(get_text_html_saulify(normalized_url), True)
    article.parse()
    text = normalize_text(article.text)
    normalized_title = normalize_text_nostop(article.title)
    article.source_id = usatoday_source_id
    ''' insert this article to database, maybe send url to another thread to get count, share, .... or maket it asynchronous'''
    # when no exception, we insert to database
    try:
        article.id = db_connect.insert_article3(normalized_url, article.title, usatoday_source_id, 
                                     article.category_id, False, is_on_homepage, article.published_time,
                                     thumbnail_url, article.short_description, USA, text_html, text, normalized_title)
    except Exception as dbE:
        print("Error when insert article to db. {}".format(dbE))
    # after insert to database, we put this url to get share, comment, like
    url_sharelikecomment_queue.put(normalized_url, True)
    article.url = normalized_url
    post_queue.put(article, True)
                  
                  
                  
                  
                  
                  
                  
                  
                  
                  
                  
                  
print('...................................................\n' +
      '...................................................\n' + 
      '...................................................\n' +
      'start get articles from usatoday' +
      '...................................................\n' +
      '...................................................\n'
      )
try:
    db_connect = IIIDatbaseConnection()
    db_connect.init_database_cont()
                      
                      
                  
                      
    ''' we process homepage sport'''
    USA_TODAY_HOMPAGE_SPORT = 'http://www.usatoday.com/sports/'
    usatoday_homepage_sport = requests.get(USA_TODAY_HOMPAGE_SPORT)
    html_tree = html.fromstring(usatoday_homepage_sport.text)
    article_urls = html_tree.xpath('//a/@href')
    for home_url in article_urls:
        if  home_url is not None and len(home_url) > 16 and ('sportsnetwork.com' not in home_url): 
            if ('http://' not in home_url and 'https://' not in home_url):
                home_url = USATODAY_HOME_ROOT + home_url
            try:
                article_home = Article(home_url)
                extract_usatoday_article(article_home, True, usatoday_category.get('sports'))
            except Exception as e:
                print('Smt wrong when process homepage sport  article:  {}'.format(e) + home_url)
                        
                  
                      
                      
    ''' we process homepage life'''
    USA_TODAY_HOMPAGE_LIFE= 'http://www.usatoday.com/life/'
    usatoday_homepage_life = requests.get(USA_TODAY_HOMPAGE_LIFE)
    html_tree = html.fromstring(usatoday_homepage_life.text)
    article_urls = html_tree.xpath('//a/@href')
    for home_url in article_urls:
        if  home_url is not None and len(home_url) > 16 : 
            if ('http://' not in home_url and 'https://' not in home_url):
                home_url = USATODAY_HOME_ROOT + home_url
            try:
                article_home = Article(home_url)
                extract_usatoday_article(article_home, True, usatoday_category.get('life'))
            except Exception as e:
                print('Smt wrong when process homepage life  article:  {}'.format(e) + home_url)
                  
                  
                  
                  
                   
    ''' we process homepage money'''
    USA_TODAY_HOMPAGE_MONEY =  'http://www.usatoday.com/money/'
    usatoday_homepage_money= requests.get(USA_TODAY_HOMPAGE_MONEY)
    html_tree = html.fromstring(usatoday_homepage_money.text)
    article_urls = html_tree.xpath('//a/@href')
    for home_url in article_urls:
        if  home_url is not None and len(home_url) > 16 : 
            if ('http://' not in home_url and 'https://' not in home_url):
                home_url = USATODAY_HOME_ROOT + home_url
            try:
                article_home = Article(home_url)
                extract_usatoday_article(article_home, True, usatoday_category.get('money'))
            except Exception as e:
                print('Smt wrong when process homepage money  article:  {}'.format(e) + home_url)
                  
                  
                  
                  
                  
                  
                  
    ''' we process homepage tech'''
    USA_TODAY_HOMPAGE_TECH =  'http://www.usatoday.com/tech/'
    usatoday_homepage_tech= requests.get(USA_TODAY_HOMPAGE_TECH)
    html_tree = html.fromstring(usatoday_homepage_tech.text)
    article_urls = html_tree.xpath('//a/@href')
    for home_url in article_urls:
        if  home_url is not None and len(home_url) > 16 : 
            if ('http://' not in home_url and 'https://' not in home_url):
                home_url = USATODAY_HOME_ROOT + home_url
            try:
                article_home = Article(home_url)
                extract_usatoday_article(article_home, True, usatoday_category.get('tech'))
            except Exception as e:
                print('Smt wrong when process homepage tech  article:  {}'.format(e) + home_url)
                  
                  
                  
                  
                  
    ''' we process homepage travel'''
    USA_TODAY_HOMPAGE_TRAVEL=  'http://www.usatoday.com/travel/'
    usatoday_homepage_travel= requests.get(USA_TODAY_HOMPAGE_TRAVEL)
    html_tree = html.fromstring(usatoday_homepage_travel.text)
    article_urls = html_tree.xpath('//a/@href')
    for home_url in article_urls:
        if  home_url is not None and len(home_url) > 16 : 
            if ('http://' not in home_url and 'https://' not in home_url):
                home_url = USATODAY_HOME_ROOT + home_url
            try:
                article_home = Article(home_url)
                extract_usatoday_article(article_home, True, usatoday_category.get('travel'))
            except Exception as e:
                print('Smt wrong when process homepage travel  article:  {}'.format(e) + home_url)
                  
                  
                  
                  
                      
                      
                      
    ''' we process homepage opinion'''
    USA_TODAY_HOMPAGE_OPINION=  'http://www.usatoday.com/opinion/'
    usatoday_homepage_opinion= requests.get(USA_TODAY_HOMPAGE_OPINION)
    html_tree = html.fromstring(usatoday_homepage_opinion.text)
    article_urls = html_tree.xpath('//a/@href')
    for home_url in article_urls:
        if  home_url is not None and len(home_url) > 16 : 
            if ('http://' not in home_url and 'https://' not in home_url):
                home_url = USATODAY_HOME_ROOT + home_url
            try:
                article_home = Article(home_url)
                extract_usatoday_article(article_home, True, usatoday_category.get('opinion'))
            except Exception as e:
                print('Smt wrong when process homepage opinion  article:  {}'.format(e) + home_url)
                  
                      
                      
                      
                      
                      
                      
    '''
    we process homepage here, to find out what has been showed in homepage
    '''         
    usatoday_homepage = requests.get(USATODAY_HOME_ROOT)
    html_tree = html.fromstring(usatoday_homepage.text)
    article_urls = html_tree.xpath('//a/@href')
    for home_url in article_urls:
        if ('http://' not in home_url and 'https://' not in home_url):
            home_url = USATODAY_HOME_ROOT + home_url
        try:
            article_home = Article(home_url)
            extract_usatoday_article(article_home, True)
        except Exception as e:
            print('Smt wrong when process homepage article:  {}'.format(e) + home_url)
                       
                       
                      
                      
                      
                      
    db_connect.close_database_cont()   
except Exception as e:        
    print('Something went wrong with database: {}'.format(e))
                      
                      
    '''
    =======================================================================================================================================
    =======================================================================================================================================
    ================================================= USA TODAY stop ======================================================================
    =======================================================================================================================================
    =======================================================================================================================================
    '''
                  
                 
          
    
    
    
    
    
    
    
    
    
    
        
'''
=======================================================================================================================================
=======================================================================================================================================
============================================================= Pople start ============================================================
=======================================================================================================================================
=======================================================================================================================================
''' 
          
people_category = {'International' : 'world',
                'Sports' : 'sport',
                'U.S.' : 'news',
                'Arts & Entertainment' : 'entertainment',
                'Business' : 'business', 
                'Media & Entertainment' : 'entertainment',
                'Investing' : 'business',
                'Markets' : 'business',
                'Stocks' : 'business',
                'Careers' : 'business',
                'Entrepreneurs' : 'business',
                'Powering Productivity' : 'business',
                'Small Business Strategies' : 'business',
                'Leaders' : 'business',
                'Mobile' : 'tech',
                'Tech' : 'tech',
                'Powering Productivity' : 'business',
                'Real Estate' : 'business',
                'Retirement' : 'business',
                'ETFs' : 'business',
                'Gold & Commodities' : 'business',
                    
                }
           
               
people_except = { 
                        
              }    
           
people_home_pages = {'http://www.peoplestylewatch.com/',
                     'http://stylenews.peoplestylewatch.com/',
                     'http://www.peoplestylewatch.com/people/stylewatch/mediapackage/0,,20201637,00.html',
                     'http://www.peoplestylewatch.com/people/stylewatch/mediapackage/0,,20201666,00.html',
                     'http://www.peoplestylewatch.com/people/stylewatch/mediapackage/0,,20755486,00.html',
                             
                  }    
               
               
               
               
               
def extract_people_article(article, is_on_homepage, predifined_category=None):
               
    if ('201' not in article.url or article.url in people_except or article.url + '/' in people_except or 'peoplestylewatch' not in article.url or article.url in people_home_pages): 
        return
    if('ttp://www.facebook.com/share' in article.url or 'https://twitter.com/intent/' in article.url):
        return
    print('\n\n')
    print("url to extract: " + article.url)
    if (db_connect.is_url_existed(article.url) != -1):
        print("url is already existed")
        url_sharelikecomment_queue.put(article.url, True)
        return
              
    print('\n')
    normalized_url  = normalize_url(article.url)
    if ('peoplestylewatch' not in normalized_url):
        return
    if (normalized_url in people_except or normalized_url + '/' in people_except):
        return
    if (db_connect.is_url_existed(normalized_url) != -1):
        print("url is already existed")
        url_sharelikecomment_queue.put(normalized_url, True)
        return
               
    article.category_id = None
    article.thumbnail_url = None
    article.short_description = None
    article.published_time = None
    article.title = None
    article.source_id = None
    article.id = None
               
                
    time_string = None
    title = None
    thumbnail_url = None
    short_description = None
    category_id = None
                
    article.download()
    html_tree = html.fromstring(article.html)
                
               
    #time 
    try:
        time_string = html_tree.xpath('//meta[@name="DATE_PUBLISHED"]')[0].attrib['content']
        time_string = time_string + " -4:00"
        time_string = time_string.replace("|" , "")
        print("extracted time: " + time_string)
        #time_string = time_string + " UTC-0400"
    except BaseException as dateE:
        print("problem with time: {}".format(dateE))
                
    date_time = parse(time_string)
    published_time = calendar.timegm(date_time.utctimetuple())
    print("time saved: ")
    print(datetime.fromtimestamp(published_time))
    print(published_time)
    if (published_time > time.time()):
        published_time = None
    article.published_time = published_time
               
               
    #title
    try:
        title = html_tree.xpath('//meta[@property="og:title"]')[0].attrib['content']
    except Exception as e:
        print("")
              
    try:
        if(title is None):
            title = html_tree.xpath('//title/text()')[0].split('|')[0]
    except Exception as e:
        print("Title not found {}".format(e))
    article.title = title
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
    try:
        if(thumbnail_url is None):
            thumbnail_url = html_tree.xpath('//meta[@name="IMAGE_PATH_FULL"]')[0].attrib['content']
            print(thumbnail_url)
    except Exception as e:
        print('Thumbnaill not found again'.format(e))
    article.thumbnail_url = thumbnail_url
                   
                   
               
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
    article.short_description = short_description
               
               
    # get category
    article.category_id = 'style'
              
              
               
    if (article.published_time is None or article.title is None or article.thumbnail_url is None):
        raise Exception("missing fields")
               
               
               
    article.source_name = "PEOPLE.COM"          
    # get content
    article.parse()
    text = normalize_text(article.text)
    text_html = true_html.escape(get_text_html_saulify(normalized_url), True)
    normalized_title = normalize_text_nostop(article.title)
    article.source_id = people_source_id
     
    ''' insert this article to database, maybe send url to another thread to get count, share, .... or maket it asynchronous'''
    # when no exception, we insert to database
    try:
        article.id = db_connect.insert_article3(normalized_url, article.title, people_source_id, 
                                     article.category_id, False, is_on_homepage, article.published_time,
                                     article.thumbnail_url, article.short_description, USA, text_html, text, normalized_title)
    except Exception as dbE:
        print("Error when insert article to db. {}".format(dbE))
    # after insert to database, we put this url to get share, comment, like
    url_sharelikecomment_queue.put(normalized_url, True)
    article.url = normalized_url
    post_queue.put(article, True)
           
           
          
          
          
          
          
print('...................................................\n' +
      '...................................................\n' + 
      '...................................................\n' +
      'start get articles from Forbes news' +
      '...................................................\n' +
      '...................................................\n'
      )
try:
    db_connect = IIIDatbaseConnection()
    db_connect.init_database_cont()     
              
              
              
    ''' we process homepage'''
    for home_page in people_home_pages:
        print("extracting: " + home_page)
        page = requests.get(home_page)
        html_tree = html.fromstring(page.text)
        article_urls = html_tree.xpath('//a/@href')
        for home_url in article_urls:
            if  home_url is not None and len(home_url) > 16: 
                if ('http://' not in home_url and 'https://' not in home_url):
                    home_url = PEOPLE_HOME + home_url
                try:
                    article_home = Article(home_url)
                    extract_people_article(article_home, True, None)
                except Exception as e:
                    print('Smt wrong when process homepage ' + home_page +  ' article:  {}'.format(e) + home_url)
              
              
              
              
              
              
              
              
           
    db_connect.close_database_cont()   
except Exception as e:        
    print('Something went wrong with database: {}'.format(e))    
              
           
          
          
          
'''
=======================================================================================================================================
=======================================================================================================================================
========================================================== poeple stop ==============================================================
=======================================================================================================================================
=======================================================================================================================================
''' 
          
        
        
    
    
    
    
    
    
          
          
          
          
         
         
         
         
         
         
         
         
         
         
         
         
                
                
                
                
                
                
                   
                   
      
      
      
      
      
'''
=======================================================================================================================================
=======================================================================================================================================
============================================================= Forbes start ===========================================================
=======================================================================================================================================
=======================================================================================================================================
''' 
        
forbes_category = {'International' : 'world',
                'Sports' : 'sport',
                'U.S.' : 'news',
                'Arts & Entertainment' : 'entertainment',
                'Business' : 'business', 
                'Media & Entertainment' : 'entertainment',
                'Investing' : 'business',
                'Markets' : 'business',
                'Stocks' : 'business',
                'Careers' : 'business',
                'Entrepreneurs' : 'business',
                'Powering Productivity' : 'business',
                'Small Business Strategies' : 'business',
                'Leaders' : 'business',
                'Mobile' : 'tech',
                'Tech' : 'tech',
                'Powering Productivity' : 'business',
                'Real Estate' : 'business',
                'Retirement' : 'business',
                'ETFs' : 'business',
                'Gold & Commodities' : 'business',
                'CEO Network' : 'business',
                'Health' : 'health',
                'Pharma & Healthcare' : 'health',
                'Innovation & Science' : 'science',
                'Security' : 'tech',
                'Gear' : 'tech',
                'Corporate Responsibility' : 'business',
                'Doing Well By Doing Good' : 'business',
                'Opinion' : 'opinions',
                'Politics' : 'opinions',
                'Science & Technology' : 'opinions',
                'Energy & Environment' : 'opinions',
                "Democracy's Problems And Prospects" : 'politics',
                'Healthcare, Fiscal, and Tax' : 'politics',
                'Economics & Finance' : 'opinions',
                'Law & Regulation' : 'opinions',
                'Science  Technology' : 'opinions',
                'Food & Drink' : 'entertainment',
                'Travel' : 'travel',
                'Forbes Travel Guide' : 'travel',
                'Lifestyle' : 'entertainment',
                'Sports & Leisure' : 'entertainment',
                'Sports & Leisure' : 'sport',
                'SportsMoney' : 'sport',
                'ForbesLife' : 'life',
                'Watches & Jewelry' : 'style',
                'Law & Regulation' : 'opinions',
                'Taxes' : 'business',
                'Leaders' : 'business',
                'Sales Leadership' : 'business',
                'Leadership' : 'business',
                'Media  Entertainment' : 'entertainment',
                'Media &amp; Entertainment' : 'entertainment',
                 'CMO Network' : 'business',
                 'CIO Next' : 'tech',
                 'Asia' : 'world',
                 'Europe': 'world',
                 'Intelligent Investing' : 'business'
                }
         
             
forbes_except = { 
                      
              }    
         
forbes_home_pages = {'http://www.forbes.com/business/' : 'business',
                  'http://www.forbes.com/investing/' : 'business',
                  'http://www.forbes.com/technology/' : 'tech',
                  'http://www.forbes.com/entrepreneurs/' : 'business',
                  'http://www.forbes.com/opinion/' : 'opinions',
                  'http://www.forbes.com/lifestyle/' : 'life',
                  FORBES_HOME : None
                  }    
             
             
             
             
             
def extract_forbes_article(article, is_on_homepage, predifined_category=None):
             
    if ('201' not in article.url or article.url in forbes_except or article.url + '/' in forbes_except or 'forbes.com' not in article.url): 
        return
    print('\n\n')
    print("url to extract: " + article.url)
    if (db_connect.is_url_existed(article.url) != -1):
        print("url is already existed")
        url_sharelikecomment_queue.put(article.url, True)
        return
            
    print('\n')
    normalized_url  = normalize_url(article.url)
    if ('forbes.com' not in normalized_url):
        return
    if (normalized_url in forbes_except or normalized_url + '/' in forbes_except):
        return
    if (db_connect.is_url_existed(normalized_url) != -1):
        print("url is already existed")
        url_sharelikecomment_queue.put(normalized_url, True)
        return
             
    article.category_id = None
    article.thumbnail_url = None
    article.short_description = None
    article.published_time = None
    article.title = None
    article.source_id = None
    article.id = None
             
              
    time_string = None
    title = None
    thumbnail_url = None
    short_description = None
    category_id = None
              
    article.download()
    html_tree = html.fromstring(article.html)
              
             
    #time 
    try:
        time_string = html_tree.xpath('//time[@itemprop="datePublished"]')[0].attrib['content']
        #time_string = time_string + " -4:00"
        print("extracted time: " + time_string)
        #time_string = time_string + " UTC-0400"
    except BaseException as dateE:
        print("problem with time: {}".format(dateE))
    try:
        if (time_string is None):
            time_string = html_tree.xpath('//time[@class="storyDate"]')[0].attrib['datetime']
            print("extracted time: " + time_string)   
    except BaseException as dateE:
        print("problem with time: {}".format(dateE))
              
    date_time = parse(time_string)
    published_time = calendar.timegm(date_time.utctimetuple())
    print("time saved: ")
    print(datetime.fromtimestamp(published_time))
    print(published_time)
    if (published_time > time.time()):
        published_time = None
    article.published_time = published_time
             
             
    #title
    try:
        title = html_tree.xpath('//meta[@property="og:title"]')[0].attrib['content']
    except Exception as e:
        print("")
            
    try:
        if(title is None):
            title = html_tree.xpath('//title/text()')[0].split('|')[0]
    except Exception as e:
        print("Title not found {}".format(e))
    article.title = title
    print(title)
             
             
             
    # get thumbnail
    try:
        thumbnail_url = html_tree.xpath('//meta[@name="sailthru.image.full"]')[0].attrib['content']
        print(thumbnail_url)
    except Exception as e:
        print('Thumbnaill not found.'.format(e))
    try:
        if(thumbnail_url is None):
            thumbnail_url = html_tree.xpath('//meta[@property="og:image"]')[0].attrib['content']
            print(thumbnail_url)
    except Exception as e:
        print('Thumbnaill not found again'.format(e))
    article.thumbnail_url = thumbnail_url
                 
                 
             
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
    article.short_description = short_description
             
             
    # get category
    try:
        category_id = html_tree.xpath('//meta[@property="article:section"]')[0].attrib['content']
        print("category: " + category_id)
    except Exception as e:
        print('Category not found'.format(e))
    try:
        if (category_id is None):
            category_id = html_tree.xpath('//meta[@property="article:section"]')[1].attrib['content']
    except Exception as e:
        print('Category not found'.format(e))
          
    if (category_id is not None and category_id in forbes_category):
        article.category_id = forbes_category.get(category_id)
    if ('forbestravelguide/201' in article.url) :
        article.category_id = 'travel'
    print(article.category_id)
            
            
             
    if (article.published_time is None or article.title is None or article.category_id is None):
        raise Exception("missing fields")
             
             
             
    article.source_name = "FORBES.COM"    
    # get content
    article.parse()
    text = normalize_text(article.text)
    text_html = true_html.escape(get_text_html_saulify(normalized_url), True)
    normalized_title = normalize_text_nostop(article.title)
    article.source_id =forbes_source_id
     
    ''' insert this article to database, maybe send url to another thread to get count, share, .... or maket it asynchronous'''
    # when no exception, we insert to database
    try:
        article.id = db_connect.insert_article3(normalized_url, article.title, forbes_source_id, 
                                     article.category_id, False, is_on_homepage, article.published_time,
                                     article.thumbnail_url, article.short_description, USA, text_html, text, normalized_title)
    except Exception as dbE:
        print("Error when insert article to db. {}".format(dbE))
    # after insert to database, we put this url to get share, comment, like
    url_sharelikecomment_queue.put(normalized_url, True)
    article.url = normalized_url
    post_queue.put(article, True)
         
         
        
        
        
        
        
print('...................................................\n' +
      '...................................................\n' + 
      '...................................................\n' +
      'start get articles from Forbes news' +
      '...................................................\n' +
      '...................................................\n'
      )
try:
    db_connect = IIIDatbaseConnection()
    db_connect.init_database_cont()     
            
            
            
    ''' we process homepage'''
    for home_page in forbes_home_pages:
        print("extracting: " + home_page)
        page = requests.get(home_page)
        html_tree = html.fromstring(page.text)
        article_urls = html_tree.xpath('//a/@href')
        for home_url in article_urls:
            if  home_url is not None and len(home_url) > 16: 
                if ('http://' not in home_url and 'https://' not in home_url):
                    home_url = FORBES_HOME + home_url
                try:
                    article_home = Article(home_url)
                    extract_forbes_article(article_home, True, forbes_home_pages.get(home_page))
                except Exception as e:
                    print('Smt wrong when process homepage ' + home_page +  ' article:  {}'.format(e) + home_url)
            
            
            
            
            
            
            
            
         
    db_connect.close_database_cont()   
except Exception as e:        
    print('Something went wrong with database: {}'.format(e))    
            
         
        
        
        
'''
=======================================================================================================================================
=======================================================================================================================================
========================================================== Forbes news stop ==============================================================
=======================================================================================================================================
=======================================================================================================================================
''' 
       
       
       
     
     
     
     
     
     
     
     
     
     
     
     
     
uproxx_except = {}
     
'''
=======================================================================================================================================
=======================================================================================================================================
============================================================= UPROXX start ===========================================================
=======================================================================================================================================
=======================================================================================================================================
''' 
     
def extract_uproxx_article(article, is_on_homepage, predifined_category=None):
            
    if ('201' not in article.url or article.url in uproxx_except or article.url + '/' in uproxx_except or 'uproxx.com' not in article.url): 
        return
    print('\n\n')
    print("url to extract: " + article.url)
    if (db_connect.is_url_existed(article.url) != -1):
        print("url is already existed")
        url_sharelikecomment_queue.put(article.url, True)
        return
           
    print('\n')
    normalized_url  = normalize_url(article.url)
    if ('uproxx.com' not in normalized_url):
        return
    if (normalized_url in uproxx_except or normalized_url + '/' in uproxx_except):
        return
    if (db_connect.is_url_existed(normalized_url) != -1):
        print("url is already existed")
        url_sharelikecomment_queue.put(normalized_url, True)
        return
          
          
    article.category_id = None
    article.thumbnail_url = None
    article.short_description = None
    article.published_time = None
    article.title = None
    article.source_id = None
    article.id = None 
    time_string = None
    short_description = None
    article.download()
    html_tree = html.fromstring(article.html)
             
            
      
    # get parse page object
    try:
        parse_page_obj = html_tree.xpath('//meta[@name="parsely-page"]')[0].attrib['content']
        parse_page_json = json.loads(parse_page_obj)
        article.title = parse_page_json['title']
        article.thumbnail_url = parse_page_json['image_url']
        time_string = parse_page_json['pub_date']
        date_time = parse(time_string)
        article.published_time = calendar.timegm(date_time.utctimetuple())
        article.category_id = 'community'
        print(parse_page_obj)
    except BaseException as dateE:
        print("problem with parse page: {}".format(dateE))   
      
            
  
            
    # get description
    try:
        short_description = html_tree.xpath('//meta[@name="twitter:description"]')[0].attrib['content']
        print(short_description)
    except Exception as e:
        print('Description not found'.format(e))    
    try:
        if(short_description is None):
            short_description = html_tree.xpath('//meta[@name="description"]')[0].attrib['content']
            print(short_description)
    except Exception as e:
        print('Description not found again'.format(e))
    article.short_description = short_description
            
                 
  
    if (article.published_time is None or article.title is None or article.category_id is None):
        raise Exception("missing fields")
            
            
            
    article.source_name = "UPROXX.COM"          
    # get content
    article.parse()
    text = normalize_text(article.text)
    text_html = true_html.escape(get_text_html_saulify(normalized_url), True)
    normalized_title = normalize_text_nostop(article.title)
    article.source_id = uproxx_source_id
     
    ''' insert this article to database, maybe send url to another thread to get count, share, .... or maket it asynchronous'''
    # when no exception, we insert to database
    try:
        article.id = db_connect.insert_article3(normalized_url, article.title, uproxx_source_id, 
                                     article.category_id, False, is_on_homepage, article.published_time,
                                     article.thumbnail_url, article.short_description, USA, text_html, text, normalized_title)
    except Exception as dbE:
        print("Error when insert article to db. {}".format(dbE))
    # after insert to database, we put this url to get share, comment, like
    url_sharelikecomment_queue.put(normalized_url, True)
    article.url = normalized_url
    post_queue.put(article, True)
  
   
   
   
   
   
   
print('...................................................\n' +
      '...................................................\n' + 
      '...................................................\n' +
      'start get articles from Uproxx news' +
      '...................................................\n' +
      '...................................................\n'
      )
try:
    db_connect = IIIDatbaseConnection()
    db_connect.init_database_cont()     
           
           
           
    ''' we process homepage only'''
    page = requests.get(UPROXX_HOME)
    html_tree = html.fromstring(page.text)
    article_urls = html_tree.xpath('//a/@href')
    for home_url in article_urls:
        if  home_url is not None and len(home_url) > 16: 
            if ('http://' not in home_url and 'https://' not in home_url):
                home_url = UPROXX_HOME + home_url
            try:
                article_home = Article(home_url)
                extract_uproxx_article(article_home, True, None)
            except Exception as e:
                print('Smt wrong when process homepage UPROXX article:  {}'.format(e) + home_url)
           
           
           
           
           
           
           
           
        
    db_connect.close_database_cont()   
except Exception as e:        
    print('Something went wrong with database: {}'.format(e))    
   
   
   
  
  
    
    
    
    
    
    
    
    
 
     
   
   
   
   
   
   
   
   
           
'''
=======================================================================================================================================
=======================================================================================================================================
================================================= IFLoveScience start ===============================================================
=======================================================================================================================================
=======================================================================================================================================
''' 
           
               
               
IfloveScience_except = {
                       
                }
           
               
IfloveScience_category = {'science' : 'science'
                   }    
           
IfloveScience_home_pages = {
                     'http://www.iflscience.com/' : 'science',
                     'http://www.iflscience.com/categories/environment' : 'science',
                     'http://www.iflscience.com/categories/technology' : 'science',
                     'http://www.iflscience.com/categories/brain' : 'science',
                     'http://www.iflscience.com/categories/plants-and-animals' : 'science',
                     'http://www.iflscience.com/categories/physics' : 'science',
                     'http://www.iflscience.com/categories/health-and-medicine' : 'science'
                  }    
               
               
               
               
               
def extract_iflscience_article(article, is_on_homepage, predifined_category=None):
               
    if ('iflscience.com/' not in article.url or 'www.iflscience.com/categories/' in article.url): 
        return
      
    print('\n')
    print("url to extract: " + article.url)
    if (db_connect.is_url_existed(article.url) != -1):
        print("url is already existed")
        url_sharelikecomment_queue.put(article.url, True)
        return
      
    normalized_url  = normalize_url(article.url)
    if ( 'iflscience.com/' not in normalized_url):
        return
    if (normalized_url in IfloveScience_except or normalized_url + '/' in IfloveScience_except):
        return
    if (db_connect.is_url_existed(normalized_url) != -1):
        print("url is already existed")
        url_sharelikecomment_queue.put(normalized_url, True)
        return
               
    article.category_id = None
    article.thumbnail_url = None
    article.short_description = None
    article.published_time = None
    article.title = None
    article.source_id = None
    article.id = None
               
                
    time_string = None
    title = None
    thumbnail_url = None
    short_description = None
    category_id = None
    date_time = None
                
    article.download()
    html_tree = html.fromstring(article.html)
                
               
               
    try:
        time_string = html_tree.xpath('//meta[@property="article:published_time"]')[0].attrib['content']
        print("extracted time: " + time_string)
    except BaseException as dateE:
        print("problem with time: {}".format(dateE))
      
    date_time = parse(time_string)
    published_time = calendar.timegm(date_time.utctimetuple())
    print("time saved: ")
    print(datetime.fromtimestamp(published_time))
    article.published_time = published_time
    if (article.published_time > time.time()):
            article.published_time = None
               
               
    #title
    try:
        title = html_tree.xpath('//meta[@property="og:title"]')[0].attrib['content']
    except Exception as e:
        print("Title not found")
               
    try:
        if(title is None):
            title = html_tree.xpath('//title/text()')[0].split('|')[0]
    except Exception as e:
        print("Title not found {}".format(e))
    article.title = title
    print(title)
               
               
               
    # get thumbnail
    try:
        thumbnail_url = html_tree.xpath('//meta[@property="og:image"]')[0].attrib['content']
        print(thumbnail_url)
    except Exception as e:
        print('Thumbnaill not found.'.format(e))
    try:
        if(thumbnail_url is None):
            thumbnail_url = html_tree.xpath('//meta[@name="twitter:image:src"]')[0].attrib['content']
            print(thumbnail_url)
    except Exception as e:
        print('Thumbnaill not found again'.format(e))
    article.thumbnail_url = thumbnail_url
                   
                   
               
    # get description
    try:
        short_description = html_tree.xpath('//meta[@name="description"]')[0].attrib['content']
        print(short_description)
    except Exception as e:
        print('')    
    try:
        if(short_description is None):
            short_description = html_tree.xpath('//meta[@property="og:description"]')[0].attrib['content']
            print(short_description)
    except Exception as e:
        print('Description not found again'.format(e))
    article.short_description = short_description
               
               
    # get category
    article.category_id = 'science'
               
               
               
               
               
    if (article.published_time is None or article.title is None or article.category_id is None):
        raise Exception("missing fields")
               
               
               
    article.source_name = "IFLScience.COM"           
    # get content
    article.parse()
    text = normalize_text(article.text)
    text_html = true_html.escape(get_text_html_saulify(normalized_url), True)
    normalized_title = normalize_text_nostop(article.title)
    article.source_id = iflovescience_id
             
    ''' insert this article to database, maybe send url to another thread to get count, share, .... or maket it asynchronous'''
    # when no exception, we insert to database
    try:
        article.id = db_connect.insert_article3(normalized_url, article.title, iflovescience_id, 
                                     article.category_id, False, is_on_homepage, article.published_time,
                                     article.thumbnail_url, article.short_description, USA, text_html, text, normalized_title)
    except Exception as dbE:
        print("Error when insert article to db. {}".format(dbE))
    # after insert to database, we put this url to get share, comment, like
    url_sharelikecomment_queue.put(normalized_url, True)
    article.url = normalized_url
    post_queue.put(article, True)
           
           
           
           
               
               
               
               
               
               
               
               
               
               
               
               
               
               
            
print('...................................................\n' +
      '...................................................\n' + 
      '...................................................\n' +
      'start get articles from IfloveScience' +
      '...................................................\n' +
      '...................................................\n'
      )
try:
    db_connect = IIIDatbaseConnection()
    db_connect.init_database_cont()     
               
               
               
    ''' we process homepage'''
    for home_page in IfloveScience_home_pages:
        print("extracting: " + home_page)
        mashable_page = requests.get(home_page)
        html_tree = html.fromstring(mashable_page.text)
        article_urls = html_tree.xpath('//a/@href')
        for home_url in article_urls:
            if  home_url is not None and len(home_url) > 16: 
                if ('http://' not in home_url and 'https://' not in home_url):
                    home_url = IFLove_SCIENC_HOME + home_url
                try:
                    article_home = Article(home_url)
                    extract_iflscience_article(article_home, True, IfloveScience_home_pages.get(home_page))
                except Exception as e:
                    print('Smt wrong when process homepage' + home_page +  'article:  {}'.format(e) + home_url)
               
               
               
               
               
               
               
               
            
    db_connect.close_database_cont()   
except Exception as e:        
    print('Something went wrong with database: {}'.format(e))    
               
               
           
'''
=======================================================================================================================================
=======================================================================================================================================
================================================= IfloveScience news stop ===============================================================
=======================================================================================================================================
=======================================================================================================================================
''' 
         
  
  












           
           
'''
=======================================================================================================================================
=======================================================================================================================================
===================================================== Newyork Daily news start ========================================================
=======================================================================================================================================
=======================================================================================================================================
''' 
           
newyorkdaily_category = {'US' : 'news',
                'U.S.' : 'news',
                'NYC Crime' : 'news',
                'New York' : 'news',
                'World' : 'world',
                'Politics' : 'politics',
                'Entertainment' : 'entertainment',
                'Gossip' : 'entertainment',
                'TV' : 'entertainment',
                'Confidential' : 'entertainment',
                'Movies' : 'entertainment',
                'Music' : 'entertainment',
                'channel-surfer' : 'entertainment', 
                'Theater &amp; Arts' : 'entertainment',
                'Theater & Arts' : 'entertainment',
                'Opinion' : 'opinions',
                'Soccer' : 'sport',
                'Basketball' : 'sport',
                'Jets' : 'sport',
                'Giants' : 'sport',
                'Football' : 'sport',
                'Mets' : 'sport',
                'Hockey' : 'sport',
                'Knicks' : 'sport',
                'Rangers' : 'sport',
                'Yankees' : 'sport',
                'Homes' : 'life',
                'Food' : 'life',
                'Horoscopes' : 'life',
                'Health' : 'health',
                'Lifestyle' : 'life',
                'Education' : 'education',
                'Sports' : 'sport',
                'Crime' : 'news',
                'Living' : 'life'
                }
            
                
newyorkdaily_except = { }    
            
newyorkdaily_home_pages = {'http://www.nydailynews.com/new-york' : 'news',
                           'http://www.nydailynews.com/news' : 'news',
                           'http://www.nydailynews.com/news/national' : 'news',
                           'http://www.nydailynews.com/news/world' : 'world',
                          'http://www.nydailynews.com/news/politics' : 'politics',
                          'http://www.nydailynews.com/entertainment' : 'entertainment',
                          'http://www.nydailynews.com/opinion' : 'opinions',
                          'http://www.nydailynews.com/life-style/health' : 'health',
                          'http://www.nydailynews.com/new-york/education' : 'education',
                          'http://www.nydailynews.com/life-style' : 'life',
                          'http://www.nydailynews.com/sports' : 'sport',
                          'http://www.nydailynews.com' : None,
                  }    
                
                
                
                
                
def extract_newyorkdaily_article(article, is_on_homepage, predifined_category=None):
                
    if (  article.url in newyorkdaily_except or article.url + '/' in newyorkdaily_except or 'nydailynews.com' not in article.url): 
        return
    if (not hasNumbers(article.url)):
        return
    print('\n\n')
    print("url to extract: " + article.url)
    if (db_connect.is_url_existed(article.url) != -1):
        print("url is already existed")
        url_sharelikecomment_queue.put(article.url, True)
        return
      
    normalize_url = article.url.split("#")[0].split("&")[0];
    print("normalized url: " + normalize_url)
    if (db_connect.is_url_existed(normalize_url) != -1):
        print("url is already existed")
        url_sharelikecomment_queue.put(normalize_url, True)
        return         
                
    article.category_id = None
    article.thumbnail_url = None
    article.short_description = None
    article.published_time = None
    article.title = None
    article.source_id = None
    article.id = None
                
                 
    time_string = None
    title = None
    thumbnail_url = None
    short_description = None
    category_id = None
                 
    article.download()
    html_tree = html.fromstring(article.html)
                 
                
    #time 
    try:
        time_string = html_tree.xpath('//meta[@name="parsely-pub-date"]')[0].attrib['content']
        print("extracted time: " + time_string)
        #time_string = time_string + " UTC-0400"
    except BaseException as dateE:
        print("problem with time: {}".format(dateE))
    date_time = parse(time_string)
    published_time = calendar.timegm(date_time.utctimetuple())
    print(published_time)
    if (published_time > time.time()):
        published_time = None
    article.published_time = published_time
                
                
    #title
    try:
        title = html_tree.xpath('//meta[@property="og:title"]')[0].attrib['content']
    except Exception as e:
        print("")
               
    try:
        if(title is None):
            title = html_tree.xpath('//title/text()')[0].split('|')[0]
    except Exception as e:
        print("Title not found {}".format(e))
    article.title = title
    print(title)
                
                
                
    # get thumbnail
    try:
        thumbnail_url = html_tree.xpath('//meta[@name="parsely-image-url"]')[0].attrib['content']
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
    article.thumbnail_url = thumbnail_url
                    
                    
                
    # get description
    try:
        short_description = html_tree.xpath('//meta[@twitter:description"]')[0].attrib['content']
        print(short_description)
    except Exception as e:
        print('')
    try:
        if(short_description is None):
            short_description = html_tree.xpath('//meta[@name="description""]')[0].attrib['content']
            print(short_description)
    except Exception as e:
        print('') 
    try:
        if(short_description is None):
            short_description = html_tree.xpath('//meta[@property="og:description"]')[0].attrib['content']
            print(short_description)
    except Exception as e:
        print('')
    article.short_description = short_description
                
                
    # get category
    try:
        category_id = html_tree.xpath('//meta[@name="nydn_section"]')[0].attrib['content']
        print(category_id)
    except Exception as e:
        print('Category not found'.format(e))
        
    try:
        if category_id is None:
            category_id = html_tree.xpath('//meta[@name="parsely-section"]')[0].attrib['content']
            print(category_id)
    except Exception as e:
        print('Category not found again'.format(e))
                    
    if (category_id is not None and category_id in newyorkdaily_category):
        article.category_id = newyorkdaily_category.get(category_id)
    print(article.category_id)
                
                
    if (article.published_time is None or article.title is None or article.category_id is None):
        raise Exception("missing fields")
                
                
                
    article.source_name = "NY DAILY NEWS"           
    # get content
    article.parse()
    text = normalize_text(article.text)
    text_html = true_html.escape(get_text_html_saulify(article.url), True)
    normalized_title = normalize_text_nostop(article.title)
    article.source_id = nydaily_news_id
     
    ''' insert this article to database, maybe send url to another thread to get count, share, .... or maket it asynchronous'''
    # when no exception, we insert to database
    try:
        article.id = db_connect.insert_article3(normalize_url, article.title, nydaily_news_id, 
                                     article.category_id, False, is_on_homepage, article.published_time,
                                     article.thumbnail_url, article.short_description, USA, text_html, text,normalized_title)
    except Exception as dbE:
        print("Error when insert article to db. {}".format(dbE))
    # after insert to database, we put this url to get share, comment, like
    url_sharelikecomment_queue.put(normalize_url, True)
    article.url = normalize_url
    post_queue.put(article, True)
            
            
           
           
           
           
           
print('...................................................\n' +
      '...................................................\n' + 
      '...................................................\n' +
      'start get articles from abc news' +
      '...................................................\n' +
      '...................................................\n'
      )
try:
    db_connect = IIIDatbaseConnection()
    db_connect.init_database_cont()     
               
               
               
    ''' we process homepage'''
    for home_page in newyorkdaily_home_pages:
        print("extracting: " + home_page)
        abc_page = requests.get(home_page)
        html_tree = html.fromstring(abc_page.text)
        article_urls = html_tree.xpath('//a/@href')
        for home_url in article_urls:
            if  home_url is not None and len(home_url) > 16: 
                if ('http://' not in home_url and 'https://' not in home_url):
                    home_url = NY_DAILY_NEWS_HOME + home_url
                try:
                    article_home = Article(home_url)
                    extract_newyorkdaily_article(article_home, True, newyorkdaily_home_pages.get(home_page))
                except Exception as e:
                    print('Smt wrong when process homepage ' + home_page +  ' article:  {}'.format(e) + home_url)
               
        
               
               
               
               
               
               
            
    db_connect.close_database_cont()   
except Exception as e:        
    print('Something went wrong with database: {}'.format(e))    
               
            
           
           
           
               
           
           
           
'''
=======================================================================================================================================
=======================================================================================================================================
===================================================== NYDaily News stop ===============================================================
=======================================================================================================================================
=======================================================================================================================================
''' 












 
  
  
  
  
  
  
  
  
 







'''============================================================================
we stop thread getting like, share, comment count here by putting poison in to queue
'''
try:
    url_sharelikecomment_queue.put(POISON, True)
    print("thread get like, comment stopped")
except Exception as e:
    print("cannot stop other thread: {}".format(e))
    
try:
    post_queue.put(POISON, True)
    print("thread post to fb stopped")
except Exception as e:
    print("cannot stop post to FB page: {}".format(e))
