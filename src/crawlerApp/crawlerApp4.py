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
BLOOMBERG_HOME_PAGE = 'http://www.bloomberg.com/'
FOX_NEWS_HOME = 'http://www.foxnews.com/'
ESPN_HOME = 'http://espn.go.com/'
BUZZFEED_HOME = 'http://www.buzzfeed.com/'
FORBES_HOME = 'http://www.forbes.com'
PEOPLE_HOME = 'http://www.people.com/'
VOGUE_HOME = 'http://www.vogue.com/?us_site=y'
EVERYDAY_HEATH_HOME = 'http://www.everydayhealth.com'
EONLINE_HOME = 'http://www.eonline.com';
TECHCRUNCH_HOME = 'http://techcrunch.com'
BLEACH_REPORT = 'http://bleacherreport.com'
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
USA = 'us'








'''
============================================================================================
====================== Start thread to get url statistic, post to page here ================
============================================================================================
'''
print('Start thread get like share comments')
url_sharelikecomment_queue = queue.Queue()
share_like_comment_thread = CommentLikeShrareGetterThread(queue=url_sharelikecomment_queue)
share_like_comment_thread.start()

print('Start thread to post to page')
post_queue = queue.Queue()
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
        
        
        
        
    # get content
    article.parse()
    text = normalize_text(article.text)
    text_html = true_html.escape(get_text_html_saulify(normalized_url), True)
    normalized_title = normalize_text_nostop(article.title)
    
    ''' insert this article to database, maybe send url to another thread to get count, share, .... or maket it asynchronous'''
    # when no exception, we insert to database
    try:
        print(db_connect.insert_article3(normalized_url, article.title, everydayhealth_source_id, 
                                     article.category_id, False, is_on_homepage, article.published_time,
                                     article.thumbnail_url, article.short_description, USA, text_html, text, normalized_title))
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
                    article_home = Article(home_url)
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
        
        
        
        
    # get content
    article.parse()
    text = normalize_text(article.text)
    text_html = true_html.escape(get_text_html_saulify(normalized_url), True)
    normalized_title = normalize_text_nostop(article.title) 
    ''' insert this article to database, maybe send url to another thread to get count, share, .... or maket it asynchronous'''
    # when no exception, we insert to database
    try:
        print(db_connect.insert_article3(normalized_url, article.title, eonline_source_id, 
                                     article.category_id, False, is_on_homepage, article.published_time,
                                     article.thumbnail_url, article.short_description, USA, text_html, text, normalized_title))
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
                    article_home = Article(home_url)
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
        
        
        
        
    # get content
    article.parse()
    text = normalize_text(article.text)
    text_html = true_html.escape(get_text_html_saulify(normalized_url), True)
    normalized_title = normalize_text_nostop(article.title)
    
    ''' insert this article to database, maybe send url to another thread to get count, share, .... or maket it asynchronous'''
    # when no exception, we insert to database
    try:
        print(db_connect.insert_article3(normalized_url, article.title, techcrunch_source_id, 
                                     article.category_id, False, is_on_homepage, article.published_time,
                                     article.thumbnail_url, article.short_description, USA, text_html, text, normalized_title))
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
                    article_home = Article(home_url)
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
       
       
       
       
    # get content
    article.parse()
    text = normalize_text(article.text)
    text_html = true_html.escape(get_text_html_saulify(normalized_url), True)
    normalized_title = normalize_text_nostop(article.title)
    
    ''' insert this article to database, maybe send url to another thread to get count, share, .... or maket it asynchronous'''
    # when no exception, we insert to database
    try:
        print(db_connect.insert_article3(normalized_url, article.title, bleachreport_source_id, 
                                     article.category_id, False, is_on_homepage, article.published_time,
                                     article.thumbnail_url, article.short_description, USA, text_html, text, normalized_title))
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
                    article_home = Article(home_url)
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
         
         
         
         
    # get content
    article.parse()
    text = normalize_text(article.text)
    text_html = true_html.escape(get_text_html_saulify(normalized_url), True)
    normalized_title = normalize_text_nostop(article.title)
       
    ''' insert this article to database, maybe send url to another thread to get count, share, .... or maket it asynchronous'''
    # when no exception, we insert to database
    try:
        print(db_connect.insert_article3(normalized_url, article.title, vogue_source_id, 
                                     article.category_id, False, is_on_homepage, article.published_time,
                                     article.thumbnail_url, article.short_description, USA, text_html, text, normalized_title))
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
                    article_home = Article(home_url)
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
                'Health' : 'health'
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
          
          
          
          
    # get content
    article.parse()
    text = normalize_text(article.text)
    text_html = true_html.escape(get_text_html_saulify(normalized_url), True)
    normalized_title = normalize_text_nostop(article.title)
       
    ''' insert this article to database, maybe send url to another thread to get count, share, .... or maket it asynchronous'''
    # when no exception, we insert to database
    try:
        print(db_connect.insert_article3(normalized_url, article.title, cbs_source_id, 
                                     article.category_id, False, is_on_homepage, article.published_time,
                                     article.thumbnail_url, article.short_description, USA, text_html, text, normalized_title))
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
                    article_home = Article(home_url)
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
