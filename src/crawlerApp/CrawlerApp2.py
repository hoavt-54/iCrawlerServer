'''
Created on Mar 15, 2015

@author: hoavu
'''

import calendar
from datetime import datetime
from dateutil.parser import parse
from lxml import html
from newspaper.article import Article
import os.path
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
# print('Start thread get like share comments')
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
================================================= Washington Post start ===============================================================
=======================================================================================================================================
=======================================================================================================================================
''' 
             
                 
                 
washington_post_category = {'news' : 'news',
                'local' : 'news',
                'national' : 'news',
                'world' : 'world',
                'opinions' : 'opinions',
                'politics' : 'politics',
                'health' : 'health',
                'tech': 'tech',
                'sports' : 'sport',
                'entertainment': 'entertainment',
                'business' : 'business',
                'education' : 'education',
                'lifestyle' : 'life',
                'business' : 'business',
                'goingoutguide' : 'entertainment',
                }
             
                 
washington_post_except = {'http://www.washingtonpost.com/ed-okeefe/2011/02/02/ABqNUZE_page.html', 
                          'http://www.washingtonpost.com/niraj-chokshi/2014/06/10/6b40abf2-f0cb-11e3-9ebc-2ee6f81ed217_page.html',
                          'http://www.washingtonpost.com/the-posts-view/2011/12/07/gIQAoEIscO_page.html',
                          'http://www.washingtonpost.com/letters-to-the-editor/2010/07/06/ABjQAIP_linkset.html',
                          'http://www.washingtonpost.com/the-posts-view/2011/12/07/gIQAoEIscO_page.html',
                          'http://www.washingtonpost.com/jonathan-capehart/2011/02/24/AB1tR7I_page.html',
                          'http://www.washingtonpost.com/opinions/ed-rogers/2012/08/09/5a9b172a-fc30-11e0-9522-7bbb534ce3e0_page.html',
                          'http://www.washingtonpost.com/opinions/erik-wemple/2012/12/17/85b31a30-9d0c-11e0-8017-e14307b2451a_page.html',
                          'http://www.washingtonpost.com/dan-stillman/2011/10/18/gIQAsDZFvL_page.html',
                          'http://www.washingtonpost.com/dana-hedgpeth/2011/02/28/ABAxzsM_page.html',
                          'http://www.washingtonpost.com/dan-steinberg/2011/02/09/ABq4PTF_page.html',
                          }    
             
washington_post_home_pages = {'http://www.washingtonpost.com/politics/' : 'politics',
                  'http://www.washingtonpost.com/opinions/' : 'opinions',
                  'http://www.washingtonpost.com/local/' : 'news',
                  'http://www.washingtonpost.com/sports/' : 'sport',
                  'http://www.washingtonpost.com/world' : 'world',
                  'http://www.washingtonpost.com/national/' : 'news',
                  'http://www.washingtonpost.com/business/' : 'business',
                  'http://www.washingtonpost.com/business/technology/' : 'tech',
                  'http://www.washingtonpost.com/lifestyle/' : 'life',
                  'http://www.washingtonpost.com/entertainment/' : 'entertainment',
                  'http://www.washingtonpost.com/local/education/' : 'education',
                  'http://www.washingtonpost.com/' : None
                  }    
             
             
                 
def extract_washington_post_article(article, is_on_homepage, predifined_category=None):
                 
    if ( ('2015' not in article.url and '2016' not in article.url and '2017' not in article.url) or article.url in washington_post_except 
                or article.url + '/' in washington_post_except or 'washingtonpost' not in article.url 
                or 'capital-weather-gang' in article.url): 
        return
    if (db_connect.is_url_existed(article.url) != -1):
        print("url is already existed")
        url_sharelikecomment_queue.put(article.url, True)
        return
    print('\n')
    normalized_url  = normalize_url(article.url)
    if ('washingtonpost' not in normalized_url):
        return
    if (normalized_url in washington_post_except or normalized_url + '/' in washington_post_except):
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
                 
                 
                 
    # get time
    try:
        time_string = html_tree.xpath('//span[@class="pb-timestamp"]/text()')[0]
        print("extracted time: " + time_string)
        #time_string = time_string + " UTC-0400"
    except BaseException as dateE:
        print("problem with time: {}".format(dateE))        
                 
    date_time = parse(time_string +  " -4:00")
    published_time = calendar.timegm(date_time.utctimetuple())
    print("time saved: ")
    print(datetime.fromtimestamp(published_time))
    print(published_time)
    if (published_time > time.time()):
        published_time = None
    article.published_time = published_time
                 
                 
                 
    #get title
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
        thumbnail_url = html_tree.xpath('//meta[@name="twitter:image:src"]')[0].attrib['content']
        print(thumbnail_url)
    except Exception as e:
        print('')
    try:
        if(thumbnail_url is None):
            thumbnail_url = html_tree.xpath('//meta[@property="og:image"]')[0].attrib['content']
            print(thumbnail_url)
    except Exception as e:
        print('')
    try:
        if(thumbnail_url is None):
            thumbnail_url = html_tree.xpath('//meta[@name="thumbnail"]')[0].attrib['content']
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
        category_id = html_tree.xpath('//meta[@name="section"]')[0].attrib['content']
        try:
            category_sub = category_id.split("/")[2]
            if (category_sub is not None and category_sub == 'technology'):
                category_id = 'tech'
        except Exception as e:
            print('')
        if (category_id != 'tech'):
            category_id = category_id.split("/")[1]
        print("extracted category: " + category_id)
    except Exception as e:
        print('Category not found'.format(e))
                     
    if (category_id is not None and category_id in washington_post_category):
        article.category_id = washington_post_category.get(category_id)
    if (article.category_id is None and ('.washingtonpost.com/national/' in article.url or 
                                         '.washingtonpost.com/local/' in article.url or 
                                         'www.washingtonpost.com/news/' in article.url)):
        article.category_id = 'news'
    if (article.category_id is None and 'washingtonpost.com/politics/' in article.url):
        article.category_id = 'politics'
    if (article.category_id is None and 'washingtonpost.com/sports/' in article.url):
        article.category_id = 'sport'
    if (article.category_id is None and 'washingtonpost.com/world/' in article.url):
        article.category_id = 'world'
    if (article.category_id is None and 'washingtonpost.com/business/' in article.url):
        article.category_id = 'business'
    if (article.category_id is None and 'washingtonpost.com/opinions/' in article.url):
        article.category_id = 'opinions'
    if (article.category_id is None and 'washingtonpost.com/lifestyle/travel/' in article.url):
        article.category_id = 'travel'
    if (article.category_id is None and 'washingtonpost.com/lifestyle/food/' in article.url):
        article.category_id = 'entertainment'
    if (article.category_id is None and predifined_category is 'education'):
        article.category_id = 'education'
    if (article.category_id is None):
        article.category_id = "others"
    print(article.category_id)
        
                 
                 
                 
    if (article.published_time is None or article.title is None or article.category_id is None):
        raise Exception("missing fields")
                 
                 
                 
    article.source_name = "WASHINGTONPOST.COM"           
    # get content
    article.parse()
    text = normalize_text(article.text)
    text_html = true_html.escape(article.article_html, True)
    normalized_title = normalize_text_nostop(article.title)
    article.source_id = washington_post_source_id
        
    ''' insert this article to database, maybe send url to another thread to get count, share, .... or maket it asynchronous'''
    # when no exception, we insert to database
    try:
        article.id = db_connect.insert_article3(normalized_url, article.title, washington_post_source_id, 
                                     article.category_id, False, is_on_homepage, article.published_time,
                                     article.thumbnail_url, article.short_description, USA, text_html, text,normalized_title)
    except Exception as dbE:
        print("Error when insert article to db. {}".format(dbE))
        return
    # after insert to database, we put this url to get share, comment, like
    url_sharelikecomment_queue.put(normalized_url, True)
    article.url = normalized_url
    post_queue.put(article, True)
                 
             
             
             
             
             
              
print('...................................................\n' +
      '...................................................\n' + 
      '...................................................\n' +
      'start get articles from washington post' +
      '...................................................\n' +
      '...................................................\n'
      )
try:
    db_connect = IIIDatbaseConnection()
    db_connect.init_database_cont()     
                 
                 
                 
    ''' we process homepage'''
    for home_page in washington_post_home_pages:
        print("extracting: " + home_page)
        washington_page = requests.get(home_page)
        html_tree = html.fromstring(washington_page.text)
        article_urls = html_tree.xpath('//a/@href')
        for home_url in article_urls:
            if  home_url is not None and len(home_url) > 16: 
                if ('http://' not in home_url and 'https://' not in home_url):
                    home_url = WASHINGTON_POST + home_url
                try:
                    article_home = Article(home_url, keep_article_html=True)
                    extract_washington_post_article(article_home, True, washington_post_home_pages.get(home_page))
                except Exception as e:
                    print('Smt wrong when process homepage' + home_page +  'article:  {}'.format(e) + home_url)
                 
                 
                 
                 
                 
                 
                 
                 
              
    db_connect.close_database_cont()   
except Exception as e:        
    print('Something went wrong with database: {}'.format(e))    
                 
              
             
             
             
             
'''
=======================================================================================================================================
=======================================================================================================================================
================================================= Washington Post stop ===============================================================
=======================================================================================================================================
=======================================================================================================================================
''' 
             
             
                
                
                
                
                
                
                
               
               
           
           
           
           
           
           
           
           
           
'''
=======================================================================================================================================
=======================================================================================================================================
===================================================== ABC News start ==================================================================
=======================================================================================================================================
=======================================================================================================================================
''' 
           
abc_category = {'US' : 'news',
                'U.S.' : 'news',
                'International' : 'world',
                'Politics' : 'politics',
                'Entertainment' : 'entertainment',
                'Technology' : 'tech',
                'Health' : 'health',
                'Lifestyle' : 'life',
                'Business' : 'business',
                'Money' : 'business',
                'Sports' : 'sport',
                }
            
                
abc_except = { }    
            
abc_home_pages = {'http://abcnews.go.com/US/' : 'news',
                  'http://abcnews.go.com/International/' : 'world',
                  'http://abcnews.go.com/Politics/' : 'politics',
                  'http://abcnews.go.com/Entertainment/' : 'entertainment',
                  'http://abcnews.go.com/Technology/' : 'tech',
                  'http://abcnews.go.com/Health/' : 'health',
                  'http://abcnews.go.com/Lifestyle/' : 'life',
                  'http://abcnews.go.com/Business/' : 'business',
                  'http://abcnews.go.com/Sports/' : 'sport',
                  'http://abcnews.go.com/' : None,
                  }    
                
                
                
                
                
def extract_abcnews_article(article, is_on_homepage, predifined_category=None):
                
    if (  article.url in abc_except or article.url + '/' in abc_except or 'abc' not in article.url): 
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
        time_string = html_tree.xpath('//meta[@itemprop="datepublished"]')[0].attrib['content']
        #time_string = time_string + " UTC-0400"
    except BaseException as dateE:
        print("")
    try:
        if (time_string is None):
            time_string = html_tree.xpath('//div[@class="date"]/text()')[0]
        #time_string = time_string + " UTC-0400"
    except BaseException as dateE:
        print("problem with time: {}".format(dateE))
    try:
        if (time_string is None):
            time_string = html_tree.xpath('//meta[@itemprop="uploadDate"]')[0].attrib['content']
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
        thumbnail_url = html_tree.xpath('//meta[@name="twitter:image:src"]')[0].attrib['content']
        print(thumbnail_url)
    except Exception as e:
        print('')
    try:
        if(thumbnail_url is None):
            thumbnail_url = html_tree.xpath('//meta[@property="og:image"]')[0].attrib['content']
            print(thumbnail_url)
    except Exception as e:
        print('')
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
        category_id = html_tree.xpath('//a[@itemprop="articleSection"]/text()')[0]
    except Exception as e:
        print('Category not found'.format(e))
                   
    try:
        if category_id is None:
            result = re.search('abcnews\.go\.com/((?:[^/])*)/', article.url)
            category_id = result.group(1)
    except Exception as e:
        print('Category not found again'.format(e))
                    
    if (category_id is not None and category_id in abc_category):
        article.category_id = abc_category.get(category_id)
    print(article.category_id)
                
                
    if (article.published_time is None or article.title is None or article.category_id is None):
        raise Exception("missing fields")
                
                
                
    article.source_name = "ABC NEWS"           
    # get content
    article.parse()
    text = normalize_text(article.text)
    text_html = true_html.escape(article.article_html, True)
    normalized_title = normalize_text_nostop(article.title)
    article.source_id = abc_source_id
     
    ''' insert this article to database, maybe send url to another thread to get count, share, .... or maket it asynchronous'''
    # when no exception, we insert to database
    try:
        article.id = db_connect.insert_article3(normalize_url, article.title, abc_source_id, 
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
    for home_page in abc_home_pages:
        print("extracting: " + home_page)
        abc_page = requests.get(home_page)
        html_tree = html.fromstring(abc_page.text)
        article_urls = html_tree.xpath('//a/@href')
        for home_url in article_urls:
            if  home_url is not None and len(home_url) > 16: 
                if ('http://' not in home_url and 'https://' not in home_url):
                    home_url = ABC_HOMEPAGE + home_url
                try:
                    article_home = Article(home_url, keep_article_html=True)
                    extract_abcnews_article(article_home, True, abc_home_pages.get(home_page))
                except Exception as e:
                    print('Smt wrong when process homepage ' + home_page +  ' article:  {}'.format(e) + home_url)
               
               
               
               
               
               
               
               
            
    db_connect.close_database_cont()   
except Exception as e:        
    print('Something went wrong with database: {}'.format(e))    
               
            
           
           
           
               
           
           
           
'''
=======================================================================================================================================
=======================================================================================================================================
===================================================== ABC News stop ===================================================================
=======================================================================================================================================
=======================================================================================================================================
''' 
          
         
         
         
         
         
         
         
        
        
        
        
        
        
        
        
        
        
        
      
      
'''
=======================================================================================================================================
=======================================================================================================================================
==================================================== Los Angeles Time start ===========================================================
=======================================================================================================================================
=======================================================================================================================================
''' 
      
latimes_category = {'LOCAL' : 'news',
                'Sports' : 'sport',
                'ARTS & ENTERTAINMENT' : 'entertainment',
                'Entertainment' : 'entertainment',
                'Business' : 'business',
                'technology' : 'tech',
                'Opinion' : 'opinions',
                'nation' : 'news',
                'Nation' : 'news',
                'World' : 'world',
                'Fashion' : 'style',
                'Style' : 'style',
                'Home & Garden' : 'life',
                'Food' : 'life',
                'Health & Fitness' : 'health',
                'Books' : 'life',
                'Travel' : 'travel',
                'Sports' : 'sport',
                'BUSINESS': 'business',
                'Science' : 'science'
                }
       
           
latimes_except = { }    
       
latimes_home_pages = {'http://www.latimes.com/local/' : 'news',
                  'http://www.latimes.com/local/california/' : 'news',
                  'http://www.latimes.com/sports/' : 'sport',
                  'http://www.latimes.com/entertainment/' : 'entertainment',
                  'http://www.latimes.com/business/technology/' : 'tech',
                  'http://www.latimes.com/business/' : 'business',
                  'http://www.latimes.com/opinion/' : 'opinions',
                        
                  'http://www.latimes.com/nation/' : 'news',
                  'http://www.latimes.com/world/' : 'world',
                  'http://www.latimes.com/health/' : 'health',
                  'http://www.latimes.com/style/' : 'life',
                  'http://www.latimes.com/home/' : 'life',
                  'http://www.latimes.com/food/' : 'life',
                  'http://www.latimes.com/travel/' : 'travel',
                        
                  'http://www.latimes.com/' : None,
                  }    
           
           
           
           
           
def extract_latimes_article(article, is_on_homepage, predifined_category=None):
           
    if ( '201' not in article.url or article.url in latimes_except or article.url + '/' in latimes_except or 'latimes' not in article.url): 
        return
    print('\n\n')
    print("url to extract: " + article.url)
    if (db_connect.is_url_existed(article.url) != -1):
        print("url is already existed")
        url_sharelikecomment_queue.put(article.url, True)
        return
          
    print('\n')
    normalized_url  = normalize_url(article.url)
    if ('latimes' not in normalized_url):
        return
    if (normalized_url in latimes_except or normalized_url + '/' in latimes_except):
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
    except BaseException as dateE:
        print("problem with time: {}".format(dateE))
    try:
        time_string = html_tree.xpath('//meta[@name="date"]')[0].attrib['content']
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
        thumbnail_url = html_tree.xpath('//div[@class="trb_allContentWrapper "]')[0].attrib['data-content-thumbnail']
        print(thumbnail_url)
    except Exception as e:
        print('')
    try:
        if(thumbnail_url is None):
            thumbnail_url = html_tree.xpath('//meta[@property="og:image"]')[0].attrib['content']
            print(thumbnail_url)
    except Exception as e:
        print('')
    try:
        if(thumbnail_url is None):
            thumbnail_url = html_tree.xpath('//meta[@name="thumbnail"]')[0].attrib['content']
            print(thumbnail_url)
    except Exception as e:
        print('Thumbnaill not found again'.format(e))
    article.thumbnail_url = thumbnail_url
               
               
           
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
    article.short_description = short_description
           
           
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
               
    if (category_id is not None and category_id in latimes_category):
        article.category_id = latimes_category.get(category_id)
    print(article.category_id)
           
           
    if (article.published_time is None or article.title is None or article.category_id is None):
        raise Exception("missing fields")
           
           
           
    article.source_name = "Los Angeles Times"        
    # get content
    article.parse()
    text = normalize_text(article.text)
    text_html = true_html.escape(article.article_html, True)
    normalized_title = normalize_text_nostop(article.title)
    article.source_id = latimes_source_id
    
    ''' insert this article to database, maybe send url to another thread to get count, share, .... or maket it asynchronous'''
    # when no exception, we insert to database
    try:
        article.id = db_connect.insert_article3(normalized_url, article.title, latimes_source_id, 
                                     article.category_id, False, is_on_homepage, article.published_time,
                                     article.thumbnail_url, article.short_description, USA, text_html, text,normalized_title)
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
    for home_page in latimes_home_pages:
        print("extracting: " + home_page)
        la_page = requests.get(home_page)
        html_tree = html.fromstring(la_page.text)
        article_urls = html_tree.xpath('//a/@href')
        for home_url in article_urls:
            if  home_url is not None and len(home_url) > 46: 
                if ('http://' not in home_url and 'https://' not in home_url):
                    home_url = LA_TIMES_HOMEPAGE + home_url
                try:
                    article_home = Article(home_url, keep_article_html=True)
                    extract_latimes_article(article_home, True, latimes_home_pages.get(home_page))
                except Exception as e:
                    print('Smt wrong when process homepage ' + home_page +  ' article:  {}'.format(e) + home_url)
          
          
          
          
          
          
          
          
       
    db_connect.close_database_cont()   
except Exception as e:        
    print('Something went wrong with database: {}'.format(e))    
          
       
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
'''
=======================================================================================================================================
=======================================================================================================================================
===================================================== Los Angeles Time stop ===========================================================
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
