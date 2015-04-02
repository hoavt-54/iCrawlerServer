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
post_queue = queue.Queue(20)
page_poster_thread = PostToFacebookPage(queue=post_queue)
page_poster_thread.start()
'''
============================================================================================
'''  













 
 
 
 
 
 
 
 
 
                
                     
'''
=======================================================================================================================================
=======================================================================================================================================
================================================= Huffington Post start ===============================================================
=======================================================================================================================================
=======================================================================================================================================
''' 
huffington_category = {'Politics' : 'politics',
                       'Business' : 'business',
                       'Entertainment' : 'entertainment',
                       'Technology' : 'tech',
                       'Green' : 'tech',
                       'Media' : 'news',
                       'WorldPost': 'world',
                       'Healthy Living' :'health',
                       'Money' : 'business',
                       'Small Business' : 'business',
                       'Sports' : 'sport',
                       'Education' : 'education',
                       'Celebrity' : 'entertainment',
                       'Comedy' : 'entertainment',
                       'GPS for the Soul' : 'health',
                       'Style' : 'style',
                       'HuffPost Home' : 'life',
                       'Taste' : 'entertainment',
                       'Weddings' : 'entertainment',
                       'Travel' : 'travel',
                       'Arts' : 'entertainment',
                       'Science' : 'tech',
                       'Religion' : 'opinions',
                       'Black Voices' : 'opinions',
                       'Gay Voices' : 'opinions'
                       }
                
huffington_except = {}
            
def extract_huffington_article(article, is_on_homepage, predifined_category=None):
    #print("url to extract: " + article.url)
    if ('/201' not in article.url or article.url in huffington_except or article.url + '/' in huffington_except or 'huffingtonpost.com' not in article.url ):
        return
    if (db_connect.is_url_existed(article.url) != -1):
        print("url is already existed")
        url_sharelikecomment_queue.put(article.url, True)
        return
    normalized_url = normalize_url(article.url)
    if ('huffingtonpost.com' not in normalized_url):
        return
    if (normalized_url in huffington_except or normalized_url + '/' in huffington_except):
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
    if (predifined_category is not None):
        article.category_id = predifined_category
                 
    article.download()
    html_tree = html.fromstring(article.html)
                 
    #get time
    try:
        time_string = html_tree.xpath('//meta[@name="sailthru.date"]')[0].attrib['content']
    except BaseException as dateE:
        print("problem with time: {}".format(dateE))
                    
    #get time
    try:
        if (time_string is None):
            time_string = html_tree.xpath('//meta[@property="sailthru.date"]')[0].attrib['content']
    except BaseException as dateE:
        print("problem with time: {}".format(dateE)) 
                 
    if (time_string is not None):
        date_time = parse(time_string)
        article.published_time = calendar.timegm(date_time.utctimetuple())
        if (article.published_time > time.time()):
            article.published_time = None
        print(article.published_time)
                 
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
    article.title = title
                 
                 
    # get thumbnail
    try:
        thumbnail_url = html_tree.xpath('//link[@rel="image_src"]')[0].attrib['href']
        print(thumbnail_url)
    except Exception as e:
        print("")
    try:
        if(thumbnail_url is None):
            thumbnail_url = html_tree.xpath('//meta[@name="image"]')[0].attrib['content']
            print(thumbnail_url)
    except Exception as e:
        print("")
    try:
        if(thumbnail_url is None):
            thumbnail_url = html_tree.xpath('//meta[@property="sailthru.image.thumb"]')[0].attrib['content']
            print(thumbnail_url)
    except Exception as e:
        print("")
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
        print("")    
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
        print("") 
    try:
        if category_id is None:
            category_id = html_tree.xpath('//meta[@name="category"]')[0].attrib['content']
    except Exception as e:
        print('Category not found again'.format(e)) 
                    
    if (category_id is not None):
        article.category_id = huffington_category.get(category_id)
        print("extracted category: "+ category_id)
    if (article.category_id is None):
        article.category_id = 'others'
                
    print(article.category_id)
                 
                 
    if (article.published_time is None or article.title is None or article.category_id is None):
        raise Exception("")
                
                
    # get content
    article.parse()
    text = normalize_text(article.text)
    text_html = true_html.escape(get_text_html_saulify(normalized_url), True)
    normalized_title = normalize_text_nostop(article.title)
    
    ''' insert this article to database, maybe send url to another thread to get count, share, .... or maket it asynchronous'''
    # when no exception, we insert to database
    try:
        print(db_connect.insert_article3(normalized_url, article.title, huffington_source_id, 
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
      'start get articles from huffington' +
      '...................................................\n' +
      '...................................................\n'
      )
try:
    db_connect = IIIDatbaseConnection()
    db_connect.init_database_cont() 
            
                
                
                
    ''' we process homepage polictis'''
    HUFFINTION_POST_POLICTICS = 'http://www.huffingtonpost.com/politics/'
    huffington_hompage_polictics = requests.get(HUFFINTION_POST_POLICTICS)
    html_tree = html.fromstring(huffington_hompage_polictics.text)
    article_urls = html_tree.xpath('//a/@href')
    for home_url in article_urls:
        if  home_url is not None and len(home_url) > 16: 
            if ('http://' not in home_url and 'https://' not in home_url):
                home_url = HUFFINGTON_POST_HOME + home_url
            try:
                article_home = Article(home_url)
                extract_huffington_article(article_home, True, huffington_category.get('Polictis'))
            except Exception as e:
                print('Smt wrong when process homepage polictics  article:  {}'.format(e) + home_url)
                   
            
            
            
            
            
    ''' we process homepage business'''
    HUFFINTION_POST_BUSINESS= 'http://www.huffingtonpost.com/business/'
    huffington_hompage_business = requests.get(HUFFINTION_POST_BUSINESS)
    html_tree = html.fromstring(huffington_hompage_business.text)
    article_urls = html_tree.xpath('//a/@href')
    for home_url in article_urls:
        if  home_url is not None and len(home_url) > 16: 
            if ('http://' not in home_url and 'https://' not in home_url):
                home_url = HUFFINGTON_POST_HOME + home_url
            try:
                article_home = Article(home_url)
                extract_huffington_article(article_home, True, huffington_category.get('Business'))
            except Exception as e:
                print('Smt wrong when process homepage business  article:  {}'.format(e) + home_url)
            
            
            
            
            
            
    ''' we process homepage entertainment'''
    HUFFINTION_POST_ENTERTAIN= 'http://www.huffingtonpost.com/entertainment/'
    huffington_hompage_business = requests.get(HUFFINTION_POST_ENTERTAIN)
    html_tree = html.fromstring(huffington_hompage_business.text)
    article_urls = html_tree.xpath('//a/@href')
    for home_url in article_urls:
        if  home_url is not None and len(home_url) > 16: 
            if ('http://' not in home_url and 'https://' not in home_url):
                home_url = HUFFINGTON_POST_HOME + home_url
            try:
                article_home = Article(home_url)
                extract_huffington_article(article_home, True, 'entertainment')
            except Exception as e:
                print('Smt wrong when process homepage entertainment  article:  {}'.format(e) + home_url)
            
            
            
            
            
            
            
            
            
    ''' we process homepage tech'''
    HUFFINTION_POST_ENTERTAIN= 'http://www.huffingtonpost.com/tech/'
    huffington_hompage_business = requests.get(HUFFINTION_POST_ENTERTAIN)
    html_tree = html.fromstring(huffington_hompage_business.text)
    article_urls = html_tree.xpath('//a/@href')
    for home_url in article_urls:
        if  home_url is not None and len(home_url) > 16: 
            if ('http://' not in home_url and 'https://' not in home_url):
                home_url = HUFFINGTON_POST_HOME + home_url
            try:
                article_home = Article(home_url)
                extract_huffington_article(article_home, True, 'tech')
            except Exception as e:
                print('Smt wrong when process homepage tech  article:  {}'.format(e) + home_url)
            
            
            
            
            
    ''' we process homepage media'''
    HUFFINTION_POST_ENTERTAIN= 'http://www.huffingtonpost.com/media/'
    huffington_hompage_business = requests.get(HUFFINTION_POST_ENTERTAIN)
    html_tree = html.fromstring(huffington_hompage_business.text)
    article_urls = html_tree.xpath('//a/@href')
    for home_url in article_urls:
        if  home_url is not None and len(home_url) > 16: 
            if ('http://' not in home_url and 'https://' not in home_url):
                home_url = HUFFINGTON_POST_HOME + home_url
            try:
                article_home = Article(home_url)
                extract_huffington_article(article_home, True, 'news')
            except Exception as e:
                print('Smt wrong when process homepage media  article:  {}'.format(e) + home_url)
            
                        
                        
                        
                
                
    ''' we process homepage world'''
    HUFFINTION_POST_ENTERTAIN= 'http://www.huffingtonpost.com/theworldpost/'
    huffington_hompage_business = requests.get(HUFFINTION_POST_ENTERTAIN)
    html_tree = html.fromstring(huffington_hompage_business.text)
    article_urls = html_tree.xpath('//a/@href')
    for home_url in article_urls:
        if  home_url is not None and len(home_url) > 16: 
            if ('http://' not in home_url and 'https://' not in home_url):
                home_url = HUFFINGTON_POST_HOME + home_url
            try:
                article_home = Article(home_url)
                extract_huffington_article(article_home, True, 'world')
            except Exception as e:
                print('Smt wrong when process homepage world  article:  {}'.format(e) + home_url)
#     
                
                
                
                
                
                
    ''' we process homepage education'''
    HUFFINTION_POST_ENTERTAIN= 'http://www.huffingtonpost.com/education/'
    huffington_hompage_business = requests.get(HUFFINTION_POST_ENTERTAIN)
    html_tree = html.fromstring(huffington_hompage_business.text)
    article_urls = html_tree.xpath('//a/@href')
    for home_url in article_urls:
        if  home_url is not None and len(home_url) > 16: 
            if ('http://' not in home_url and 'https://' not in home_url):
                home_url = HUFFINGTON_POST_HOME + home_url
            try:
                article_home = Article(home_url)
                extract_huffington_article(article_home, True, 'education')
            except Exception as e:
                print('Smt wrong when process homepage education  article:  {}'.format(e) + home_url)
                            
                            
                            
                            
                            
                            
                            
                            
                            
    ''' we process homepage health'''
    HUFFINTION_POST_ENTERTAIN= 'http://www.huffingtonpost.com/healthy-living/'
    huffington_hompage_business = requests.get(HUFFINTION_POST_ENTERTAIN)
    html_tree = html.fromstring(huffington_hompage_business.text)
    article_urls = html_tree.xpath('//a/@href')
    for home_url in article_urls:
        if  home_url is not None and len(home_url) > 16: 
            if ('http://' not in home_url and 'https://' not in home_url):
                home_url = HUFFINGTON_POST_HOME + home_url
            try:
                article_home = Article(home_url)
                extract_huffington_article(article_home, True, 'health')
            except Exception as e:
                print('Smt wrong when process homepage health  article:  {}'.format(e) + home_url)
            
            
            
            
            
            
            
            
                
    ''' we process homepage comedy'''
    HUFFINTION_POST_ENTERTAIN= 'http://www.huffingtonpost.com/comedy/'
    huffington_hompage_business = requests.get(HUFFINTION_POST_ENTERTAIN)
    html_tree = html.fromstring(huffington_hompage_business.text)
    article_urls = html_tree.xpath('//a/@href')
    for home_url in article_urls:
        if  home_url is not None and len(home_url) > 16: 
            if ('http://' not in home_url and 'https://' not in home_url):
                home_url = HUFFINGTON_POST_HOME + home_url
            try:
                article_home = Article(home_url)
                extract_huffington_article(article_home, True, 'entertainment')
            except Exception as e:
                print('Smt wrong when process homepage comedy  article:  {}'.format(e) + home_url)
            
            
                
                
                
                
                
                
    ''' we process homepage style'''
    HUFFINTION_POST_ENTERTAIN= 'http://www.huffingtonpost.com/style/'
    huffington_hompage_business = requests.get(HUFFINTION_POST_ENTERTAIN)
    html_tree = html.fromstring(huffington_hompage_business.text)
    article_urls = html_tree.xpath('//a/@href')
    for home_url in article_urls:
        if  home_url is not None and len(home_url) > 16: 
            if ('http://' not in home_url and 'https://' not in home_url):
                home_url = HUFFINGTON_POST_HOME + home_url
            try:
                article_home = Article(home_url)
                extract_huffington_article(article_home, True, 'style')
            except Exception as e:
                print('Smt wrong when process homepage style  article:  {}'.format(e) + home_url)
                
                
                
                
                
                
                
                
                
    ''' we process homepage travel'''
    HUFFINTION_POST_ENTERTAIN= 'http://www.huffingtonpost.com/travel/'
    huffington_hompage_business = requests.get(HUFFINTION_POST_ENTERTAIN)
    html_tree = html.fromstring(huffington_hompage_business.text)
    article_urls = html_tree.xpath('//a/@href')
    for home_url in article_urls:
        if  home_url is not None and len(home_url) > 16: 
            if ('http://' not in home_url and 'https://' not in home_url):
                home_url = HUFFINGTON_POST_HOME + home_url
            try:
                article_home = Article(home_url)
                extract_huffington_article(article_home, True, 'travel')
            except Exception as e:
                print('Smt wrong when process homepage travel  article:  {}'.format(e) + home_url)
                            
                            
                            
                            
                            
                            
                            
    ''' we process homepage sports'''
    HUFFINTION_POST_ENTERTAIN= 'http://www.huffingtonpost.com/sports/'
    huffington_hompage_business = requests.get(HUFFINTION_POST_ENTERTAIN)
    html_tree = html.fromstring(huffington_hompage_business.text)
    article_urls = html_tree.xpath('//a/@href')
    for home_url in article_urls:
        if  home_url is not None and len(home_url) > 16: 
            if ('http://' not in home_url and 'https://' not in home_url):
                home_url = HUFFINGTON_POST_HOME + home_url
            try:
                article_home = Article(home_url)
                extract_huffington_article(article_home, True, 'sport')
            except Exception as e:
                print('Smt wrong when process homepage sport  article:  {}'.format(e) + home_url)           
                            
                            
                            
                            
                            
                            
    ''' we process homepage'''
    huffington_hompage_business = requests.get(HUFFINGTON_POST_HOME)
    html_tree = html.fromstring(huffington_hompage_business.text)
    article_urls = html_tree.xpath('//a/@href')
    for home_url in article_urls:
        if  home_url is not None and len(home_url) > 16: 
            if ('http://' not in home_url and 'https://' not in home_url):
                home_url = HUFFINGTON_POST_HOME + home_url
            try:
                article_home = Article(home_url)
                extract_huffington_article(article_home, True, 'sport')
            except Exception as e:
                print('Smt wrong when process homepage article:  {}'.format(e) + home_url)       
             
             
             
                            
            
            
            
            
    db_connect.close_database_cont()   
except Exception as e:        
    print('Something went wrong with database: {}'.format(e))
                 
                 
    '''
    =======================================================================================================================================
    =======================================================================================================================================
    ================================================= Huffington Post stop ================================================================
    =======================================================================================================================================
    =======================================================================================================================================
    '''
            
            
            
            
           
         
  
     
     
     
     
     
     
     
     
     
     
     
     
     
  













           
           
           
           
           
           
           
           
           
           
           
           
           
'''
=======================================================================================================================================
=======================================================================================================================================
================================================= Newyork Times start ===============================================================
=======================================================================================================================================
=======================================================================================================================================
''' 
           
newyorktime_category = {'Middle East' : 'world',
                       'Africa' : 'world',
                       'Asia Pacific' : 'world',
                       'Europe' : 'world',
                       'Americas' : 'world',
                       'N.Y. / Region' : 'news',
                       'Politics' : 'politics',
                       'U.S.' : 'news',
                       'Technology' : 'tech',
                       'Economy' : 'business',
                       'The Upshot' : 'news',
                       'Personal Tech' : 'tech',
                       'Business Day' : 'business',
                       'DealBook' : 'business',
                       'Small Business' : 'business',
                       'business' : 'business',
                       'Opinion' : 'opinions',
                       'Science' : 'science',
                       'Energy & Environment' : 'science',
                       'Baseball' : 'sport',
                       'Golf' : 'sport',
                       'Pro Football' : 'sport',
                       'Style' : 'style',
                       'Fashion & Style' : 'style',
                       'Travel' : 'travel',
                       'Commercial Real Estate': 'business',
                       'International Business' : 'business'
                       }
               
newyorktime_except = {}
           
def extract_newyorktime_article(article, is_on_homepage, predifined_category=None):
    #print("url to extract: " + article.url)
    if ('/201' not in article.url or article.url in newyorktime_except or article.url + '/' in newyorktime_except or 'nytimes.com' not in article.url ):
        return
    if (db_connect.is_url_existed(article.url) != -1):
        print("url is already existed")
        url_sharelikecomment_queue.put(article.url, True)
        return
    normalized_url  = article.url.split("?")[0].split("#")[0];
    if ('nytimes.com' not in normalized_url):
        return
    if (normalized_url in newyorktime_except or normalized_url + '/' in newyorktime_except):
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
                
               
               
    try:
        time_string = html_tree.xpath('//meta[@name="ptime"]')[0].attrib['content']
        #time_string = time_string + " UTC-0400"
    except BaseException as dateE:
        print("problem with time: {}".format(dateE))
    try:
        if(time_string is None):
            time_string = html_tree.xpath('//meta[@name="pdate"]')[0].attrib['content']
        #time_string = time_string + " UTC-0400"
    except BaseException as dateE:
        print("problem with time: {}".format(dateE))
    date_time = parse(time_string)
    published_time = calendar.timegm(date_time.utctimetuple())
    print(published_time)
    article.published_time = published_time
    if (article.published_time > time.time()):
            article.published_time = None
               
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
        thumbnail_url = html_tree.xpath('//meta[@name="thumbnail_150"]')[0].attrib['content']
        print(thumbnail_url)
    except Exception as e:
        print('Thumbnaill not found.'.format(e))
    try:
        if(thumbnail_url is None):
            thumbnail_url = html_tree.xpath('//meta[@property="twitter:image"]')[0].attrib['content']
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
               
    if (category_id is not None and category_id in newyorktime_category):
        article.category_id = newyorktime_category.get(category_id)
        print("extracted category: "+ category_id)
               
    if (category_id == "The Upshot"):
        article.category_id = predifined_category
    if (article.category_id is None and predifined_category == 'health'):
        article.category_id = 'health'
    print(article.category_id)
               
               
               
    if (article.published_time is None or article.title is None or article.category_id is None):
        raise Exception("lack fields")
               
               
    # get content
    article.parse()
    text = normalize_text(article.text)
    text_html = true_html.escape(get_text_html_saulify(normalized_url), True)
    normalized_title = normalize_text_nostop(article.title)
            
    ''' insert this article to database, maybe send url to another thread to get count, share, .... or maket it asynchronous'''
    # when no exception, we insert to database
    try:
        print(db_connect.insert_article3(normalized_url, article.title, newyorktimes_source_id, 
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
      'start get articles from newyork times' +
      '...................................................\n' +
      '...................................................\n'
      )
try:
    db_connect = IIIDatbaseConnection()
    db_connect.init_database_cont() 
           
               
               
               
    ''' we process world articles'''
    NEWYORK_TIME_PAGE = 'http://www.nytimes.com/pages/world/index.html'
    newyork_time_page = requests.get(NEWYORK_TIME_PAGE)
    html_tree = html.fromstring(newyork_time_page.text)
    article_urls = html_tree.xpath('//a/@href')
    for home_url in article_urls:
        if  home_url is not None and len(home_url) > 16: 
            if ('http://' not in home_url and 'https://' not in home_url):
                home_url = NEWYORKTIME_HOME + home_url
            try:
                article_home = Article(home_url)
                extract_newyorktime_article(article_home, True, 'world')
            except Exception as e:
                print('Smt wrong when process newyork time world article:  {}'.format(e) + home_url)
                            
                            
                            
                            
                
                
                
    ''' we process usa articles'''
    NEWYORK_TIME_PAGE = 'http://www.nytimes.com/pages/national/index.html'
    newyork_time_page = requests.get(NEWYORK_TIME_PAGE)
    html_tree = html.fromstring(newyork_time_page.text)
    article_urls = html_tree.xpath('//a/@href')
    for home_url in article_urls:
        if  home_url is not None and len(home_url) > 16: 
            if ('http://' not in home_url and 'https://' not in home_url):
                home_url = NEWYORKTIME_HOME + home_url
            try:
                article_home = Article(home_url)
                extract_newyorktime_article(article_home, True, 'news')
            except Exception as e:
                print('Smt wrong when process newyork time usa article:  {}'.format(e) + home_url)
                            
                            
                            
                
                
    ''' we process polictics articles'''
    NEWYORK_TIME_PAGE = 'http://www.nytimes.com/pages/politics/index.html'
    newyork_time_page = requests.get(NEWYORK_TIME_PAGE)
    html_tree = html.fromstring(newyork_time_page.text)
    article_urls = html_tree.xpath('//a/@href')
    for home_url in article_urls:
        if  home_url is not None and len(home_url) > 16: 
            if ('http://' not in home_url and 'https://' not in home_url):
                home_url = NEWYORKTIME_HOME + home_url
            try:
                article_home = Article(home_url)
                extract_newyorktime_article(article_home, True,'politics')
            except Exception as e:
                print('Smt wrong when process newyork time polictics article:  {}'.format(e) + home_url)           
                            
                            
                        
                        
                        
                        
    ''' we process newyork religion articles'''
    NEWYORK_TIME_PAGE = 'http://www.nytimes.com/pages/nyregion/index.html'
    newyork_time_page = requests.get(NEWYORK_TIME_PAGE)
    html_tree = html.fromstring(newyork_time_page.text)
    article_urls = html_tree.xpath('//a/@href')
    for home_url in article_urls:
        if  home_url is not None and len(home_url) > 16: 
            if ('http://' not in home_url and 'https://' not in home_url):
                home_url = NEWYORKTIME_HOME + home_url
            try:
                article_home = Article(home_url)
                extract_newyorktime_article(article_home, True,'news')
            except Exception as e:
                print('Smt wrong when process newyork religion article:  {}'.format(e) + home_url)     
            
                            
                            
                            
                            
                            
    ''' we process newyork business articles'''
    NEWYORK_TIME_PAGE = 'http://www.nytimes.com/pages/business/index.html'
    newyork_time_page = requests.get(NEWYORK_TIME_PAGE)
    html_tree = html.fromstring(newyork_time_page.text)
    article_urls = html_tree.xpath('//a/@href')
    for home_url in article_urls:
        if  home_url is not None and len(home_url) > 16: 
            if ('http://' not in home_url and 'https://' not in home_url):
                home_url = NEWYORKTIME_HOME + home_url
            try:
                article_home = Article(home_url)
                extract_newyorktime_article(article_home, True,'business')
            except Exception as e:
                print('Smt wrong when process newyork business article:  {}'.format(e) + home_url)                 
                            
                            
                           
                           
                           
                           
    ''' we process newyork opinions articles'''
    NEWYORK_TIME_PAGE = 'http://www.nytimes.com/pages/opinion/index.html'
    newyork_time_page = requests.get(NEWYORK_TIME_PAGE)
    html_tree = html.fromstring(newyork_time_page.text)
    article_urls = html_tree.xpath('//a/@href')
    for home_url in article_urls:
        if  home_url is not None and len(home_url) > 16: 
            if ('http://' not in home_url and 'https://' not in home_url):
                home_url = NEWYORKTIME_HOME + home_url
            try:
                article_home = Article(home_url)
                extract_newyorktime_article(article_home, True,'opinions')
            except Exception as e:
                print('Smt wrong when process newyork opinions article:  {}'.format(e) + home_url) 
                           
                           
            
            
            
    ''' we process newyork tech articles'''
    NEWYORK_TIME_PAGE = 'http://www.nytimes.com/pages/technology/index.html'
    newyork_time_page = requests.get(NEWYORK_TIME_PAGE)
    html_tree = html.fromstring(newyork_time_page.text)
    article_urls = html_tree.xpath('//a/@href')
    for home_url in article_urls:
        if  home_url is not None and len(home_url) > 16: 
            if ('http://' not in home_url and 'https://' not in home_url):
                home_url = NEWYORKTIME_HOME + home_url
            try:
                article_home = Article(home_url)
                extract_newyorktime_article(article_home, True,'tech')
            except Exception as e:
                print('Smt wrong when process newyork tech article:  {}'.format(e) + home_url) 
            
            
            
            
            
    ''' we process newyork science articles'''
    NEWYORK_TIME_PAGE = 'http://www.nytimes.com/pages/science/index.html'
    newyork_time_page = requests.get(NEWYORK_TIME_PAGE)
    html_tree = html.fromstring(newyork_time_page.text)
    article_urls = html_tree.xpath('//a/@href')
    for home_url in article_urls:
        if  home_url is not None and len(home_url) > 16: 
            if ('http://' not in home_url and 'https://' not in home_url):
                home_url = NEWYORKTIME_HOME + home_url
            try:
                article_home = Article(home_url)
                extract_newyorktime_article(article_home, True,'science')
            except Exception as e:
                print('Smt wrong when process newyork science article:  {}'.format(e) + home_url) 
                           
               
               
               
               
               
    ''' we process newyork travel articles'''
    NEWYORK_TIME_PAGE = 'http://www.nytimes.com/pages/travel/index.html'
    newyork_time_page = requests.get(NEWYORK_TIME_PAGE)
    html_tree = html.fromstring(newyork_time_page.text)
    article_urls = html_tree.xpath('//a/@href')
    for home_url in article_urls:
        if  home_url is not None and len(home_url) > 16: 
            if ('http://' not in home_url and 'https://' not in home_url):
                home_url = NEWYORKTIME_HOME + home_url
            try:
                article_home = Article(home_url)
                extract_newyorktime_article(article_home, True,'travel')
            except Exception as e:
                print('Smt wrong when process newyork travel article:  {}'.format(e) + home_url) 
               
               
               
               
               
    ''' we process newyork style articles'''
    NEWYORK_TIME_PAGE = 'http://www.nytimes.com/pages/fashion/index.html'
    newyork_time_page = requests.get(NEWYORK_TIME_PAGE)
    html_tree = html.fromstring(newyork_time_page.text)
    article_urls = html_tree.xpath('//a/@href')
    for home_url in article_urls:
        if  home_url is not None and len(home_url) > 16: 
            if ('http://' not in home_url and 'https://' not in home_url):
                home_url = NEWYORKTIME_HOME + home_url
            try:
                article_home = Article(home_url)
                extract_newyorktime_article(article_home, True,'style')
            except Exception as e:
                print('Smt wrong when process newyork style article:  {}'.format(e) + home_url) 
               
               
               
               
               
               
    ''' we process newyork health articles'''
    NEWYORK_TIME_PAGE = 'http://www.nytimes.com/pages/health/index.html'
    newyork_time_page = requests.get(NEWYORK_TIME_PAGE)
    html_tree = html.fromstring(newyork_time_page.text)
    article_urls = html_tree.xpath('//a/@href')
    for home_url in article_urls:
        if  home_url is not None and len(home_url) > 16: 
            if ('http://' not in home_url and 'https://' not in home_url):
                home_url = NEWYORKTIME_HOME + home_url
            try:
                article_home = Article(home_url)
                extract_newyorktime_article(article_home, True,'health')
            except Exception as e:
                print('Smt wrong when process newyork health article:  {}'.format(e) + home_url) 
               
               
                
                           
                           
                           
                           
           
    db_connect.close_database_cont()   
except Exception as e:        
    print('Something went wrong with database: {}'.format(e))
                    
    '''
    =======================================================================================================================================
    =======================================================================================================================================
    ================================================= Newyork Times  stop  ================================================================
    =======================================================================================================================================
    =======================================================================================================================================
    '''
          
          
          
          
          
          
          
          
          
         
         
         
         
         
         
         
'''
=======================================================================================================================================
=======================================================================================================================================
================================================= NBC news start ===============================================================
=======================================================================================================================================
=======================================================================================================================================
''' 
         
             
             
nbc_category = {'us-news' : 'news',
                'news' : 'news',
                'local' : 'news',
                'world' : 'world',
                'latin-america' : 'world',
                'europe' : 'world',
                'latin-america' : 'world',
                'latin-america' : 'world',
                'politics' : 'politics',
                'health' : 'health',
                'tech': 'tech',
                'science' : 'science',
                'pop-culture': 'entertainment',
                'business' : 'business',
                'education' : 'education',
                'crime-courts' : 'news',
                'investigations' : 'news',
                }
         
             
nbc_except = {'http://www.nbcnews.com/feature/3rd-block','http://www.nbcnews.com/news/us-news/nbc-affiliates-n19981',
              'http://www.nbcnews.com/feature/30-seconds-to-know' }    
         
nbc_home_pages = {'http://www.nbcnews.com/news/us-news' : 'news',
                  'http://www.nbcnews.com/news/world' : 'world',
                  'http://www.nbcnews.com/politics' : 'politics',
                  'http://www.nbcnews.com/health' : 'health',
                  'http://www.nbcnews.com/tech' : 'tech',
                  'http://www.nbcnews.com/science' : 'science',
                  'http://www.nbcnews.com/pop-culture' : 'entertainment',
                  'http://www.nbcnews.com/business' : 'business',
                  'http://www.nbcnews.com/news/investigations' : 'news',
                  'http://www.nbcnews.com/pop-culture/lifestyle' : 'life',
                  'http://www.nbcnews.com/news/education' : 'education',
                  'http://www.nbcnews.com/' : None,
                           
                  }    
             
             
             
             
             
def extract_nbcnews_article(article, is_on_homepage, predifined_category=None):
             
    if (  article.url in nbc_except or article.url + '/' in nbc_except or 'nbc' not in article.url or "/media-kit/" in article.url): 
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
    if ('nbc' not in normalized_url):
        return
    if (normalized_url in nbc_except or normalized_url + '/' in nbc_except):
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
    date_time = None
              
    article.download()
    html_tree = html.fromstring(article.html)
              
             
             
    try:
        time_string = html_tree.xpath('//time[@itemprop="datePublished"]')[0].attrib['datetime']
        print("extracted time: " + time_string)
        date_time = parse(time_string +  " -7:00")
        #time_string = time_string + " UTC-0400"
    except BaseException as dateE:
        print("problem with time: {}".format(dateE))
                 
    try:
        if (time_string is None and date_time is None):
            time_string = html_tree.xpath('//div[@class="dateline"]/text()')[1]
            if (time_string is not None):
                time_string = time_string.replace ("Published at ", "")
                time_string = time_string.replace ("on ", "")
                print("extracted time: " + time_string)
                date_time = parse(time_string)
            #time_string = time_string + " UTC-0400"
    except BaseException as dateE:
        print("problem with time: {}".format(dateE))
                     
    try:
        if (time_string is None and date_time is None):
            time_string = html_tree.xpath('//div[@class="dateline bottom"]/text()')[1]
            if (time_string is not None):
                time_string = time_string.replace ("Published at ", "")
                time_string = time_string.replace ("on ", "")
                print("extracted time: " + time_string)
                date_time = parse(time_string)
            #time_string = time_string + " UTC-0400"
    except BaseException as dateE:
        print("problem with time: {}".format(dateE))
             
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
        print('')    
    try:
        if(short_description is None):
            short_description = html_tree.xpath('//meta[@property="og:description"]')[0].attrib['content']
            print(short_description)
    except Exception as e:
        print('Description not found again'.format(e))
    article.short_description = short_description
             
             
    # get category
    try:
        category_group = re.search('nbcnews\.com/((?:[^/])*)/', article.url)
        category_id = category_group.group(1)
        if (category_id == 'news'):
            sub_group = re.search('news/((?:[^/])*)/', article.url)
            if(sub_group is not None and sub_group.group(1) is not None):
                category_id = sub_group.group(1)
        print ("category on url: " + category_id)
    except Exception as e:
        print('')
                 
    if ('nbcnewyork.com/news/' in article.url ):
        category_id = 'news'
                 
    if (category_id is not None and category_id in nbc_category):
        article.category_id = nbc_category.get(category_id)
                 
    if (category_id == 'watch'):
        article.category_id = predifined_category
    print("extracted category: "+ article.category_id)
             
             
             
             
             
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
        print(db_connect.insert_article3(normalized_url, article.title, nbc_source_id, 
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
      'start get articles from nbcNews' +
      '...................................................\n' +
      '...................................................\n'
      )
try:
    db_connect = IIIDatbaseConnection()
    db_connect.init_database_cont()     
             
             
             
    ''' we process homepage'''
    for home_page in nbc_home_pages:
        print("extracting: " + home_page)
        nbc_page = requests.get(home_page)
        html_tree = html.fromstring(nbc_page.text)
        article_urls = html_tree.xpath('//a/@href')
        for home_url in article_urls:
            if  home_url is not None and len(home_url) > 16: 
                if ('http://' not in home_url and 'https://' not in home_url):
                    home_url = NBC_HOMEPAGE + home_url
                try:
                    article_home = Article(home_url)
                    extract_nbcnews_article(article_home, True, nbc_home_pages.get(home_page))
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
