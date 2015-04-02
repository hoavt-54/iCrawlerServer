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
from newspaper.article import Article
import os.path
from pytz import timezone
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


cnn_except = {'http://edition.cnn.com', 'http://edition.cnn.com/world',
              'http://edition.cnn.com/sport', 'http://edition.cnn.com/tech',
               'http://edition.cnn.com/showbiz', 'http://edition.cnn.com/specials/world/style'
               'http://travel.cnn.com/', 'http://money.cnn.com/INTERNATIONAL/',
               'http://edition.cnn.com/regions', 'http://edition.cnn.com/us',
               'http://edition.cnn.com/china', 'http://edition.cnn.com/africa' ,
               'http://edition.cnn.com/americas', 'http://edition.cnn.com/asia',
               'http://edition.cnn.com/europe', 'http://edition.cnn.com/middle-east',
               'http://edition.cnn.com/videos', 'http://edition.cnn.com/specials/stories-worth-watching-video',
               'http://edition.cnn.com/tv', 'http://edition.cnn.com/tv/shows', 'http://edition.cnn.com/tv/schedule/europe',
               'http://edition.cnn.com/specials', 'http://edition.cnn.com/opinions',
                'http://edition.cnn.com/specials/profiles', 'http://edition.cnn.com/more',
                'http://edition.cnn.com/interactive/mobile/', 'http://edition.cnn.com/tools/',
                'http://arabic.cnn.com/', 'http://cnnespanol.cnn.com/',
                'http://mexico.cnn.com/', 'http://www.facebook.com/cnninternational',
                'http://twitter.com/cnni', 'http://plus.google.com/+CNNInternational',
                'http://edition.cnn.com/WEATHER', 'http://edition.cnn.com/specials/photos',
                'http://edition.cnn.com/specials/cnn-heroes', 'http://thecnnfreedomproject.blogs.cnn.com/',
                'http://www.ireport.com/', 'http://edition.cnn.com/specials/tv/anchors-and-reporters',
                'http://edition.cnn.com/cookie', 'http://edition.cnn.com/',
                'http://edition.cnn.com/login.html', 'http://edition.cnn.com/mycnn',
                'http://edition.cnn.com/entertainment', 'http://edition.cnn.com/specials/world/style',
                'http://edition.cnn.com//travel.cnn.com', 'http://edition.cnn.com//money.cnn.com/INTERNATIONAL/',
                'http://edition.cnn.com/specials/international-video-landing/feature-show-videos',
                'http://edition.cnn.com/specials/international-video-landing/videos-espanol',
                'http://edition.cnn.com/weather', 'http://edition.cnn.com//arabic.cnn.com', 
                'http://edition.cnn.com//ireport.cnn.com', 'http://edition.cnn.com//cnnespanol.cnn.com',
                'http://edition.cnn.com//mexico.cnn.com', 'http://edition.cnn.com//www.facebook.com/cnninternational',
                'http://edition.cnn.com//twitter.com/cnni', 'http://edition.cnn.com//plus.google.com/+CNNInternational',
                'http://edition.cnn.com/specials/impact-your-world', 'http://edition.cnn.com//thecnnfreedomproject.blogs.cnn.com',
                'http://edition.cnn.com//mexico.cnn.com', 'http://edition.cnn.com//www.facebook.com/cnninternational',
                'http://edition.cnn.com//twitter.com/cnni', 'http://edition.cnn.com//plus.google.com/+CNNInternational',
                'http://edition.cnn.com/specials/impact-your-world', 'http://edition.cnn.com//thecnnfreedomproject.blogs.cnn.com',
                'http://www.turner.com', 'http://commercial.cnn.com', 'http://www.turner.com/careers',
                'http://cnnnewsource.com', 'http://travel.cnn.com/', 
                }
def extract_cnn_article (article, is_on_homepage, predifined_category=None):
    if ('/201' not in article.url or article.url in cnn_except):
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
    article.download()
    article.category_id = ''
    if (predifined_category is not None):
        article.category_id = predifined_category
    article.thumbnail_url = ''
    html_tree = html.fromstring(article.html)
    
    ''' money cnn format different '''
    if 'http://money.cnn.com' in normalized_url:
        time_string = html_tree.xpath('//meta[@name="date"]')[0].attrib['content']
        print("extracted time: " + time_string)
        datetime_obj = datetime.strptime(time_string, "%Y-%m-%d %H:%M:%S")
        datetime_obj_tz = datetime_obj.replace(tzinfo=timezone('EST'))
        article.update_time = calendar.timegm(datetime_obj_tz.utctimetuple())
        if (article.update_time > time.time()):
            article.update_time = None
        print("time saved: ")
        print(datetime.fromtimestamp(article.update_time, pytz.timezone('America/Los_Angeles')))
        article.category_id = 'business'
    else:
        time_string = html_tree.xpath('//meta[@property="og:pubdate"]')[0].attrib['content']
        date_time = parse(time_string)
        print("extracted time: " + time_string)
        article.update_time = calendar.timegm(date_time.utctimetuple())
        if (article.update_time > time.time()):
            article.update_time = None
        print("time saved: ")
        print(datetime.fromtimestamp(article.update_time))
        
    
    print(article.update_time)
    title = html_tree.xpath('//meta[@property="og:title"]')[0].attrib['content']
    article.title = title.split(" - CNN.com")[0]
    print(article.title)
    
    try:
        article.thumbnail_url = html_tree.xpath('//meta[@property="og:image"]')[0].attrib['content']
        print(article.thumbnail_url)
    except Exception as e:
        print('Thumbnaill not found once.'.format(e))
        article.thumbnail_url = article.top_img
        print(article.thumbnail_url)
    article.short_description = html_tree.xpath('//meta[@property="og:description"]')[0].attrib['content']
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
    
    if (article.update_time is None or article.title is None or article.category_id is None):
        raise Exception("")
    print(article.category_id)
    
    ''' get clean text content '''
    text_html = true_html.escape(get_text_html_saulify(normalized_url), True)
    article.parse()
    text = normalize_text(article.text)
    normalized_title = normalize_text_nostop(article.title)
    ''' insert this article to database, maybe send url to another thread to get count, share, .... or maket it asynchronous'''
    # when no exception, we insert to database
    print(db_connect.insert_article3(normalized_url, article.title, cnn_source_id, article.category_id, 
                                     False, is_on_homepage, article.update_time, article.thumbnail_url, article.short_description, USA, text_html, text, normalized_title))
    
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
Here we travel all source article by using article. Take 'CACHING' into account later 
'''
try:
    db_connect = IIIDatbaseConnection()
    db_connect.init_database_cont()
    print('Reading CNN source ...')
                   
              
    ''' we process homepage sport'''
    CNN_HOMPAGE_SPORT = 'http://edition.cnn.com/sport'
    cnn_homepage_sport = requests.get(CNN_HOMPAGE_SPORT)
    html_tree = html.fromstring(cnn_homepage_sport.text)
    article_urls = html_tree.xpath('//a/@href')
    for home_url in article_urls:
        if  home_url is not None and len(home_url) > 16: 
            if ('http://' not in home_url and 'https://' not in home_url):
                home_url = CNN_HOMPAGE_ROOT + home_url
            try:
                article_home = Article(home_url)
                extract_cnn_article(article_home, True, cnn_category.get('sport'))
            except Exception as e:
                print('Smt wrong when process homepage sport  article:  {}'.format(e) + home_url)
                    
                     
    '''=======we process homepage technology==========='''
    CNN_HOMPAGE_TECH = 'http://edition.cnn.com/tech'
    cnn_homepage_tech = requests.get(CNN_HOMPAGE_TECH)
    html_tree = html.fromstring(cnn_homepage_tech.text)
    article_urls = html_tree.xpath('//a/@href')
    for home_url in article_urls:
        if  home_url is not None and len(home_url) > 16: 
            if ('http://' not in home_url and 'https://' not in home_url):
                home_url = CNN_HOMPAGE_ROOT + home_url
            try:
                article_home = Article(home_url)
                extract_cnn_article(article_home, True, cnn_category.get('tech'))
            except Exception as e:
                print('Smt wrong when process homepage technology article:  {}'.format(e) + home_url)
                     
         
         
         
    '''=======we process homepage living==========='''
    CNN_HOMPAGE_TECH = 'http://www.cnn.com/living'
    cnn_homepage_tech = requests.get(CNN_HOMPAGE_TECH)
    html_tree = html.fromstring(cnn_homepage_tech.text)
    article_urls = html_tree.xpath('//a/@href')
    for home_url in article_urls:
        if  home_url is not None and len(home_url) > 16: 
            if ('http://' not in home_url and 'https://' not in home_url):
                home_url = CNN_HOMPAGE_ROOT + home_url
            try:
                article_home = Article(home_url)
                extract_cnn_article(article_home, True, 'life')
            except Exception as e:
                print('Smt wrong when process homepage life article:  {}'.format(e) + home_url)
                     
                     
                     
    '''we process homepage entertainment'''
    CNN_HOMPAGE_ENTERTAIN = 'http://edition.cnn.com/entertainment'
    cnn_homepage_entertain = requests.get(CNN_HOMPAGE_ENTERTAIN)
    html_tree = html.fromstring(cnn_homepage_entertain.text)
    article_urls = html_tree.xpath('//a/@href')
    for home_url in article_urls:
        if  home_url is not None and len(home_url) > 16: 
            if ('http://' not in home_url and 'https://' not in home_url):
                home_url = CNN_HOMPAGE_ROOT + home_url
            try:
                article_home = Article(home_url)
                extract_cnn_article(article_home, True, cnn_category.get('entertainment'))
            except Exception as e:
                print('Smt wrong when process homepage entertainment article:  {}'.format(e) + home_url)
                     
                     
                     
                       
                     
    '''we process homepage travel'''
    CNN_HOMPAGE_TRAVEL = 'http://travel.cnn.com/'
    cnn_homepage_travel = requests.get(CNN_HOMPAGE_TRAVEL)
    html_tree = html.fromstring(cnn_homepage_travel.text)
    article_urls = html_tree.xpath('//a/@href')
    for home_url in article_urls:
        if  home_url is not None and len(home_url) > 16: 
            home_url = home_url
            try:
                article_home = Article(home_url)
                extract_cnn_article(article_home, True, cnn_category.get('travel'))
            except Exception as e:
                print('Smt wrong when process homepage travel article:  {}'.format(e) + home_url)
                     
                     
                     
                     
    '''we process homepage opinion'''
    CNN_HOMPAGE_OPINIONS = 'http://edition.cnn.com/opinions'
    cnn_homepage_opinion = requests.get(CNN_HOMPAGE_OPINIONS)
    html_tree = html.fromstring(cnn_homepage_opinion.text)
    article_urls = html_tree.xpath('//a/@href')
    for home_url in article_urls:
        if  home_url is not None and len(home_url) > 16: 
            if ('http://' not in home_url and 'https://' not in home_url):
                home_url = CNN_HOMPAGE_ROOT + home_url
            try:
                article_home = Article(home_url)
                extract_cnn_article(article_home, True, cnn_category.get('opinions'))
            except Exception as e:
                print('Smt wrong when process homepage opinion article:  {}'.format(e) + home_url)
                     
                 
                  
                  
                  
    '''we process homepage polictics'''
    CNN_HOMPAGE_POLITICS = 'http://www.cnn.com/politics'
    cnn_homepage_opinion = requests.get(CNN_HOMPAGE_POLITICS)
    html_tree = html.fromstring(cnn_homepage_opinion.text)
    article_urls = html_tree.xpath('//a/@href')
    for home_url in article_urls:
        if  home_url is not None and len(home_url) > 16: 
            if ('http://' not in home_url and 'https://' not in home_url):
                home_url = CNN_HOMPAGE_ROOT + home_url
            try:
                article_home = Article(home_url)
                extract_cnn_article(article_home, True, cnn_category.get('politics'))
            except Exception as e:
                print('Smt wrong when process homepage polictics article:  {}'.format(e) + home_url)
                  
                  
                  
                  
                  
    '''we process homepage usa'''
    CNN_HOMPAGE_POLITICS = 'http://www.cnn.com/us'
    cnn_homepage_opinion = requests.get(CNN_HOMPAGE_POLITICS)
    html_tree = html.fromstring(cnn_homepage_opinion.text)
    article_urls = html_tree.xpath('//a/@href')
    for home_url in article_urls:
        if  home_url is not None and len(home_url) > 16: 
            if ('http://' not in home_url and 'https://' not in home_url):
                home_url = CNN_HOMPAGE_ROOT + home_url
            try:
                article_home = Article(home_url)
                extract_cnn_article(article_home, True, cnn_category.get('us'))
            except Exception as e:
                print('Smt wrong when process homepage usa article:  {}'.format(e) + home_url)
                 
                 
                 
                 
                 
                 
    '''we process homepage world'''
    CNN_HOMPAGE_POLITICS = 'http://edition.cnn.com/world'
    cnn_homepage_opinion = requests.get(CNN_HOMPAGE_POLITICS)
    html_tree = html.fromstring(cnn_homepage_opinion.text)
    article_urls = html_tree.xpath('//a/@href')
    for home_url in article_urls:
        if  home_url is not None and len(home_url) > 16: 
            if ('http://' not in home_url and 'https://' not in home_url):
                home_url = CNN_HOMPAGE_ROOT + home_url
            try:
                article_home = Article(home_url)
                extract_cnn_article(article_home, True, cnn_category.get('world'))
            except Exception as e:
                print('Smt wrong when process homepage usa article:  {}'.format(e) + home_url)
                 
                   
                   
    '''
    we process homepage here, to find out what has been showed in homepage
    '''         
    cnn_homepage = requests.get(CNN_HOMPAGE_ROOT)
    html_tree = html.fromstring(cnn_homepage.text)
    article_urls = html_tree.xpath('//a/@href')
    for home_url in article_urls:
        if ('http://' not in home_url and 'https://' not in home_url):
            home_url = CNN_HOMPAGE_ROOT + home_url
        try:
            article_home = Article(home_url)
            extract_cnn_article(article_home, True)
        except Exception as e:
            print('Smt wrong when process homepage article:  {}'.format(e) + home_url)
                    
                    
                    
                    
                   
                  
               
                   
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
usatoday_execept = {'http://www.usatoday.com/', 'https://offers.usatoday.com/3FOR34COM',
                    'http://www.usatoday.com/news/','http://www.usatoday.com/sports/', 
                    'http://www.usatoday.com/life/', 'http://www.usatoday.com/money/',
                    'http://www.usatoday.com/tech/', 'http://www.usatoday.com/travel/',
                    'http://www.usatoday.com/opinion/', 'http://www.usatoday.com/weather/',
                    'http://crosswords.usatoday.com/', 'http://www.usatoday.com/yourtake/',
                    'http://www.usatoday.com/topic/f4cd5d76-8c46-4d69-8a8f-85dfd6fefc5c/investigations/',
                    'http://www.usatoday.com/media/latest/videos/news/',
                    'http://www.usatoday.com/money/markets/', 'http://static.usatoday.com/mobile-apps/',
                    'http://www.usatoday.com/life/books/best-selling/','http://www.usatodayclassifieds.com/',
                    'http://college.usatoday.com/','http://reg.e.usatoday.com/',
                    'http://www.usatoday.com/media/latest/photos/news/',
                    'https://portfoliotracker.usatoday.com/portfolio', 'http://video-network.usatoday.com',
                    'http://www.usatoday.com/life/web-to-watch/','http://www.usatoday.com/shop/',
                    'http://www.usatoday.com/search', 'http://www.usatoday.com/conversation-guidelines/index.html',
                    'http://www.usatoday.com#', 'http://www.usatoday.com/topic/E01C4890-85A2-4E0B-A3DD-58BD88E71251/interactive-graphics/',
                    'http://www.usatoday.com/conversation-guidelines/index.html#signinfaq', 'http://www.usatoday.com/conversation-guidelines/index.html',
                    'http://fantasy.usatoday.com/', 'http://www.usatoday.com/sports/olympics/',
                    'http://mmajunkie.com/', 'http://www.usatoday.com/sports/motor-sports/',
                    'http://www.usatoday.com/sports/action-sports/', 'http://www.printroom.com/pro/usatoday/',
                    'http://www.usatodayhss.com/', 'http://www.usatoday.com/sports/horse-racing/',
                    'http://www.usatoday.com/media/latest/videos/sports/', 'http://ftw.usatoday.com/',
                    'http://www.usatoday.com/sports/main-section', 'http://www.usatoday.com/sports/social-links',
                    'http://www.bnqt.com', 'http://sportsnetwork.com/merge/tsnform.aspx',
                    'http://sportspolls.usatoday.com/ncaa/football/polls/coaches-poll/', 'http://sports.usatoday.com/ncaa/salaries/',
                    'http://www.usatoday.com/sports/college/schools/finances/', 'http://fantasyscore.com/', 
                    'http://fantasy.usatoday.com/category/football/', 'http://fantasy.usatoday.com/category/baseball',
                    'http://fantasy.usatoday.com/category/hockey', 'http://www.usatoday.com/sports/fantasy/baseball/player-news/',
                    'http://www.usatoday.com/sports/fantasy/baseball/statistics/', 'http://www.usatoday.com/sports/fantasy/baseball/injuries/',
                    'http://www.usatoday.com/sports/fantasy/baseball/salaries/', 'http://www.usatoday.com/sports/mlb/sagarin/', 
                    'http://www.baseballhq.com/', 'http://www.kffl.com/fantasy-baseball/',
                    'http://www.pgatour.com/stats.html/', 'http://sportsnetwork.com/merge/tsnform.aspx',
                    'http://www.usatoday.com/sports/action-sports', 'http://www.usatoday.com/sports/action-sports',
                    'http://sportsnetwork.com/merge/tsnform.aspx', 'http://www.usatoday.com/sports/fantasy/football/statistics/',
                    'http://www.usatoday.com/sports/mlb/teams/', 'http://www.usatoday.com/sports/mlb/rankings/',
                    'http://www.usatoday.com/sports/fantasy/football/player-news/', 'http://www.kffl.com/fantasy-football/',
                    'http://www.thehuddle.com/', 'http://www.usatoday.com/sports/mlb/injuries/', 
                    'http://www.usatoday.com/sports/nfl/', 'http://www.usatoday.com/sports/nfl/scores/',
                    'http://www.usatoday.com/sports/nfl/schedule/', 'http://www.usatoday.com/sports/nfl/standings/',
                    'http://www.usatoday.com/sports/nfl/statistics/','http://www.usatoday.com/sports/nfl/teams/',
                    'http://www.usatoday.com/sports/nfl/rankings/','http://www.usatoday.com/sports/nfl/injuries/',
                    'http://www.usatoday.com/sports/nfl/sagarin/',
                    'http://www.usatoday.com/sports/mlb/', 'http://www.usatoday.com/sports/mlb/scores/',
                    'http://www.usatoday.com/sports/mlb/schedule/', 'http://www.usatoday.com/sports/mlb/standings/',
                    'http://www.usatoday.com/sports/mlb/statistics/','http://www.usatoday.com/sports/mlb/salaries/',
                    'http://www.usatoday.com/sports/nba/', 'http://www.usatoday.com/sports/nba/scores/',
                    'http://www.usatoday.com/sports/nba/schedule/', 'http://www.usatoday.com/sports/nba/standings/',
                    'http://www.usatoday.com/sports/nba/statistics/','http://www.usatoday.com/sports/nba/teams/',
                    'http://www.usatoday.com/sports/nba/rankings/','http://www.usatoday.com/sports/nba/injuries/',
                    'http://www.usatoday.com/sports/nba/sagarin/',
                    'http://www.usatoday.com/sports/nhl/', 'http://www.usatoday.com/sports/nhl/scores/',
                    'http://www.usatoday.com/sports/nhl/schedule/', 'http://www.usatoday.com/sports/nhl/standings/',
                    'http://www.usatoday.com/sports/nhl/statistics/','http://www.usatoday.com/sports/nhl/teams/',
                    'http://www.usatoday.com/sports/nhl/rankings/','http://www.usatoday.com/sports/nhl/injuries/',
                    'http://www.usatoday.com/sports/nhl/sagarin/','http://www.usatoday.com/sports/nhl/salaries/',
                                  
                    'http://www.usatoday.com/sports/ncaaf/', 'http://www.usatoday.com/sports/ncaaf/scores/',
                    'http://www.usatoday.com/sports/ncaaf/schedule/', 'http://www.usatoday.com/sports/ncaaf/standings/',
                    'http://www.usatoday.com/sports/ncaaf/statistics/','http://www.usatoday.com/sports/ncaaf/teams/',
                    'http://www.usatoday.com/sports/ncaaf/rankings/','http://www.usatoday.com/sports/ncaaf/injuries/',
                    'http://www.usatoday.com/sports/ncaaf/sagarin/','http://www.usatoday.com/sports/ncaaf/salaries/',
                                  
                    'http://www.usatoday.com/sports/ncaab/', 'http://www.usatoday.com/sports/ncaab/scores/',
                    'http://www.usatoday.com/sports/ncaab/schedule/', 'http://www.usatoday.com/sports/ncaab/standings/',
                    'http://www.usatoday.com/sports/ncaab/statistics/','http://www.usatoday.com/sports/ncaab/teams/',
                    'http://www.usatoday.com/sports/ncaab/rankings/','http://www.usatoday.com/sports/ncaab/injuries/',
                    'http://www.usatoday.com/sports/ncaab/sagarin/','http://www.usatoday.com/sports/ncaab/salaries/',
                                  
                    'http://www.usatoday.com/sports/nascar/', 'http://www.usatoday.com/sports/nascar/scores/',
                    'http://www.usatoday.com/sports/nascar/schedule/', 'http://www.usatoday.com/sports/nascar/standings/',
                    'http://www.usatoday.com/sports/nascar/statistics/','http://www.usatoday.com/sports/nascar/teams/',
                    'http://www.usatoday.com/sports/nascar/rankings/','http://www.usatoday.com/sports/nascar/injuries/',
                    'http://www.usatoday.com/sports/nascar/sagarin/','http://www.usatoday.com/sports/nascar/salaries/',
                                  
                    'http://www.usatoday.com/sports/wnba/', 'http://www.usatoday.com/sports/wnba/scores/',
                    'http://www.usatoday.com/sports/wnba/schedule/', 'http://www.usatoday.com/sports/wnba/standings/',
                    'http://www.usatoday.com/sports/wnba/statistics/','http://www.usatoday.com/sports/wnba/teams/',
                    'http://www.usatoday.com/sports/wnba/rankings/','http://www.usatoday.com/sports/wnba/injuries/',
                    'http://www.usatoday.com/sports/wnba/sagarin/','http://www.usatoday.com/sports/wnba/salaries/',
                                  
                    'http://www.usatoday.com/sports/fantasy/baseball/', 'http://www.usatoday.com/sports/golf/leaderboard/',
                    'http://www.usatoday.com/sports/fantasy/football/injuries/', 'http://www.usatoday.com/sports/fantasy/football/',
                    'http://sportspolls.usatoday.com/ncaa/basketball-men/polls/coaches-poll/',
                    'http://footballfour.usatoday.com/', 'http://sportspolls.usatoday.com/ncaa/basketball-women/polls/coaches-poll/',
                                  
                                  
                    'http://www.usatoday.com/sports/golf/schedule/', 'http://www.usatoday.com/sports/golf/players/', 
                                  
                    'http://www.usatoday.com/sports/mls/scores/', 'http://www.usatoday.com/sports/mls/schedule/',
                    'http://www.usatoday.com/sports/mls/standings/', 'http://www.usatoday.com/sports/mls/teams/',
                    'http://www.usatoday.com/sports/mls/sagarin/', 'http://www.usatoday.com/sports/motor-sports/schedule/',
                    'http://www.usatoday.com/sports/nascar/results/', 'http://www.usatoday.com/sports/nascar/drivers/',
                    'http://sportspolls.usatoday.com/ncaa/basketball-women/polls/coaches-poll/', 
                    'http://www.usatoday.com/sports/olympics/2014/', 'http://www.usatoday.com/sports/tennis/schedule/',
                    'http://www.usatoday.com/sports/tennis/players/','http://worldcup.usatoday.com/',
                                  
                    'https://service.usatoday.com/subscriptions/dc/checkout.faces', 'http://www.usatoday.com/money/personal-finance/',
                                  
                                  
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
        thumbnail_url = html_tree.xpath('//meta[@name="twitter:image:src"]')[0].attrib['content']
        print(thumbnail_url)
    except Exception as e:
        #print('Thumbnaill not found. {}'.format(e))
        print("")
    try:
        if(thumbnail_url is None):
            thumbnail_url = html_tree.xpath('//meta[@itemprop="image"]')[0].attrib['content']
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
                  
                  
                  
    if (article.published_time is None or article.title is None or article.category_id is None):
        raise Exception("")
               
    text_html = true_html.escape(get_text_html_saulify(normalized_url), True)
    article.parse()
    text = normalize_text(article.text)
    normalized_title = normalize_text_nostop(article.title)
    ''' insert this article to database, maybe send url to another thread to get count, share, .... or maket it asynchronous'''
    # when no exception, we insert to database
    try:
        print(db_connect.insert_article3(normalized_url, article.title, usatoday_source_id, 
                                     article.category_id, False, is_on_homepage, article.published_time,
                                     thumbnail_url, article.short_description, USA, text_html, text, normalized_title))
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
        thumbnail_url = html_tree.xpath('//meta[@property="og:image"]')[0].attrib['content']
        print(thumbnail_url)
    except Exception as e:
        print('Thumbnaill not found.'.format(e))
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
           
           
           
           
    # get content
    article.parse()
    text = normalize_text(article.text)
    text_html = true_html.escape(get_text_html_saulify(normalized_url), True)
    normalized_title = normalize_text_nostop(article.title)
    
    ''' insert this article to database, maybe send url to another thread to get count, share, .... or maket it asynchronous'''
    # when no exception, we insert to database
    try:
        print(db_connect.insert_article3(normalized_url, article.title, people_source_id, 
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
          
          
          
          
    # get content
    article.parse()
    text = normalize_text(article.text)
    text_html = true_html.escape(get_text_html_saulify(normalized_url), True)
    normalized_title = normalize_text_nostop(article.title)
    ''' insert this article to database, maybe send url to another thread to get count, share, .... or maket it asynchronous'''
    # when no exception, we insert to database
    try:
        print(db_connect.insert_article3(normalized_url, article.title, forbes_source_id, 
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
