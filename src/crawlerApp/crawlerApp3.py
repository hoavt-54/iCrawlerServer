'''
Created on Mar 15, 2015

@author: hoavu
'''

from apt.progress.text import long
import calendar
from datetime import datetime
from dateutil.parser import parse
from dateutil import tz
from lxml import html
from newspaper.article import Article
import os.path
import queue
import re
import json
import requests
import sys
import time

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from extractContent.buzzFeedContentExtractor import buzzFeedContentExtractor
from crawlerApp.PostAndGetFromFbPages import CommentLikeShrareGetterThread, \
    POISON, PostToFacebookPage
from crawlerApp import PostAndGetFromFbPages
from crawlerApp.utils import normalize_url, get_text_html_saulify, \
    normalize_text, hasNumbers, normalize_text_nostop, time_from_short_string,\
    unix_time_to_string
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
                    'politics' : 'politics',
                    'china' : 'world',
                    'asia' : 'world',
                    'middle-east' : 'world',
                    'europe' : 'world'
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
NBC_HOMEPAGE = 'http://www.nbcnews.com'
ABC_HOMEPAGE = 'http://abcnews.go.com'
LA_TIMES_HOMEPAGE = 'http://www.latimes.com'
NEWYORKTIME_HOME = "http://www.nytimes.com"
WASHINGTON_POST = 'http://www.washingtonpost.com'
CBS_NEWS_HOME = 'http://www.cbsnews.com'
BLOOMBERG_HOME_PAGE = 'http://www.bloomberg.com/'
FOX_NEWS_HOME = 'http://www.foxnews.com'
ESPN_HOME = 'http://espn.go.com'
BUZZFEED_HOME = 'http://www.buzzfeed.com'
FORBES_HOME = 'http://www.forbes.com'
PEOPLE_HOME = 'http://www.people.com'
VOGUE_HOME = 'http://www.vogue.com/?us_site=y'
EVERYDAY_HEATH_HOME = 'http://www.everydayhealth.com'
EONLINE_HOME = 'http://www.eonline.com';
TECHCRUNCH_HOME = 'http://techcrunch.com'
BLEACH_REPORT = 'http://bleacherreport.com'
BUSINESS_INSIDER = 'http://www.businessinsider.com'
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
business_insider_id = 'business_insider'
USA = 'us'








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
post_queue = queue.Queue(30)
page_poster_thread = PostToFacebookPage(queue=post_queue, ids=PostAndGetFromFbPages.pages_ids3, tokens=PostAndGetFromFbPages.pages_tokens3)
page_poster_thread.start()
'''
============================================================================================
'''  








 
 
 
  
  
       
         
          
'''
=======================================================================================================================================
=======================================================================================================================================
============================================================= bloomberg start ==========================================================
=======================================================================================================================================
=======================================================================================================================================
''' 
           
bloomberg_category = {'technology' : 'tech',
                'industries' : 'business',
                'markets' : 'business',
                'world' : 'World',
                'businessweek-magazine' : 'business',
                'science-energy' : 'science',
                }
            
                
bloomberg_except = { 
                         
              }    
            
bloomberg_home_pages = {'http://www.bloomberg.com/markets/' : 'business',
                  'http://www.bloomberg.com/' : None,
                  'http://www.bloomberg.com/news/science-energy' : 'science',
                  'http://www.bloomberg.com/technology/' : 'tech',
                  'http://www.bloomberg.com/politics/' : 'politics',
                  'http://www.bloomberg.com/news/world' : 'world',
                  'http://www.bloomberg.com/news/industries' : 'business'
                  }    
                
                
                
                
                
def extract_bloomberg_article(article, is_on_homepage, predifined_category=None):
                
    if ('201' not in article.url or article.url in bloomberg_except or article.url + '/' in bloomberg_except or 'bloomberg' not in article.url): 
        return
    print('\n\n')
    #print("url to extract: " + article.url)
    if (db_connect.is_url_existed(article.url) != -1):
        print("url is already existed")
        url_sharelikecomment_queue.put(article.url, True)
        return
               
                
    article.category_id = None
    article.thumbnail_url = None
    article.short_description = None
    article.published_time = None
    article.title = None
    article.source_id = None
    article.id = None
                
    text_html = None 
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
    except BaseException as dateE:
        print("problem with time: {}".format(dateE))
    try:
        if time_string is None:
            time_string = html_tree.xpath('//time[@itemprop="datePublished"]')[0].attrib['datetime']
    except BaseException as dateE:
        print("problem with time: {}".format(dateE))
    date_time = parse(time_string)
    published_time = calendar.timegm(date_time.utctimetuple())
    if (published_time > time.time()):
        published_time = None
    print(published_time)
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
        thumbnail_url = html_tree.xpath('//meta[@property="og:image"]')[0].attrib['content']
        print(thumbnail_url)
    except Exception as e:
        print('Thumbnaill not found.'.format(e))
    try:
        if(thumbnail_url is None):
            thumbnail_url = html_tree.xpath('//meta[@name="parsely-image-url"]')[0].attrib['content']
            print(thumbnail_url)
    except Exception as e:
        print('Thumbnaill not found again'.format(e))
    try:
        if(thumbnail_url is None):
            thumbnail_url = html_tree.xpath('//meta[@name="thumbnail"]')[0].attrib['content']
            print(thumbnail_url)
    except Exception as e:
        print('Thumbnaill not found again'.format(e))
    if (thumbnail_url is not None and thumbnail_url.startswith("//")):
        thumbnail_url = "http:" + thumbnail_url    
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
    
    
    #keywords
    keywords = ""; 
    try:
        keywords = html_tree.xpath('//meta[@name="keywords"]')[0].attrib['content']
        keywords = keywords.lower();
    except Exception as e:
        print("")
                
                
    # get category
    try:
        category_id = html_tree.xpath('//meta[@name="parsely-section"]')[0].attrib['content']
    except Exception as e:
        print('Category not found'.format(e))
                    
    if (category_id is not None and category_id in bloomberg_category):
        article.category_id = bloomberg_category.get(category_id)
    if ('bloomberg.com/politics/' in article.url):
        article.category_id = 'politics'
           
    if (article.category_id == None):
        article.category_id = predifined_category
    print(article.category_id)
               
               
                
    if (article.published_time is None or article.title is None or article.category_id is None):
        raise Exception("missing fields")
                
                
                
    article.source_name = "BLOOMBERG.COM"          
    # get content
    article.parse()
    if (len(keywords) < 2): # no keywords
        article.nlp()
        for key in article.keywords:
            keywords = keywords + key + ","
        keywords = keywords[0:-1]
    text = normalize_text(article.text)
    try:
        text_html = true_html.escape(article.article_html, True)
    except Exception as ee:
        print("cannot get simplified text from saulify")
    normalized_title = normalize_text_nostop(article.title)    
    article.source_id = bloomberg_source_id
    
    ''' insert this article to database, maybe send url to another thread to get count, share, .... or maket it asynchronous'''
    # when no exception, we insert to database
    try:
        article.id = db_connect.insert_article3(article.url, article.title, bloomberg_source_id, 
                                     article.category_id, False, is_on_homepage, article.published_time,
                                     article.thumbnail_url, article.short_description, USA, text_html,
                                      text, normalized_title, keywords)
    except Exception as dbE:
        print("Error when insert article to db. {}".format(dbE))
    # after insert to database, we put this url to get share, comment, like
    url_sharelikecomment_queue.put(article.url, True)
    article.url = article.url
    post_queue.put(article, True)
            
            
           
           
            
            
            
print('...................................................\n' +
      '...................................................\n' + 
      '...................................................\n' +
      'start get articles from bloomberg' +
      '...................................................\n' +
      '...................................................\n'
      )
try:
    db_connect = IIIDatbaseConnection()
    db_connect.init_database_cont()     
                
                
                
    ''' we process homepage'''
    for home_page in bloomberg_home_pages:
        print("extracting: " + home_page)
        page = requests.get(home_page)
        html_tree = html.fromstring(page.text)
        article_urls = html_tree.xpath('//a/@href')
        for home_url in article_urls:
            if  home_url is not None and len(home_url) > 16: 
                if ('http://' not in home_url and 'https://' not in home_url):
                    if ("news/" in home_url):
                        home_url = BLOOMBERG_HOME_PAGE + home_url
                    else:
                        home_url = home_page + home_url
                try:
                    article_home = Article(home_url, keep_article_html=True)
                    extract_bloomberg_article(article_home, True, bloomberg_home_pages.get(home_page))
                except Exception as e:
                    print('Smt wrong when process homepage ' + home_page +  ' article:  {}'.format(e) + home_url)
                
                
                
                
                
                
                
                
             
    db_connect.close_database_cont()   
except Exception as e:        
    print('Something went wrong with database: {}'.format(e))    
                
             
            
            
           
           
           
           
'''
=======================================================================================================================================
=======================================================================================================================================
========================================================== bloomberg stop ==============================================================
=======================================================================================================================================
=======================================================================================================================================
''' 
          
          
          
          
          
          
          
          
          
          
          
'''
=======================================================================================================================================
=======================================================================================================================================
============================================================= FoxNews start ===========================================================
=======================================================================================================================================
=======================================================================================================================================
''' 
          
foxnews_category = {'us' : 'news',
                'politics' : 'politics',
                'opinion' : 'opinions',
                'entertainment' : 'entertainment',
                'tech' : 'tech',
                'science' : 'science',
                'world' : 'World',
                'businessweek-magazine' : 'business',
                'science-energy' : 'science',
                'health' : 'health',
                'leisure' : 'life',
                'world' : 'world',
                'sports' : 'sport',
                'lifestyle' : 'life'
                }
           
               
foxnews_except = { 
              'http://www.foxnews.com///video.foxnews.com/v/2013931500001/fox-news-radio/',
              'http://www.foxnews.com/politics/elections/2014/2014-midterm-elections/'
              }    
           
foxnews_home_pages = {'http://www.foxnews.com/us/index.html' : 'news',
                  FOX_NEWS_HOME : None,
                  'http://www.foxnews.com/politics/index.html' : 'politics',
                  'http://www.foxnews.com/opinion/index.html' : 'opinions',
                  'http://www.foxnews.com/entertainment/index.html' : 'entertainment',
                  'http://www.foxnews.com/tech/index.html' : 'tech',
                  'http://www.foxnews.com/science/index.html' : 'science',
                  'http://www.foxnews.com/health/index.html' : 'health',
                  'http://www.foxnews.com/world/index.html' : 'world',
                  'http://www.foxnews.com/sports/index.html' : 'sport',
                  'http://www.foxnews.com/leisure/index.html' : 'life'
                  }    
               
               
               
               
               
def extract_foxnews_article(article, is_on_homepage, predifined_category=None):
               
    if (article.url in foxnews_except or article.url + '/' in foxnews_except or 'foxnews' not in article.url): 
        return
    if (not hasNumbers(article.url)):
        return
    print("url to extract: " + article.url)
    if (db_connect.is_url_existed(article.url) != -1):
        print("url is already existed")
        url_sharelikecomment_queue.put(article.url, True)
        return
              
    print('\n')
    normalized_url  = article.url.split("?")[0].split("#")[0]
    if ('foxnews' not in normalized_url):
        return
    if (normalized_url in foxnews_except or normalized_url + '/' in foxnews_except):
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
        time_string = html_tree.xpath('//meta[@name="dcterms.created"]')[0].attrib['content']
    except BaseException as dateE:
        print("problem with time: {}".format(dateE))
    try:
        if time_string is None:
            time_string = html_tree.xpath('//time[@itemprop="datePublished"]')[0].attrib['datetime']
    except BaseException as dateE:
        print("problem with time: {}".format(dateE))
    print("extracted time: " + time_string)
    from_zone = tz.gettz('EST')
    date_time = parse(time_string)
    date_time = date_time.replace(tzinfo=from_zone)
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
    article.thumbnail_url = thumbnail_url
    if(thumbnail_url == 'http://global.fncstatic.com/static/v/all/img/fn_128x128.png'):
        article.thumbnail_url = None
                   
                   
               
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
               
    #keywords
    keywords = ""; 
    try:
        keywords = html_tree.xpath('//meta[@name="keywords"]')[0].attrib['content']
        keywords = keywords.lower();
    except Exception as e:
        print("")
     
               
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
                   
    if (category_id is not None and category_id in foxnews_category):
        article.category_id = foxnews_category.get(category_id)
    print(article.category_id)
              
              
               
               
    if (article.published_time is None or article.title is None or article.category_id is None):
        raise Exception("missing fields")
               
               
               
    article.source_name = "FOX NEWS"           
    # get content
    article.parse()
    if (len(keywords) < 2):
        article.nlp()
        for key in article.keywords:
            keywords = keywords + key + ","
        keywords = keywords[0:-1]
    text = normalize_text(article.text)
    text_html = true_html.escape(get_text_html_saulify(normalized_url), True)
    normalized_title = normalize_text_nostop(article.title)
    article.source_id = foxnews_source_id
    
    ''' insert this article to database, maybe send url to another thread to get count, share, .... or maket it asynchronous'''
    # when no exception, we insert to database
    try:
        article.id = db_connect.insert_article3(normalized_url, article.title, foxnews_source_id, 
                                     article.category_id, False, is_on_homepage, article.published_time,
                                     article.thumbnail_url, article.short_description, USA, text_html,
                                     text, normalized_title, keywords)
    except Exception as dbE:
        print("Error when insert article to db. {}".format(dbE))
    # after insert to database, we put this url to get share, comment, like
    url_sharelikecomment_queue.put(normalized_url, True)
    article.url = normalized_url
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
    for home_page in foxnews_home_pages:
        print("extracting: " + home_page)
        page = requests.get(home_page)
        html_tree = html.fromstring(page.text)
        article_urls = html_tree.xpath('//a/@href')
        for home_url in article_urls:
            if  home_url is not None and len(home_url) > 16: 
                if ('http://' not in home_url and 'https://' not in home_url and 'www.foxnews' not in home_url):
                    home_url = FOX_NEWS_HOME + home_url
                try:
                    article_home = Article(home_url, keep_article_html=True)
                    extract_foxnews_article(article_home, True, foxnews_home_pages.get(home_page))
                except Exception as e:
                    print('Smt wrong when process homepage ' + home_page +  ' article:  {}'.format(e) + home_url)
               
               
               
               
               
               
               
               
            
    db_connect.close_database_cont()   
except Exception as e:        
    print('Something went wrong with database: {}'.format(e))    
               
            
           
           
           
          
          
          
'''
=======================================================================================================================================
=======================================================================================================================================
========================================================== FoxNews stop ===============================================================
=======================================================================================================================================
=======================================================================================================================================
''' 
          
          
          
          
          
          
         
         
         
         
         
         
         
         
         
         
         
         
         
'''
=======================================================================================================================================
=======================================================================================================================================
============================================================== ESPN start =============================================================
=======================================================================================================================================
=======================================================================================================================================
''' 
         
espn_category = {'sport' : 'sport'
                }
          
              
espn_except = { 
              'http://www.foxnews.com///video.foxnews.com/v/2013931500001/fox-news-radio/'
              }    
          
espn_home_pages = {'http://www.foxnews.com/us/index.html' : 'sport',
                  ESPN_HOME : None,
                  'http://espn.go.com/nfl' : 'sport',
                  'http://espn.go.com/mlb/' : 'sport',
                  'http://espn.go.com/nba/' : 'sport',
                  'http://espn.go.com/nhl/' : 'sport',
                  'http://espn.go.com/college-football/' : 'sport',
                  'http://espn.go.com/mens-college-basketball/' : 'sport',
                  'http://espn.go.com/racing/nascar/' : 'sport',
                  'http://www.espnfc.us/' : 'sport',
                  'http://espn.go.com/sports/' : 'sport'
                  }    
              
              
              
              
              
def extract_espn_article(article, is_on_homepage, predifined_category=None):
              
    if (article.url in espn_except or article.url + '/' in espn_except or 'espn' not in article.url or '/id/' not in article.url): 
        return
    if (not hasNumbers(article.url)):
        return
    print("url to extract: " + article.url)
    if (db_connect.is_url_existed(article.url) != -1):
        print("url is already existed")
        url_sharelikecomment_queue.put(article.url, True)
        return
             
    print('\n')
    normalized_url  = article.url.split("?")[0].split("#")[0]
    if ('espn' not in normalized_url or len(normalized_url) < 60):
        return
    if (normalized_url in espn_except or normalized_url + '/' in espn_except):
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
    keywords = ""
    published_time = 0
    article.download()
    html_tree = html.fromstring(article.html)
              
    #time
    
    try:
        time_string = html_tree.xpath('//meta[@name="DC.date.issued"]')[0].attrib['content']
        print("extracted time: " + time_string)
        date_time = parse(time_string)
        published_time = calendar.timegm(date_time.utctimetuple())
    except BaseException as dateE:
        print("problem with time: {}".format(dateE))        
    
    try:
        if (published_time == 0):
            article_header_tag = html_tree.xpath('//header[@class="article-header"]')[0]
            time_string = article_header_tag.xpath('//span[@class="timestamp"]/text()')[0] 
            time_string = time_string
            published_time = time.time() - time_from_short_string(time_string)
            print("extracted time: " + time_string)
    except BaseException as dateE:
        print("problem with time: {}".format(dateE))
    
    print("time saved: ")
    print(datetime.fromtimestamp(published_time))
    if (published_time > time.time()):
        published_time = None
    article.published_time = int(published_time)
              
              
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
    article.category_id = 'sport'
    print(article.category_id)
             
             
              
              
    if (article.published_time is None or article.title is None or article.category_id is None):
        raise Exception("missing fields")
              
              
              
    article.source_name = "ESPN"          
    # get content
    article.parse()
    article.nlp()
    for key in article.keywords:
        keywords = keywords + key + ","
    keywords = keywords[0:-1]
    print(keywords)
    text = normalize_text(article.text)
    text_html = true_html.escape(article.article_html, True)
    normalized_title = normalize_text_nostop(article.title)
    article.source_id = espn_source_id
    
    ''' insert this article to database, maybe send url to another thread to get count, share, .... or maket it asynchronous'''
    # when no exception, we insert to database
    try:
        article.id = db_connect.insert_article3(normalized_url, article.title, espn_source_id, 
                                     article.category_id, False, is_on_homepage, article.published_time,
                                     article.thumbnail_url, article.short_description, USA, text_html, 
                                     text, normalized_title, keywords)
    except Exception as dbE:
        print("Error when insert article to db. {}".format(dbE))
    # after insert to database, we put this url to get share, comment, like
    url_sharelikecomment_queue.put(normalized_url, True)
    article.url = normalized_url
    post_queue.put(article, True)
          
          
         
         
         
          
          
print('...................................................\n' +
      '...................................................\n' + 
      '...................................................\n' +
      'start get articles from espn' +
      '...................................................\n' +
      '...................................................\n'
      )
try:
    db_connect = IIIDatbaseConnection()
    db_connect.init_database_cont()     
              
              
              
    ''' we process homepage'''
    for home_page in espn_home_pages:
        print("extracting: " + home_page)
        page = requests.get(home_page)
        html_tree = html.fromstring(page.text)
        article_urls = html_tree.xpath('//a/@href')
        for home_url in article_urls:
            if  home_url is not None and len(home_url) > 16: 
                if ('http://' not in home_url and 'https://' not in home_url and 'espn.go' not in home_url):
                    home_url = ESPN_HOME + home_url
                try:
                    article_home = Article(home_url, keep_article_html=True)
                    extract_espn_article(article_home, True, espn_home_pages.get(home_page))
                except Exception as e:
                    print('Smt wrong when process homepage ' + home_page +  ' article:  {}'.format(e) + home_url)
              
              
              
              
              
              
              
              
           
    db_connect.close_database_cont()   
except Exception as e:        
    print('Something went wrong with database: {}'.format(e))    
              
           
          
          
          
          
         
         
'''
=======================================================================================================================================
=======================================================================================================================================
========================================================== ESPN stop ===============================================================
=======================================================================================================================================
=======================================================================================================================================
''' 
         
         
        
        
        
       
       
       
       
       
       
       
       
       
       
       
      
      
      
      
      
'''
=======================================================================================================================================
=======================================================================================================================================
============================================================== BuzzFeed start =============================================================
=======================================================================================================================================
=======================================================================================================================================
''' 
      
buzzfeed_category = {'community' : 'community',
                 'USNews' : 'news',
                 'Tech' : 'tech',
                 'World' : 'world',
                 'TVAndMovies' : 'entertainment',
                 'Politics' : 'politics',
                 'Music' : 'entertainment',
                 'Celebrity' : 'entertainment',
                 'Culture' : 'entertainment',
                 'Rewind' : 'community',
                 'Parents' : 'life',
                 'Health' : 'health',
                 'DIY' : 'life',    
                 'Food' : 'life',
                 'Travel' : 'travel',
                 'Style' : 'style',
                 'Animals' : 'entertainment',
                 'Business' : 'business',
                 'UK' : 'community',
                 'Science' : 'science',
                 'Australia' : 'community',
                 'Community' : 'community',
                 'Videos' :'community',
                }
       
           
buzzfeed_except = { 
              'http://www.buzzfeed.com/tools/email/politics',
              'http://www.buzzfeed.com/tag/state_department',
              'http://www.buzzfeed.com/tag/social_security_administration',
              'http://www.buzzfeed.com/tag/2016_election',
              'http://www.buzzfeed.com/tag/twitter_parodies',
              }    
       
buzzfeed_home_pages = {'http://www.buzzfeed.com/community' : 'community',
                  BUZZFEED_HOME : None,
                  'http://www.buzzfeed.com/politics' : 'politics',
                  'http://www.buzzfeed.com/travel' : 'travel',
                  'http://www.buzzfeed.com/health' : 'health',
                  'http://www.buzzfeed.com/business' : 'business',
                  'http://www.buzzfeed.com/science' : 'science',
                  'http://www.buzzfeed.com/celebrity' : 'entertainment',
                  'http://www.buzzfeed.com/entertainment' : 'entertainment',
                  'http://www.buzzfeed.com/tech' : 'tech',
                  'http://www.buzzfeed.com/life' : 'life',
                  'http://www.buzzfeed.com/parents' : 'life',
                  'http://www.buzzfeed.com/politics' : 'politics'
                  }    
           
           
           
           
           
def extract_buzzfeed_article(article, is_on_homepage, predifined_category=None):
           
    if (article.url in buzzfeed_except or article.url + '/' in buzzfeed_except or 'buzzfeed' not in article.url): 
        return
    if (not hasNumbers(article.url)):
        return
    print("url to extract: " + article.url)
    if (db_connect.is_url_existed(article.url) != -1):
        print("url is already existed")
        url_sharelikecomment_queue.put(article.url, True)
        return
          
    print('\n')
    normalized_url  = article.url.split("?")[0].split("#")[0]
    if ('buzzfeed' not in normalized_url or len(normalized_url) < 50):
        return
    if (normalized_url in buzzfeed_except or normalized_url + '/' in buzzfeed_except):
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
        time_span_tag = html_tree.xpath('//span[@class="buzz_datetime converted_buzz_datetime"]')[0]
        time_script_tag= time_span_tag.xpath('//script[@type="text/javascript"]')[0]
        result_regex = re.search(r"formatted_date\(([A-Za-z0-9_\./\\-]*)\);", time_span_tag.text_content())
        time_string = result_regex.group(1)
        print("extracted_time: " + time_string)
        #time_string = time_string + " UTC-0400"
    except BaseException as dateE:
        print("problem with time: {}".format(dateE))
    try:
        if (time_string is None):
            time_span_tag = html_tree.xpath('//span[@class="buzz-datetime converted_buzz_datetime"]')[0]
            time_script_tag= time_span_tag.xpath('//script[@type="text/javascript"]')[0]
            result_regex = re.search(r"formatted_date\(([A-Za-z0-9_\./\\-]*)\);", time_span_tag.text_content())
            time_string = result_regex.group(1)
            print("extracted_time: " + time_string)
            #time_string = time_string + " UTC-0400"
    except BaseException as dateE:
        print("problem with time: {}".format(dateE))
    article.published_time = long(time_string)
    print(article.published_time)
           
           
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
    print(title)
    article.title = title
           
           
           
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
    article.thumbnail_url = thumbnail_url
               
    
    #keywords
    try:
        article.keywords = ""; 
        keywords = html_tree.xpath('//meta[@name="keywords"]')[0].attrib['content']
        article.keywords = keywords.lower();
    except Exception as e:
        print("")          
           
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
    except Exception as e:
        print('Category not found'.format(e))
              
    try:
        if category_id is None:
            category_id = html_tree.xpath('//meta[@name="category"]')[0].attrib['content']
    except Exception as e:
        print('Category not found again'.format(e))
    print(category_id)
    if(category_id is not None and category_id  in buzzfeed_category):
        article.category_id = buzzfeed_category.get(category_id)
           
           
    if (article.published_time is None or article.title is None or article.category_id is None):
        raise Exception("missing fields")
           
           
           
    article.source_name = "BUZZFEED"        
    # get content
    article.parse()
    text = normalize_text(article.text)
    #extractor = buzzFeedContentExtractor()
    #extractor.parse(html.fromstring(article.html), title, unix_time_to_string(article.published_time), normalized_url)
    text_html = true_html.escape(article.article_html, True)
    normalized_title = normalize_text_nostop(article.title)
    article.source_id = buzzfeed_source_id
    
    ''' insert this article to database, maybe send url to another thread to get count, share, .... or maket it asynchronous'''
    # when no exception, we insert to database
    try:
        article.id = db_connect.insert_article3(normalized_url, article.title, buzzfeed_source_id, 
                                     article.category_id, False, is_on_homepage, article.published_time,
                                     article.thumbnail_url, article.short_description, USA, text_html, 
                                     text, normalized_title, article.keywords)
    except Exception as dbE:
        print("Error when insert article to db. {}".format(dbE))
    # after insert to database, we put this url to get share, comment, like
    url_sharelikecomment_queue.put(normalized_url, True)
    article.url = normalized_url
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
    for home_page in buzzfeed_home_pages:
        print("extracting: " + home_page)
        page = requests.get(home_page)
        html_tree = html.fromstring(page.text)
        article_urls = html_tree.xpath('//a/@href')
        for home_url in article_urls:
            if  home_url is not None and len(home_url) > 16: 
                if ('http://' not in home_url and 'https://' not in home_url and 'buzzfeed.com' not in home_url):
                    home_url = BUZZFEED_HOME + home_url
                try:
                    article_home = Article(home_url, keep_article_html=True)
                    extract_buzzfeed_article(article_home, True, buzzfeed_home_pages.get(home_page))
                except Exception as e:
                    print('Smt wrong when process homepage ' + home_page +  ' article:  {}'.format(e) + home_url)
           
           
           
           
           
           
           
           
        
    db_connect.close_database_cont()   
except Exception as e:        
    print('Something went wrong with database: {}'.format(e))    
           
        
       
      
      
      
      
      
'''
=======================================================================================================================================
=======================================================================================================================================
========================================================== buzzfeed.com stop ===============================================================
=======================================================================================================================================
=======================================================================================================================================
''' 
     
     
    
    
    
  
 
 

   
   
  
  
  
  
  
  
  
  
         
'''
=======================================================================================================================================
=======================================================================================================================================
================================================= Business Insider start ===============================================================
=======================================================================================================================================
=======================================================================================================================================
''' 
         
             
             
business_insider_except = {
                     
                }
         
             
business_insider_category = {'sai' : 'tech', 
                   'social-media' : 'tech',
                   'science' : 'science', 
                   'politics' : 'politics', 
                   'warroom' : 'business',
                   'careers-contributor' : 'business',
                   'clusterstock-contributor' : 'business',
                   'retail' : 'business',
                   'travel-contributor' : 'travel',
                   'world' : 'world', 
                   'entertainment' : 'entertainment',
                   'clusterstock' : 'business',
                   'sportspage' : 'sport',
                   'thelife' : 'life',
                   'thelife-contributor' : 'life', 
                   'sportspage-contributor' : 'health',
                    'science-contributor' : 'science',
                    'sai-contributor' : 'tech',
                    'travel' : 'travel',
                    'yourmoney' : 'business',
                    'defense' : 'world',
                    'education' : 'education',
                    'transportation-contributor' : 'sport',
                    'moneygame' : 'business',
                    'enterprise' : 'business',
                    'transportation' : 'sport',
                   }    
         
business_insider_home_pages = {
                     'http://www.businessinsider.com/sai' : 'tech',
                     'http://www.businessinsider.com/clusterstock' : 'business',
                     'http://www.businessinsider.com/politics' : 'politics',
                     'http://www.businessinsider.com/thelife' : 'life'      ,
                     'http://www.businessinsider.com/warroom' : 'business', 
                     'http://www.businessinsider.com/sportspage' : 'sport',
                     'http://www.businessinsider.com/video' : None,
                     'http://www.businessinsider.com' : None
                }    
             
             
             
             
             
def extract_business_insider_article(article, is_on_homepage, predifined_category=None):
             
    if ('201' not in article.url or 'businessinsider.com' not in article.url): 
        return
    
    print('\n')
    print("url to extract: " + article.url)
    if (db_connect.is_url_existed(article.url) != -1):
        print("url is already existed")
        url_sharelikecomment_queue.put(article.url, True)
        return
    
    normalized_url  = normalize_url(article.url)
    if ('201' not in article.url or 'businessinsider.com' not in normalized_url):
        return
    if (normalized_url in business_insider_except or normalized_url + '/' in business_insider_except):
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
              
             
    #get time and category   
    try:
        data_json = html_tree.xpath('//script[@type="application/ld+json"]')[0]
        #print(data_json.text)
        result = re.search("\/\/<!\[CDATA\[((.|\n)*)\/\/\]\]>", data_json.text)
        data_json = json.loads(result.group(1))
        print(data_json['dateCreated'])
        time_string = data_json['dateCreated']
        category_id = data_json['articleSection']
        print(category_id)
        article.category_id = business_insider_category.get(category_id)
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
        thumbnail_url = html_tree.xpath('//meta[@property="twitter:image"]')[0].attrib['content']
        print(thumbnail_url)
    except Exception as e:
        print('Thumbnaill not found.'.format(e))
    try:
        if(thumbnail_url is None):
            thumbnail_url = html_tree.xpath('//meta[@name="tbi-image"]')[0].attrib['content']
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
             
    
    #keywords
    try:
        article.keywords = ""; 
        keywords = html_tree.xpath('//meta[@name="keywords"]')[0].attrib['content']
        article.keywords = keywords.lower();
    except Exception as e:
        print("")
       
             
             
    if (article.published_time is None or article.title is None or article.category_id is None):
        raise Exception("missing fields")
             
             
             
    article.source_name = "BUSINESS INSIDER"           
    # get content
    article.parse()
    text = normalize_text(article.text)
    text_html = true_html.escape(article.article_html, True)
    normalized_title = normalize_text_nostop(article.title)
    article.source_id = business_insider_id
    
    ''' insert this article to database, maybe send url to another thread to get count, share, .... or maket it asynchronous'''
    # when no exception, we insert to database
    try:
        article.id = db_connect.insert_article3(normalized_url, article.title, business_insider_id, 
                                     article.category_id, False, is_on_homepage, article.published_time,
                                     article.thumbnail_url, article.short_description, USA, 
                                     text_html, text, normalized_title, article.keywords)
    except Exception as dbE:
        print("Error when insert article to db. {}".format(dbE))
    # after insert to database, we put this url to get share, comment, like
    url_sharelikecomment_queue.put(normalized_url, True)
    article.url = normalized_url
    post_queue.put(article, True)
         
         
         
         
             
             
             
             
             
             
             
             
             
             
             
             
             
             
          
print('...................................................\n' +
      '...................................................\n' + 
      '...................................................\n' +
      'start get articles from Business Insider' +
      '...................................................\n' +
      '...................................................\n'
      )
try:
    db_connect = IIIDatbaseConnection()
    db_connect.init_database_cont()     
             
             
             
    ''' we process homepage'''
    for home_page in business_insider_home_pages:
        print("extracting: " + home_page)
        business_page = requests.get(home_page)
        html_tree = html.fromstring(business_page.text)
        article_urls = html_tree.xpath('//a/@href')
        for home_url in article_urls:
            if  home_url is not None and len(home_url) > 16: 
                if ('http://' not in home_url and 'https://' not in home_url):
                    home_url = BUSINESS_INSIDER + home_url
                try:
                    article_home = Article(home_url, keep_article_html=True)
                    extract_business_insider_article(article_home, True, business_insider_home_pages.get(home_page))
                except Exception as e:
                    print('Smt wrong when process homepage' + home_page +  'article:  {}'.format(e) + " " +home_url)
             
             
             
             
             
             
             
             
          
    db_connect.close_database_cont()   
except Exception as e:        
    print('Something went wrong with database: {}'.format(e))    
             
             
         
'''
=======================================================================================================================================
=======================================================================================================================================
================================================= BusinessInsider news stop ===============================================================
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
