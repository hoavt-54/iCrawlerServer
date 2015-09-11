'''
Created on May 31, 2015

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

CNBC_HOME = 'http://www.cnbc.com'


cnbc_source_id = "cnbc"

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
================================================= cnbc news start ===============================================================
=======================================================================================================================================
=======================================================================================================================================
''' 
          
              
              
cnbc_category = {'US: News' : 'news',
                'CNBC Explains' : 'news',
                'U.S. News' : 'news',
                'Europe: News' : 'world',
                'White House' : 'politics',
                'Politics' : 'politics',
                'Congress' : 'politics',
                'Law' : 'politics',
                'Taxes' : 'politics',
                'Elections' : 'politics',
                'Health Care' : 'politics',
                'Kudlow&#039;s Corner' : 'politics',
                'The Fed' : 'politics',
                'Mergers and Acquisitions' : 'business',
                'Entertainment' : 'entertainment',
                'Technology' : 'tech',
                'Mobile' : 'tech',
                'Social Media' : 'tech',
                'Enterprise' : 'tech',
                'Gaming' : 'tech',
                'Cybersecurity' : 'tech',
                'Code Conference' : 'tech',
                'Tech Drivers' : 'tech',
                'Tech Transformers' : 'tech',
                'Natural Disasters' : 'science',
                'Sports' : 'sport',
                'Lawsuits' : 'news',
                'Weather' : 'news',
                'Personal Finance' : 'business',
                'Airlines' : 'news',
                'Autos' : 'news',
                'Catalog Retail' : 'business',
                'US Economy' : 'business',
                'Utilities' : 'news',
                'Energy' : 'business',
                'Wealth' : 'business',
                'Oil and Gas' : 'business',
                'Real Estate' : 'business',
                'Housing' : 'business',
                'Mortgages' : 'business',
                'Construction' : 'business',
                'Commercial and Real Estate' : 'business',
                'Finance' :'business',
                'Bank' : 'business',
                'Investing' : 'business',
                'Wall Street' : 'business',
                'Hedge Funds' : 'business',
                'Venture Capital' : 'business',
                'Trading Nation' : 'business',
                'Advisor Insight' : 'business',
                'Age-based Investing' : 'life',
                'FA Career Planner' : 'life',
                'Straight Talk' : 'life',
                'Retirement' : 'life',
                'Savings' : 'life',
                'Career' : 'life',
                'College' : 'life',
                'small business week' : 'business',
                'Small Business' : 'business',
                'Road to Iconic' : 'business',
                'Labor Unions' : 'business',
                'Restaurants' : 'business',
                'Consumer Staples' : 'business',
                
                
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
                'meet-the-press' : 'politics',
                'first-read' : 'politics',
                'nightly-news' : 'news'
                }
          
              
cnbc_except = {'http://www.cnbc.com/id/10000664', 'http://www.cnbc.com/id/20910258', 
               'http://www.cnbc.com/id/10000108' , 'http://www.cnbc.com/id/10000115', 
               'http://www.cnbc.com/id/15837362', 'http://www.cnbc.com/id/10000101', 
               'http://www.cnbc.com/id/10000826', 'http://www.cnbc.com/id/15839135',
               'http://www.cnbc.com/id/19836768', 'http://www.cnbc.com/id/10001150',
               'http://www.cnbc.com/id/10000110', 'http://www.cnbc.com/id/10001054',
               'http://www.cnbc.com/id/10000101', 'http://www.cnbc.com/id/10000113',
               'http://www.cnbc.com/id/10000116', 'http://www.cnbc.com/id/100370673',
               'http://www.cnbc.com/id/16903222', 'http://www.cnbc.com/id/19832390',
               'http://www.cnbc.com/id/19794221', 'http://www.cnbc.com/id/15839121',
               'http://www.cnbc.com/id/17689937', 'http://www.cnbc.com/id/100003242',
               'http://www.cnbc.com/id/10000527', 'http://www.cnbc.com/id/10000528',
               'http://www.cnbc.com/id/15839215', 'http://www.cnbc.com/id/15839171',
               'http://www.cnbc.com/id/15839178', 'http://www.cnbc.com/id/15839203',
               'http://www.cnbc.com/id/15839193', 'http://www.cnbc.com/id/10000946',
               'http://www.cnbc.com/id/15839069', 'http://www.cnbc.com/id/102356916',
               'http://www.cnbc.com/id/100646281', 'http://www.cnbc.com/id/21324812',
               'http://www.cnbc.com/id/41585735', 'http://www.cnbc.com/id/15839076',
               'http://www.cnbc.com/id/15839074', 'http://www.cnbc.com/id/19854910',
               'http://www.cnbc.com/id/10000066', 'http://www.cnbc.com/id/100397778',
               'http://www.cnbc.com/id/101004656', 'http://www.cnbc.com/id/46328872',
               'http://www.cnbc.com/id/100807029', 'http://www.cnbc.com/id/44877279',
               'http://www.cnbc.com/id/45108356', 'http://www.cnbc.com/id/45107907',
               'http://www.cnbc.com/id/45108438', 'http://www.cnbc.com/id/101625231',
               'http://www.cnbc.com/id/15839263', 'http://www.cnbc.com/id/100004038',
               'http://www.cnbc.com/id/100616801', 'http://www.cnbc.com/id/100004036',
               'http://www.cnbc.com/id/100004034', 'http://www.cnbc.com/id/100004035',
               'http://www.cnbc.com/id/100004032', 'http://www.cnbc.com/id/100004033',
               'http://www.cnbc.com/id/15837856', 'http://www.cnbc.com/id/15837856',
               'http://www.cnbc.com/id/15838789', 'http://www.cnbc.com/id/15838668',
               'http://www.cnbc.com/id/15837872', 'http://www.cnbc.com/id/10000113',
               'http://www.cnbc.com/id/101520028', 'http://www.cnbc.com/id/10000664',
               'http://www.cnbc.com/id/19854910/page/2', 'http://www.cnbc.com/id/19854910/page/400',
               'http://www.cnbc.com/id/20910258/page/161', 'http://www.cnbc.com/id/20910258/page/2',
               'http://www.cnbc.com/id/10000664/page/151', 'http://www.cnbc.com/id/10000664/page/2',
               'http://www.cnbc.com/id/10000113/page/174', 'http://www.cnbc.com/id/10000113/page/2',
               'http://www.cnbc.com/id/10000876', 'http://www.cnbc.com/id/10000958', 
               'http://www.cnbc.com/id/10000293', 'http://www.cnbc.com/id/10000621',
               'http://www.cnbc.com/id/102334827', 'http://www.cnbc.com/id/10001079',
               'http://www.cnbc.com/id/10000887', 'http://www.cnbc.com/id/10000109',
               'http://www.cnbc.com/id/10001075', 'http://www.cnbc.com/id/10001062',
               'http://www.cnbc.com/id/100727362', 
                }    
          
cnbc_home_pages = { 'http://www.cnbc.com/' : None,
                   'http://www.cnbc.com/id/10000113' : 'politics',
                   'http://www.cnbc.com/id/10000664' : 'business',
                   'http://www.cnbc.com/id/20910258' : 'business',
                   'http://www.cnbc.com/id/19854910' : 'tech',
                  }    
              
              
              
              
              
def extract_cnbcnews_article(article, is_on_homepage, predifined_category=None):
    
    if (  article.url in cnbc_except  or 'cnbc.com/id/' not in article.url ): 
        return
    if (not hasNumbers(article.url)):
        return
    #print("url to extract: " + article.url)
    if (db_connect.is_url_existed(article.url) != -1):
        print("url is already existed")
        url_sharelikecomment_queue.put(article.url, True)
        return
    normalized_url  = article.url.split("?")[0].split("#")[0].split("&")[0];
    if ('cnbc.com/id/' not in normalized_url):
        return
    if (normalized_url in cnbc_except or normalized_url + '/' in cnbc_except):
        return
    if (db_connect.is_url_existed(normalized_url) != -1):
        print("url is already existed")
        url_sharelikecomment_queue.put(normalized_url, True)
        return
    print("\n")
    print("url: " + normalized_url)
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
        
    try:
        if (time_string is None):
            time_string = html_tree.xpath('//meta[@itemprop="dateCreated"]')[0].attrib['content']
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
        print('Thumbnaill not found again {}'.format(e))
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
        category_id = html_tree.xpath('//meta[@property="article:section"]')[0].attrib['content']
    except Exception as e:
        print('Category not found'.format(e))
                  
    if (category_id is not None and category_id in cnbc_category):
        article.category_id = cnbc_category.get(category_id)
                  
    print("extracted category: "+ article.category_id)
              
              
              
              
              
    if (article.published_time is None or article.title is None or article.category_id is None):
        raise Exception("missing fields ")
              
              
              
    article.source_name = "CNBC"          
    # get content
    article.parse()
    text = normalize_text(article.text)
    text_html = true_html.escape(get_text_html_saulify(normalized_url), True)
    normalized_title = normalize_text_nostop(article.title)
    article.source_id = cnbc_source_id
            
    ''' insert this article to database, maybe send url to another thread to get count, share, .... or maket it asynchronous'''
    # when no exception, we insert to database
    try:
        article.id = db_connect.insert_article3(normalized_url, article.title, cnbc_source_id, 
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
      'start get articles from cnbcNews' +
      '...................................................\n' +
      '...................................................\n'
      )
try:
    db_connect = IIIDatbaseConnection()
    db_connect.init_database_cont()     
              
              
              
    ''' we process homepage'''
    for home_page in cnbc_home_pages:
        print("extracting: " + home_page)
        cnbc_page = requests.get(home_page)
        html_tree = html.fromstring(cnbc_page.text)
        article_urls = html_tree.xpath('//a/@href')
        for home_url in article_urls:
            if  home_url is not None: 
                if ('http://' not in home_url and 'https://' not in home_url):
                        home_url = CNBC_HOME + home_url
                try:
                    article_home = Article(home_url)
                    extract_cnbcnews_article(article_home, True, cnbc_home_pages.get(home_page))
                except Exception as e:
                    print('Smt wrong when process homepage' + home_page +  'article:  {}'.format(e) + home_url)
              
              
              
              
              
              
              
              
           
    db_connect.close_database_cont()   
except Exception as e:        
    print('Something went wrong with database: {}'.format(e))    
              
              
          
'''
=======================================================================================================================================
=======================================================================================================================================
================================================= cnbc news stop ===============================================================
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