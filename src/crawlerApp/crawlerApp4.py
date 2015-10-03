'''
Created on Mar 15, 2015

@author: hoavu
'''

from apt.progress.text import long
import calendar
from datetime import datetime
from dateutil.parser import parse
from dateutil.tz import tzlocal
import json
from lxml import html
from newspaper.article import Article
import os.path
import queue
import requests
import sys
import time
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from crawlerApp.PostAndGetFromFbPages import CommentLikeShrareGetterThread, \
    POISON, PostToFacebookPage
from crawlerApp.utils import normalize_url, get_text_html_saulify, \
    normalize_text, hasNumbers, normalize_text_nostop
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
HUFFINGTON_POST_HOME = 'http://www.huffingtonpost.com/'
NBC_HOMEPAGE = 'http://www.nbcnews.com/'
ABC_HOMEPAGE = 'http://abcnews.go.com'
LA_TIMES_HOMEPAGE = 'http://www.latimes.com'
NEWYORKTIME_HOME = "http://www.nytimes.com"
WASHINGTON_POST = 'http://www.washingtonpost.com/'
CBS_NEWS_HOME = 'http://www.cbsnews.com'
BLOOMBERG_HOME_PAGE = 'http://www.bloomberg.com'
FOX_NEWS_HOME = 'http://www.foxnews.com/'
ESPN_HOME = 'http://espn.go.com/'
BUZZFEED_HOME = 'http://www.buzzfeed.com/'
FORBES_HOME = 'http://www.forbes.com'
PEOPLE_HOME = 'http://www.people.com'
VOGUE_HOME = 'http://www.vogue.com/?us_site=y'
EVERYDAY_HEATH_HOME = 'http://www.everydayhealth.com'
EONLINE_HOME = 'http://www.eonline.com'
TECHCRUNCH_HOME = 'http://techcrunch.com'
BLEACH_REPORT = 'http://bleacherreport.com'
THEBLAZE_HOME = "http://www.theblaze.com"
REUTERS_HOME = "http://www.reuters.com"
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
theblaze_source_id = 'theblaze'
reuters_source_id = "reuters"
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
page_poster_thread = PostToFacebookPage(queue=post_queue)
page_poster_thread.start()
'''
============================================================================================
'''  






 
 
 
 
 
 
 
 
 
 
 
  
  
  
    
  
  
  
  
  
  
  
   
   
   
   
   
   
'''
=======================================================================================================================================
=======================================================================================================================================
============================================================ EverydayHeath start ======================================================
=======================================================================================================================================
=======================================================================================================================================
''' 
     
everydayheathy_category = {
                              
                }
      
          
everydayheathy_except = { 
                'http://www.everydayhealth.com/drugs/all-drugs/', 'http://www.everydayhealth.com/cancer/index.aspx',
                'http://www.everydayhealth.com/diet-nutrition/vitamins-meds.aspx',
                'http://www.everydayhealth.com/pain-management/headache/index.aspx',
                'http://www.everydayhealth.com/health-center/common-topics.aspx',
                'http://www.everydayhealth.com/vision-center/allarticles.aspx', 'http://www.everydayhealth.com/columns/recipe-of-the-day/',
                'http://www.everydayhealth.com/diet-nutrition/allarticles.aspx',
                'http://www.everydayhealth.com/dental-health/101.aspx',
                'http://www.everydayhealth.com/atrial-fibrillation/',
                'http://www.everydayhealth.com/multiple-sclerosis/', 'http://www.everydayhealth.com/members/account/profile2.aspx',
                'http://www.everydayhealth.com/newsletter-subscriptions/signup/'
                'http://www.everydayhealth.com/newsletter-subscriptions/',
                'http://www.everydayhealth.com/alternative-health/the-basics.aspx',
                'http://www.everydayhealth.com/lifestyle/healthy-food-finds/'
              }    
      
everydayheathy_home_pages = {EVERYDAY_HEATH_HOME, 'http://www.everydayhealth.com/lifestyle/healthy-living/',
                             'http://www.everydayhealth.com/lifestyle/food/', 'http://www.everydayhealth.com/lifestyle/kidshealth/',
                             'http://www.everydayhealth.com/lifestyle/beauty/', 'http://www.everydayhealth.com/fitness/',
                             "http://www.everydayhealth.com/conditions/mens-health", "http://www.everydayhealth.com/conditions/sexual-health",
                             'http://www.everydayhealth.com/lifestyle/healthy-recipes/',
                        
                  }    
          
          
          
          
          
def extract_everydayheathy_article(article, is_on_homepage, predifined_category=None):
          
    if (article.url in everydayheathy_except or article.url + '/' in everydayheathy_except or 'everydayhealth' not in article.url or article.url in everydayheathy_home_pages): 
        return
    if('ttp://www.facebook.com' in article.url or 'https://twitter.com' in article.url or '/conditions/' in article.url or 'ools.everydayhealth.c' in article.url):
        return
    print('\n\n')
    print("url to extract: " + article.url)
    if (db_connect.is_url_existed(article.url) != -1):
        print("url is already existed")
        url_sharelikecomment_queue.put(article.url, True)
        return
         
    print('\n')
    normalized_url  = article.url.split("?")[0].split("#")[0];
    if ('everydayhealth' not in normalized_url or len(normalized_url) < 45):
        return
    if (normalized_url in everydayheathy_except or normalized_url + '/' in everydayheathy_except):
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
    article.download()
    html_tree = html.fromstring(article.html)
           
          
    #time 
    try:
        time_string = html_tree.xpath('//p[@class="date"]/text()')[0]
        time_string = time_string.replace("Published", "") + " 00:00 " + datetime.now(tzlocal()).tzname()
        print("extracted time: " + time_string)
        #time_string = time_string + " UTC-0400"
    except BaseException as dateE:
        print("problem with time: {}".format(dateE))
       
    try:
        time_string = html_tree.xpath('//meta[@itemprop="datePublished"]')[0].attrib['content']
        time_string = time_string + "-04:00"
        print("extracted time: " + time_string)
        #time_string = time_string + " UTC-0400"
    except BaseException as dateE:
        print("problem with time: {}".format(dateE))
       
    try:
        if (time_string is None):
            time_string = html_tree.xpath('//meta[@itemprop="dateModified"]')[0].attrib['content']
    except BaseException as dateE:
        print("problems with time {}".format(dateE))
    try:
        if (time_string is None):
            time_string = html_tree.xpath('//meta[@name="datemodified"]')[0].attrib['content']
            time_string = time_string + "-04:00"
    except BaseException as dateE:
        print("problems with time {}".format(dateE))
       
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
            thumbnail_url = html_tree.xpath('//meta[@name="twitter:image"]')[0].attrib['content']
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
    article.category_id = 'health'
         
         
          
    if (article.published_time is None or article.title is None or article.thumbnail_url is None):
        raise Exception("missing fields")
          
          
          
    article.source_name = "everydayhealth.com"       
    # get content
    article.parse()
    text = normalize_text(article.text)
    text_html = true_html.escape(article.article_html, True)
    normalized_title = normalize_text_nostop(article.title)
    article.source_id = everydayhealth_source_id
     
    ''' insert this article to database, maybe send url to another thread to get count, share, .... or maket it asynchronous'''
    # when no exception, we insert to database
    try:
        article.id = db_connect.insert_article3(normalized_url, article.title, everydayhealth_source_id, 
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
    for home_page in everydayheathy_home_pages:
        print("extracting: " + home_page)
        page = requests.get(home_page)
        html_tree = html.fromstring(page.text)
        article_urls = html_tree.xpath('//a/@href')
        for home_url in article_urls:
            if  home_url is not None and len(home_url) > 16: 
                if ('http://' not in home_url and 'https://' not in home_url):
                    home_url = EVERYDAY_HEATH_HOME + home_url
                try:
                    article_home = Article(home_url, keep_article_html=True)
                    extract_everydayheathy_article(article_home, True, None)
                except Exception as e:
                    print('Smt wrong when process homepage ' + home_page +  ' article:  {}'.format(e) + home_url)
         
         
         
         
         
         
         
         
      
    db_connect.close_database_cont()   
except Exception as e:        
    print('Something went wrong with database: {}'.format(e))    
         
      
     
     
     
'''
=======================================================================================================================================
=======================================================================================================================================
========================================================== everydayhealth stop ==============================================================
=======================================================================================================================================
=======================================================================================================================================
''' 
     
   
   
   
   
   
   
   
   
   
   
   
   
   
   
'''
=======================================================================================================================================
=======================================================================================================================================
============================================================= EOnline start ===========================================================
=======================================================================================================================================
=======================================================================================================================================
''' 
     
eonline_category = {
                              
                }
      
          
eonline_except = { 
                   
              }    
      
eonline_home_pages = { 'http://www.eonline.com/news'
                        
                  }    
          
          
          
          
          
def extract_eonline_article(article, is_on_homepage, predifined_category=None):
          
    if (article.url in eonline_except or article.url + '/' in eonline_except or 'eonline.com' not in article.url or article.url in eonline_home_pages): 
        return
    if('ttp://www.facebook.com' in article.url or 'https://twitter.com' in article.url):
        return
    print('\n\n')
    print("url to extract: " + article.url)
    if (db_connect.is_url_existed(article.url) != -1):
        print("url is already existed")
        url_sharelikecomment_queue.put(article.url, True)
        return
         
    print('\n')
    normalized_url  = article.url.split("?")[0].split("#")[0];
    if ('eonline.com' not in normalized_url or len(normalized_url) < 60):
        return
    if (normalized_url in eonline_except or normalized_url + '/' in eonline_except):
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
    article.download()
    html_tree = html.fromstring(article.html)
           
          
    #time 
    try:
        time_string = html_tree.xpath('//meta[@name="sailthru.date"]')[0].attrib['content']
        time_string = time_string + " -7:00"
        print("extracted time: " + time_string)
        #time_string = time_string + " UTC-0400"
    except BaseException as dateE:
        print("problem with time: {}".format(dateE))
    try:
        if (time_string is None):
            time_string = html_tree.xpath('//time')[0].attrib['datetime']
            #time_string = time_string + " -4:00"
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
        thumbnail_url = html_tree.xpath('//meta[@name="twitter:image"]')[0].attrib['content']
        print(thumbnail_url)
    except Exception as e:
        print('Thumbnaill not found. {}'.format(e))
    try:
        if(thumbnail_url is None):
            thumbnail_url = html_tree.xpath('//meta[@property="og:image"]')[0].attrib['content']
            print(thumbnail_url)
    except Exception as e:
        print('Thumbnaill not found.'.format(e))
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
    article.category_id = 'entertainment'
         
         
          
    if (article.published_time is None or article.title is None or article.thumbnail_url is None):
        raise Exception("missing fields")
          
          
          
    article.source_name = "EONLINE.COM"        
    # get content
    article.parse()
    text = normalize_text(article.text)
    text_html = true_html.escape(article.article_html, True)
    normalized_title = normalize_text_nostop(article.title) 
    article.source_id = eonline_source_id
     
    ''' insert this article to database, maybe send url to another thread to get count, share, .... or maket it asynchronous'''
    # when no exception, we insert to database
    try:
        article.id = db_connect.insert_article3(normalized_url, article.title, eonline_source_id, 
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
    for home_page in eonline_home_pages:
        print("extracting: " + home_page)
        page = requests.get(home_page)
        html_tree = html.fromstring(page.text)
        article_urls = html_tree.xpath('//a/@href')
        for home_url in article_urls:
            if  home_url is not None and len(home_url) > 16: 
                if ('http://' not in home_url and 'https://' not in home_url):
                    home_url = EONLINE_HOME + home_url
                try:
                    article_home = Article(home_url, keep_article_html=True)
                    extract_eonline_article(article_home, True, None)
                except Exception as e:
                    print('Smt wrong when process homepage ' + home_page +  ' article:  {}'.format(e) + home_url)
         
         
         
         
         
         
         
         
      
    db_connect.close_database_cont()   
except Exception as e:        
    print('Something went wrong with database: {}'.format(e))    
         
      
     
     
     
'''
=======================================================================================================================================
=======================================================================================================================================
========================================================== EOnline stop ==============================================================
=======================================================================================================================================
=======================================================================================================================================
''' 
     
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
'''
=======================================================================================================================================
=======================================================================================================================================
============================================================= Techcrunch start ===========================================================
=======================================================================================================================================
=======================================================================================================================================
''' 
     
techcrunch_category = {
                              
                }
      
          
techcrunch_except = { 
                   
              }    
      
techcrunch_home_pages = { 'http://techcrunch.com/', 'http://techcrunch.com/startups/',
                         'http://techcrunch.com/mobile/', 'http://techcrunch.com/gadgets/',
                         'http://techcrunch.com/enterprise/', 'http://techcrunch.com/social/',
                         'http://techcrunch.com/europe/'
                        
                  }    
          
          
          
          
          
def extract_techcrunch_article(article, is_on_homepage, predifined_category=None):
          
    if ('201' not in article.url or article.url in techcrunch_except or article.url + '/' in techcrunch_except or 'techcrunch.com/' not in article.url or article.url in techcrunch_home_pages): 
        return
    if('ttp://www.facebook.com' in article.url or 'https://twitter.com' in article.url):
        return
    print('\n\n')
    print("url to extract: " + article.url)
    if (db_connect.is_url_existed(article.url) != -1):
        print("url is already existed")
        url_sharelikecomment_queue.put(article.url, True)
        return
         
    print('\n')
    normalized_url  = article.url.split("?")[0].split("#")[0];
    if ('techcrunch.com/' not in normalized_url or len(normalized_url) < 45):
        return
    if (normalized_url in techcrunch_except or normalized_url + '/' in techcrunch_except):
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
    article.download()
    html_tree = html.fromstring(article.html)
           
          
    #time 
    try:
        time_string = html_tree.xpath('//meta[@name="sailthru.date"]')[0].attrib['content']
        time_string = time_string + " -7:00"
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
        print('Thumbnaill not found. {}'.format(e))
    try:
        if(thumbnail_url is None):
            thumbnail_url = html_tree.xpath("//meta[@name='twitter:image:src']")[0].attrib['content']
            print(thumbnail_url)
    except Exception as e:
        print('Thumbnaill not found.'.format(e))
    try:
        if(thumbnail_url is None):
            thumbnail_url = html_tree.xpath("//meta[@name='sailthru.image.full']")[0].attrib['content']
            print(thumbnail_url)
    except Exception as e:
        print('Thumbnaill not found.'.format(e))
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
    article.category_id = 'tech'
         
         
          
    if (article.published_time is None or article.title is None or article.thumbnail_url is None):
        raise Exception("missing fields")
          
          
          
    article.source_name = "TECHCRUNCH"     
    # get content
    article.parse()
    text = normalize_text(article.text)
    text_html = true_html.escape(article.article_html, True)
    normalized_title = normalize_text_nostop(article.title)
    article.source_id = techcrunch_source_id
     
    ''' insert this article to database, maybe send url to another thread to get count, share, .... or maket it asynchronous'''
    # when no exception, we insert to database
    try:
        article.id = db_connect.insert_article3(normalized_url, article.title, techcrunch_source_id, 
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
    for home_page in techcrunch_home_pages:
        print("extracting: " + home_page)
        page = requests.get(home_page)
        html_tree = html.fromstring(page.text)
        article_urls = html_tree.xpath('//a/@href')
        for home_url in article_urls:
            if  home_url is not None and len(home_url) > 16: 
                if ('http://' not in home_url and 'https://' not in home_url):
                    home_url = TECHCRUNCH_HOME + home_url
                try:
                    article_home = Article(home_url, keep_article_html=True)
                    extract_techcrunch_article(article_home, True, None)
                except Exception as e:
                    print('Smt wrong when process homepage ' + home_page +  ' article:  {}'.format(e) + home_url)
         
         
         
         
         
         
         
         
      
    db_connect.close_database_cont()   
except Exception as e:        
    print('Something went wrong with database: {}'.format(e))    
         
      
     
     
     
'''
=======================================================================================================================================
=======================================================================================================================================
========================================================== Techcrunch stop ==============================================================
=======================================================================================================================================
=======================================================================================================================================
''' 
     
   
   
   
   
   
   
   
  
  
  
  
  
  
  
  
  
  
  
'''
=======================================================================================================================================
=======================================================================================================================================
========================================================== BleacherReport start =======================================================
=======================================================================================================================================
=======================================================================================================================================
''' 
    
bleacher_category = {
                             
                }
     
         
bleacher_except = { 
                  
              }    
     
bleacher_home_pages = { 'http://bleacherreport.com/',
                     'http://bleacherreport.com/nfl',
                     'http://bleacherreport.com/college-basketball',
                     'http://bleacherreport.com/nba',
                     'http://bleacherreport.com/college-football',
                     'http://bleacherreport.com/mlb',
                     'http://bleacherreport.com/world-football',
                     'http://bleacherreport.com/ufc',
                     'http://bleacherreport.com/wwe',
                     'http://bleacherreport.com/golf',
                     'http://bleacherreport.com/nascar',
                       
                  }    
         
         
         
         
         
def extract_bleacher_article(article, is_on_homepage, predifined_category=None):
         
    if (article.url in bleacher_except or article.url + '/' in bleacher_except or 'bleacherreport' not in article.url or article.url in bleacher_home_pages): 
        return
    if('ttp://www.facebook.com' in article.url or 'https://twitter.com' in article.url):
        return
    if (not hasNumbers(article.url)):
        return
    print('\n\n')
    print("url to extract: " + article.url)
    if (db_connect.is_url_existed(article.url) != -1):
        print("url is already existed")
        url_sharelikecomment_queue.put(article.url, True)
        return
        
    print('\n')
    normalized_url  = article.url.split("?")[0].split("#")[0];
    if ('bleacherreport' not in normalized_url or len(normalized_url) < 45):
        return
    if (normalized_url in bleacher_except or normalized_url + '/' in bleacher_except):
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
    article.download()
    html_tree = html.fromstring(article.html)
          
         
    #time 
    try:
        time_string = html_tree.xpath('//meta[@name="pubdate"]')[0].attrib['content']
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
        title = html_tree.xpath('//h1[@class="article_title"]/text()')[0]
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
        print('Thumbnaill not found. {}'.format(e))
    try:
        if(thumbnail_url is None):
            thumbnail_url = html_tree.xpath("//meta[@name='twitter:image']")[0].attrib['content']
            print(thumbnail_url)
    except Exception as e:
        print('Thumbnaill not found.'.format(e))
    try:
        if(thumbnail_url is None):
            thumbnail_url = html_tree.xpath("//meta[@name='sailthru.image.full']")[0].attrib['content']
            print(thumbnail_url)
    except Exception as e:
        print('Thumbnaill not found.'.format(e))
    article.thumbnail_url = thumbnail_url
             
             
         
    # get description
    try:
        short_description = html_tree.xpath('//meta[@property="og:description"]')[0].attrib['content']
        print(short_description)
    except Exception as e:
        print('Description not found'.format(e))    
    try:
        if(short_description is None):
            short_description = html_tree.xpath('//meta[@"twitter:description"]')[0].attrib['content']
            print(short_description)
    except Exception as e:
        print('Description not found again'.format(e))
    article.short_description = short_description
         
         
    # get category
    article.category_id = 'sport'
        
        
         
    if (article.published_time is None or article.title is None or article.thumbnail_url is None):
        raise Exception("missing fields")
         
         
         
    article.source_name = "BLEACHER REPORT"    
    # get content
    article.parse()
    text = normalize_text(article.text)
    text_html = true_html.escape(article.article_html, True)
    normalized_title = normalize_text_nostop(article.title)
    article.source_id = bleachreport_source_id
      
    ''' insert this article to database, maybe send url to another thread to get count, share, .... or maket it asynchronous'''
    # when no exception, we insert to database
    try:
        article.id = db_connect.insert_article3(normalized_url, article.title, bleachreport_source_id, 
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
    for home_page in bleacher_home_pages:
        print("extracting: " + home_page)
        page = requests.get(home_page)
        html_tree = html.fromstring(page.text)
        article_urls = html_tree.xpath('//a/@href')
        for home_url in article_urls:
            if  home_url is not None and len(home_url) > 50: 
                if ('http://' not in home_url and 'https://' not in home_url):
                    home_url = BLEACH_REPORT + home_url
                try:
                    article_home = Article(home_url, keep_article_html=True)
                    extract_bleacher_article(article_home, True, None)
                except Exception as e:
                    print('Smt wrong when process homepage ' + home_page +  ' article:  {}'.format(e) + home_url)
        
        
        
        
        
        
        
        
     
    db_connect.close_database_cont()   
except Exception as e:        
    print('Something went wrong with database: {}'.format(e))    
        
     
    
    
    
'''
=======================================================================================================================================
=======================================================================================================================================
======================================================== Bleacher Report stop =========================================================
=======================================================================================================================================
=======================================================================================================================================
''' 
    
  
  
  
  
  
  
  
   
    
'''
=======================================================================================================================================
=======================================================================================================================================
============================================================= Vogue start ============================================================
=======================================================================================================================================
=======================================================================================================================================
''' 
      
vogue_category = {
                
                }
       
           
vogue_except = { 
                    
              }    
       
vogue_home_pages = {'http://www.vogue.com/fashion/',
                     'http://www.vogue.com/beauty/',
                     'http://www.vogue.com/?us_site=y'
                         
                  }    
           
           
           
           
           
def extract_vogue_article(article, is_on_homepage, predifined_category=None):
           
    if (article.url in vogue_except or article.url + '/' in vogue_except or 'vogue.com' not in article.url or article.url in vogue_home_pages): 
        return
    if('ttp://www.facebook.com' in article.url or 'https://twitter.com/intent/' in article.url):
        return
    if(not hasNumbers(article.url)):
        return 
    print('\n\n')
    print("url to extract: " + article.url)
    if (db_connect.is_url_existed(article.url) != -1):
        print("url is already existed")
        url_sharelikecomment_queue.put(article.url, True)
        return
          
    print('\n')
    normalized_url  = article.url.split("?")[0].split("#")[0];
    if ('vogue.com' not in normalized_url or len(normalized_url) < 45):
        return
    if (normalized_url in vogue_except or normalized_url + '/' in vogue_except):
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
        time_string = html_tree.xpath('//time')[0].attrib['datetime']
        #time_string = time_string + " -4:00"
        print("extracted time: " + time_string)
        #time_string = time_string + " UTC-0400"
    except BaseException as dateE:
        print("problem with time: {}".format(dateE))
    try:
        if (time_string is None):
            time_string = html_tree.xpath('//time[@class="article-content-meta--date"]')[0].attrib['datetime']
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
        page_data = html_tree.xpath("//meta[@name='parsely-page']")[0].attrib['content']
        jdata = json.loads(page_data)
        thumbnail_url = jdata['image_url']
        print(thumbnail_url)
    except Exception as e:
        print('Thumbnaill not found. {}'.format(e))
    try:
        if(thumbnail_url is None):
            thumbnail_url = html_tree.xpath('//meta[@name="twitter:image:src"]')[0].attrib['content']
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
    article.category_id = 'style'
          
          
           
    if (article.published_time is None or article.title is None or article.thumbnail_url is None):
        raise Exception("missing fields")
           
           
           
    article.source_name = "VOGUE"      
    # get content
    article.parse()
    text = normalize_text(article.text)
    text_html = true_html.escape(article.article_html, True)
    normalized_title = normalize_text_nostop(article.title)
    article.source_id = vogue_source_id
         
    ''' insert this article to database, maybe send url to another thread to get count, share, .... or maket it asynchronous'''
    # when no exception, we insert to database
    try:
        article.id = db_connect.insert_article3(normalized_url, article.title, vogue_source_id, 
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
    for home_page in vogue_home_pages:
        print("extracting: " + home_page)
        page = requests.get(home_page)
        html_tree = html.fromstring(page.text)
        article_urls = html_tree.xpath('//a/@href')
        for home_url in article_urls:
            if  home_url is not None and len(home_url) > 16: 
                if ('http://' not in home_url and 'https://' not in home_url):
                    home_url = 'http://www.vogue.com' + home_url
                try:
                    article_home = Article(home_url, keep_article_html=True)
                    extract_vogue_article(article_home, True, None)
                except Exception as e:
                    print('Smt wrong when process homepage ' + home_page +  ' article:  {}'.format(e) + home_url)
          
          
          
          
          
          
          
          
       
    db_connect.close_database_cont()   
except Exception as e:        
    print('Something went wrong with database: {}'.format(e))    
          
       
      
      
      
'''
=======================================================================================================================================
=======================================================================================================================================
========================================================== vogue stop ==============================================================
=======================================================================================================================================
=======================================================================================================================================
''' 
      
    
    
  
  
  
  
  
  
  
  
  
  
  
  
  
      
       
       
       
       
       
       
       
       
'''
=======================================================================================================================================
=======================================================================================================================================
============================================================= CBSNews start ===========================================================
=======================================================================================================================================
=======================================================================================================================================
''' 
       
cbs_category = {'World' : 'world',
                'Sports' : 'sport',
                'U.S.' : 'news',
                'Entertainment' : 'entertainment',
                'MoneyWatch Tech' : 'tech',
                'SciTech' : 'tech',
                'Politics' : 'politics',
                'Money' : 'business',
                'Work' : 'business',
                'Markets' : 'business',
                'Trending' : 'news',
                'Retirement' : 'life',
                'MoneyWatch Small Business' : 'business',
                'Crimesider' : 'news',
                'Health' : 'health',
                'CBS Evening News': 'news'
                }
        
            
cbs_except = { 'http://www.cbsnews.com/cbs-this-morning/', 'http://www.cbsnews.com/face-the-nation/',
              'http://cbsn.cbsnews.com/?ftag=CNMdaef904','http://cbsn.cbsnews.com/' ,
              'http://www.cbsnews.com/politics/battleground/', 'http://www.cbsnews.com/politics/white-house/',
              'http://www.cbsnews.com/60-minutes/overtime/', 'http://www.cbsnews.com/face-the-nation/face-to-face/',
              'http://www.cbsnews.com/moneywatch/markets/', 'http://www.cbsnews.com/moneywatch/money/',
              'http://www.cbsnews.com/moneywatch/work/', 'http://www.cbsnews.com/moneywatch/small-business/',
              'http://www.cbsnews.com/moneywatch/retirement/', 'http://www.cbsnews.com/moneywatch/tech/',
              'http://www.cbsnews.com/moneywatch/trending/', 'http://www.cbsnews.com/videos/topics/moneywatch/',
              'http://www.cbsnews.com/search/author/mark-thoma/'
                     
              }    
        
cbs_home_pages = {'http://www.cbsnews.com/world/' : 'world',
                  'http://www.cbsnews.com/us/' : 'news',
                  'http://www.cbssports.com/' : 'sport',
                  'http://www.cbsnews.com/entertainment/' : 'entertainment',
                  'http://www.cbsnews.com/tech/' : 'tech',
                  'http://www.cbsnews.com/moneywatch/' : 'business',
                  'http://www.cbsnews.com/politics/' : 'politics',
                  'http://www.cbsnews.com/health/': 'health',
                         
                  'http://www.cbsnews.com/' : None,
                  }    
            
            
            
            
            
def extract_cbsnews_article(article, is_on_homepage, predifined_category=None):
            
    if (article.url in cbs_except or article.url + '/' in cbs_except or 'cbsnews' not in article.url): 
        return
    print('\n\n')
    print("url to extract: " + article.url)
    if (db_connect.is_url_existed(article.url) != -1):
        print("url is already existed")
        url_sharelikecomment_queue.put(article.url, True)
        return
           
    print('\n')
    normalized_url  = normalize_url(article.url)
    if ('cbsnews' not in normalized_url):
        return
    if (normalized_url in cbs_except or normalized_url + '/' in cbs_except):
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
        time_string = html_tree.xpath('//meta[@itemprop="datePublished"]')[0].attrib['content']
        time_string = time_string + " -4:00"
               
        #time_string = time_string + " UTC-0400"
    except BaseException as dateE:
        print("problem with time: {}".format(dateE))
    try:
        if (time_string is None):
            time_string = html_tree.xpath('//time[@class="storyDate"]')[0].attrib['datetime'] 
    except BaseException as dateE:
        print("problem with time: {}".format(dateE))
           
    try:
        if (time_string is None):
            time_string = html_tree.xpath('//time[@itemprop="uploadDate" ]')[0].attrib['datetime'] 
    except BaseException as dateE:
        print("problem with time: {}".format(dateE))
               
    print("extracted time: " + time_string)
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
        thumbnail_url = html_tree.xpath('//meta[@property="og:image"]')[0].attrib['content']
        print(thumbnail_url)
    except Exception as e:
        print('Thumbnaill not found.'.format(e))
    try:
        if(thumbnail_url is None):
            thumbnail_url = html_tree.xpath('//meta[@itemprop="thumbnailUrl" ]')[0].attrib['content']
            print(thumbnail_url)
    except Exception as e:
        print('Thumbnaill not found again'.format(e))
    try:
        if(thumbnail_url is None):
            thumbnail_url = html_tree.xpath('//meta[@name="twitter:image"]')[0].attrib['content']
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
        category_id = html_tree.xpath('//meta[@itemprop="articleSection"]')[0].attrib['content']
    except Exception as e:
        print('Category not found'.format(e))
                
    if (category_id is not None and category_id in cbs_category):
        article.category_id = cbs_category.get(category_id)
    if ('.cbssports.com' in article.url):
        article.category_id = 'sport'
    if ('cbsnews.com/videos' in article.url):
        article.category_id = predifined_category
    if (category_id == 'CBS Evening News' or category_id == 'CBS This Morning'):
        article.category_id = predifined_category
           
    print(article.category_id)
           
           
            
    if (article.published_time is None or article.title is None or article.category_id is None):
        raise Exception("missing fields")
            
            
            
    article.source_name = "CBS NEWS"       
    # get content
    article.parse()
    text = normalize_text(article.text)
    text_html = true_html.escape(article.article_html, True)
    normalized_title = normalize_text_nostop(article.title)
    article.source_id = cbs_source_id
         
    ''' insert this article to database, maybe send url to another thread to get count, share, .... or maket it asynchronous'''
    # when no exception, we insert to database
    try:
        article.id = db_connect.insert_article3(normalized_url, article.title, cbs_source_id, 
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
      'start get articles from abc news' +
      '...................................................\n' +
      '...................................................\n'
      )
try:
    db_connect = IIIDatbaseConnection()
    db_connect.init_database_cont()     
           
           
           
    ''' we process homepage'''
    for home_page in cbs_home_pages:
        print("extracting: " + home_page)
        page = requests.get(home_page)
        html_tree = html.fromstring(page.text)
        article_urls = html_tree.xpath('//a/@href')
        for home_url in article_urls:
            if  home_url is not None and len(home_url) > 16: 
                if ('http://' not in home_url and 'https://' not in home_url):
                    home_url = CBS_NEWS_HOME + home_url
                try:
                    article_home = Article(home_url, keep_article_html=True)
                    extract_cbsnews_article(article_home, True, cbs_home_pages.get(home_page))
                except Exception as e:
                    print('Smt wrong when process homepage ' + home_page +  ' article:  {}'.format(e) + home_url)
           
           
           
           
           
           
           
           
        
    db_connect.close_database_cont()   
except Exception as e:        
    print('Something went wrong with database: {}'.format(e))    
           
        
       
       
       
'''
=======================================================================================================================================
=======================================================================================================================================
========================================================== CBS news stop ==============================================================
=======================================================================================================================================
=======================================================================================================================================
''' 
       
     
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
          
'''
=======================================================================================================================================
=======================================================================================================================================
================================================= theblaze  start ===============================================================
=======================================================================================================================================
=======================================================================================================================================
''' 
          
              
              
theblaze_except = {
                      
                }
          
              
theblaze_category = {'Education' : 'education',
                     'Faith' : 'opinions',
                     'TheBlaze TV' : 'news',
                     'Government' : 'politics',
                     'Entertainment' : 'entertainment',
                     'Sports' : 'sport',
                     'Business' : 'business',
                     'Science' : 'science',
                     'Technology' : 'technology',
                     'Health' : 'health',
                     'World' : 'world',
                     'Crime' : 'news',
                     'US' : 'news',
                     'Media' : 'entertainment',
                     'Environment' : 'science',
                     'Campus' : 'education',
                     'Politics' : 'politics',
                   }    
          
theblaze_home_pages = {'http://www.theblaze.com/stories/category/education/' : 'education',
                       'http://www.theblaze.com/stories/category/world/' : 'world',
                       'http://www.theblaze.com/stories/category/environment/' : 'science',
                       'http://www.theblaze.com/' : None,
                       'http://www.theblaze.com/stories/category/politics/' : 'politics'
                       }    
              
              
              
              
              
def extract_theblaze_article(article, is_on_homepage, predifined_category=None):
              
    if ('201' not in article.url or 'theblaze.com' not in article.url): 
        return
     
    print('\n')
    print("url to extract: " + article.url)
    if (db_connect.is_url_existed(article.url) != -1):
        print("url is already existed")
        url_sharelikecomment_queue.put(article.url, True)
        return
     
    normalized_url  = normalize_url(article.url)
    if ('201' not in article.url or 'theblaze.com' not in normalized_url):
        return
    if (normalized_url in theblaze_except or normalized_url + '/' in theblaze_except):
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
        time_string = html_tree.xpath('//meta[@name="dc.date"]')[0].attrib['content']
        print("extracted time: " + time_string)
    except BaseException as dateE:
        print("problem with time: {}".format(dateE))
 
    date_time = parse(time_string)
    article.published_time = calendar.timegm(date_time.utctimetuple())
    print("time saved: ")
    print(datetime.fromtimestamp(article.published_time))
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
        thumbnail_url = html_tree.xpath('//meta[@name="twitter:image"]')[0].attrib['content']
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
              
     
    try:
        category_id = html_tree.xpath('//meta[@itemprop="articleSection"]')[0].attrib['content']
        article.category_id = theblaze_category.get(category_id)
    except Exception as e:
        print('category not found. {}'.format(e))
    print(category_id)
     
     
     
        
              
              
    if (article.published_time is None or article.title is None or article.category_id is None):
        raise Exception("missing fields")
              
              
              
    article.source_name = "THE BLAZE"         
    # get content
    article.parse()
    text = normalize_text(article.text)
    text_html = true_html.escape(article.article_html, True)
    normalized_title = normalize_text_nostop(article.title)
    article.source_id = theblaze_source_id
            
    ''' insert this article to database, maybe send url to another thread to get count, share, .... or maket it asynchronous'''
    # when no exception, we insert to database
    try:
        article.id = db_connect.insert_article3(normalized_url, article.title, theblaze_source_id, 
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
      'start get articles from Business Insider' +
      '...................................................\n' +
      '...................................................\n'
      )
try:
    db_connect = IIIDatbaseConnection()
    db_connect.init_database_cont()     
              
              
              
    ''' we process homepage'''
    for home_page in theblaze_home_pages:
        print("extracting: " + home_page)
        business_page = requests.get(home_page)
        html_tree = html.fromstring(business_page.text)
        article_urls = html_tree.xpath('//a/@href')
        for home_url in article_urls:
            if  home_url is not None and len(home_url) > 16: 
                if ('http://' not in home_url and 'https://' not in home_url):
                    home_url = THEBLAZE_HOME + home_url
                try:
                    article_home = Article(home_url, keep_article_html=True)
                    extract_theblaze_article(article_home, True, theblaze_home_pages.get(home_page))
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


















         
          
          
          
          
'''
=======================================================================================================================================
=======================================================================================================================================
========================================================= Reuters start ===============================================================
=======================================================================================================================================
=======================================================================================================================================
''' 
          
              
              
reuters_category = {'News - US' : 'news',
                    'news' : 'news',
                    'Finance - Deals' : 'business',
                    'Finance - Markets' : 'business',
                    'Finance - Business News' : 'business',
                    'Landing Finance-Legal' : 'business',
                    'Landing Finance - Deals' : 'business',
                    'Video - Business' : 'business',
                    'Video - Personal Finance' : 'business',
                    'Business' : 'business',
                    'business' : 'business',
                    'Finance - Deals' : 'business',
                    'Finance - Technology' : 'tech',
                    'News - World' : 'world',
                    'Finance - Personal Finance' : 'business',
                    'News - Sports' : 'sport',
                    'News - India Top News' : 'world',
                    'world' : 'world',
                    'Video - World News' : 'world',
                    'Video - Politics' : 'politics',
                    'politics' : 'politics',
                    'News - Politics' : 'politics',
                    'opinions' : 'opinions',
                    'News - Health' : 'health',
                    'News - Science' : 'science',
                    'Video - Technology' : 'tech',
                    'Finance - Green Business' : 'science',
                    'News - Entertainment' : 'entertainment',
                    'News - Lifestyle' : 'life',
                }
          
              
reuters_except = { }    
          
reuters_home_pages = {'http://www.reuters.com/finance' : 'business',
                      'http://www.reuters.com/news/world' : 'world',
                    'http://www.reuters.com/finance/personal-finance' : 'business',
                    'http://blogs.reuters.com/us' : 'opinions',
                    'http://www.reuters.com/news/lifestyle': 'life',
                  }    
              
              
              
              
              
def extract_reutersnews_article(article, is_on_homepage, predifined_category=None):
              
    if ( "/2015" not in article.url or article.url in reuters_except or article.url + '/' in reuters_except or '.reuters.com' not in article.url ): 
        return
    if (not hasNumbers(article.url)):
        return
    print('\n')
    #print("url to extract: " + article.url)
    if (db_connect.is_url_existed(article.url) != -1):
        print("url is already existed")
        url_sharelikecomment_queue.put(article.url, True)
        return
    normalized_url  = normalize_url(article.url)
    if ('.reuters.com' not in normalized_url):
        return
    if (normalized_url in reuters_except or normalized_url + '/' in reuters_except):
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
    category_id = None
    date_time = None
               
    article.download()
    html_tree = html.fromstring(article.html)
               
              
              
    try:
        meta_data = html_tree.xpath('//script[@type="application/ld+json"]/text()')[0]
        meta_data = json.loads(meta_data)
        article.title = meta_data['headline']
        article.thumbnail_url = meta_data['thumbnailUrl']
        
        time_string = meta_data['dateCreated']
        date_time = parse(time_string)
        article.published_time = calendar.timegm(date_time.utctimetuple())
        print("time saved: ")
        print(datetime.fromtimestamp(article.published_time))
        if (article.published_time > time.time()):
            article.published_time = None
        print(article.published_time)
        
        category_id = meta_data['articleSection']
        if (not category_id or category_id is "Unknown"):
            category_id = predifined_category
        if (category_id is not None and category_id in reuters_category):
            article.category_id = reuters_category.get(category_id)
        print("extracted category: "+ category_id)
        print("saved category: "+ article.category_id)
        
    except Exception as dateE:
        print("problem with meta data: {}".format(dateE))
    
    
    try:
        if (article.published_time is None):
            meta_data = html_tree.xpath("//meta[@name='parsely-page']")[0].attrib['content']
            meta_data = json.loads(meta_data)
            article.title = meta_data['title']
            article.thumbnail_url = meta_data['image_url']
            if (article.thumbnail_url is None):
                article.thumbnail_url = article.top_image
            
            time_string = meta_data['pub_date']
            date_time = parse(time_string)
            article.published_time = calendar.timegm(date_time.utctimetuple())
            print("time saved: ")
            print(datetime.fromtimestamp(article.published_time))
            if (article.published_time > time.time()):
                article.published_time = None
            print(article.published_time)
            
            category_id = meta_data['section']
            if (category_id is None or len(category_id) == 0 or category_id is "Unknown" or category_id is "General"):
                category_id = predifined_category
            if ('blogs.reuters' in article.url):
                category_id = 'opinions'
                article.category_id = 'opinions'
            if (category_id is not None and category_id in reuters_category):
                article.category_id = reuters_category.get(category_id)
            print("extracted category: "+ article.category_id)
        
    except Exception as dateE:
        print("problem with meta data: {}".format(dateE))
 
              
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
              
              
              
    if (article.published_time is None or article.title is None or article.category_id is None):
        raise Exception("missing fields ")
              
              
              
    article.source_name = "REUTERS"          
    # get content
    article.parse()
    text = normalize_text(article.text)
    text_html = true_html.escape(article.article_html, True)
    normalized_title = normalize_text_nostop(article.title)
    article.source_id = reuters_source_id
            
    ''' insert this article to database, maybe send url to another thread to get count, share, .... or maket it asynchronous'''
    # when no exception, we insert to database
    try:
        article.id = db_connect.insert_article3(normalized_url, article.title, reuters_source_id, 
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
      'start get articles from Reuters' +
      '...................................................\n' +
      '...................................................\n'
      )
try:
    db_connect = IIIDatbaseConnection()
    db_connect.init_database_cont()     
              
              
              
    ''' we process homepage'''
    for home_page in reuters_home_pages:
        print("extracting: " + home_page)
        reuters_page = requests.get(home_page)
        html_tree = html.fromstring(reuters_page.text)
        article_urls = html_tree.xpath('//a/@href')
        for home_url in article_urls:
            if  home_url is not None and len(home_url) > 16: 
                if ('http://' not in home_url and 'https://' not in home_url):
                    home_url = REUTERS_HOME + home_url
                try:
                    article_home = Article(home_url, keep_article_html=True)
                    extract_reutersnews_article(article_home, True, reuters_home_pages.get(home_page))
                except Exception as e:
                    print('Smt wrong when process homepage' + home_page +  'article:  {}'.format(e) + home_url)
              
              
              
              
              
              
              
              
           
    db_connect.close_database_cont()   
except Exception as e:        
    print('Something went wrong with database: {}'.format(e))    
              
              
          
'''
=======================================================================================================================================
=======================================================================================================================================
================================================= NBC news stop ===============================================================
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
