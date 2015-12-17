'''
@author: hoavu
'''
'''
handle CNN first, just for now
'''
# cnn_cate_id -> iii_cate_id
'''
============================================================================================
===================================  Start thread to get url statistic here ================
============================================================================================
'''

import calendar
from datetime import datetime
from dateutil.parser import parse
import json
from lxml import html
import newspaper
from newspaper.article import Article
from pytz import timezone
import queue
import requests
from threading import Thread
from threading import Thread

from crawlerApp.PostAndGetFromFbPages import CommentLikeShrareGetterThread, \
    POISON, PostToFacebookPage
from crawlerApp.utils import normalize_url
from crawlerApp.utils import normalize_url, hasNumbers, convert_vn_date
from iiidatabase.DatabaseConnectionLib import IIIDatbaseConnection


print('Start thread get like share comments')
url_sharelikecomment_queue = queue.Queue()
share_like_comment_thread = CommentLikeShrareGetterThread(queue=url_sharelikecomment_queue)
share_like_comment_thread.start()
 
'''
============================================================================================
'''   
    


'''
========================================================================================
============================VnExpress start ============================================
========================================================================================
'''
VNEXPRESS_HOME = "http://vnexpress.net"
vnexpress_source_id = 'vnexpress'
VN = 'vn'
vnexpress_category = { '1001005' : 'news', '1003450' : 'opinions', '1001002' : 'world',
                        '1001158' : 'world', '1001139' : 'world', '1001147' : 'world',
                        '1003170' : 'business', '1003165' : 'business', '1003179' : 'business',
                        '1003175' : 'business', '1003185' : 'business', '1003180' : 'business',
                        '1003181' : 'business', '1002727' : 'entertainment', '1002726' : 'entertainment',
                        '1002750' : 'entertainment', '1002748' : 'entertainment', '1002728' : 'entertainment',
                        '1002993' : 'entertainment', '1002731' : 'entertainment', '1002995' : 'entertainment',
                        '1002733' : 'entertainment', '1002753' : 'entertainment', '1002752' : 'entertainment',
                        '1002720' : 'entertainment', '1002737' : 'entertainment', '1002568' : 'sport',
                        '1002575' : 'sport', '1002580' : 'sport', '1002587' : 'sport', '1002570' : 'sport',
                        '1002584' : 'sport', '1002619' : 'sport', '1003495' : 'sport', '1002623' : 'sport',
                        '1003001' : 'sport', '1003426' : 'law', '1001007' : 'law', '1001117' : 'law',
                        '1003498' : 'education', '1003497' : 'education', '1003500' : 'education',
                        '1003281' : 'travel', '1003254' : 'travel', '1003266' : 'travel',
                        '1003261' : 'travel', '1003282' : 'travel', '1003303' : 'travel',
                        '1003315' : 'travel', '20000'  : 'travel', '1003316' : 'travel',
                        '1001009' : 'tech', '1002661' : 'tech', '1002648' : 'tech',
                        '1002645' : 'tech', '1002646' : 'tech', '1002647' : 'tech',
                        '1001014' : 'expressing', 'Thời sự': 'news', 'Góc nhìn' : 'opinions',
                        'Thế giới' : 'world', 'Kinh doanh' : 'business', 'Giải trí' : 'entertainment',
                        'Thể thao' : 'sport', 'Pháp luật' : 'law', 'Giáo dục' : 'education',
                        'Đời sống' : 'entertainment', 'Du lịch' : 'travel', 'Khoa học' : 'tech',
                        'Số hóa' : 'tech', 'Tâm sự' : 'expressing', 'Cộng đồng' : 'community',
                        '1003693' : 'world', '1001142' : 'world', 
                        '1003520' : 'entertainment' , '1003521' : 'entertainment', '1002732': 'entertainment',
                        '1002734' : 'entertainment', '1002622' : 'sport', '1003598' : 'sport',
                         '1002586' : 'sport', '1002582': 'sport',
                         '1002967' : 'life', '1003399' : 'life', '1003463' : 'life',
                        '1003313' : 'travel', '1003287' : 'travel', '1003275' : 'travel',
                        '1001012' : 'community', '1003082' : 'expressing'
                    }

vnexpress_except = {
                    }

db_connect = None

def extract_vnexpress_article (article, is_on_homepage, predifined_category=None):
    if (not hasNumbers(article.url) or article.url in vnexpress_except or article.url + '/' in vnexpress_except or 'vnexpress' not in article.url ):
        return
    if (db_connect.is_url_existed(article.url) != -1):
        print("url is already existed")
        url_sharelikecomment_queue.put(article.url, True)
        return
    normalized_url = normalize_url(article.url)
    if ('vnexpress' not in normalized_url):
        return
    if (normalized_url in vnexpress_except or normalized_url + '/' in vnexpress_except):
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
        time_string = time_string.replace (' + ', 'GMT+')
    except BaseException as dateE:
        print("problem with time: {}".format(dateE))
        
    try: # this is for business time only
        time_string = html_tree.xpath('//div[@class="block_timer left txt_666"]/text()')
        time_string = time_string[0] + " " + time_string[1]
        time_string = convert_vn_date(time_string)
    except BaseException as dateE:
            print("problem with time: {}".format(dateE))
            
    try: # this is for sport time only
        time_string = html_tree.xpath('//div[@class="block_timer left txt_666"]/text()')
        time_string = time_string[0]
        time_string = time_string.replace("|","")
        print(time_string)
        time_string = convert_vn_date(time_string)
        print(time_string)
    except BaseException as dateE:
            print("problem with time: {}".format(dateE))        
    
    if (time_string is not None):
        date_time = parse(time_string)
        article.published_time = calendar.timegm(date_time.utctimetuple())
        print(article.published_time)
    
    
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
    article.title = title.split("- VnExpress")[0]
    
    
    # get thumbnail
    try:
        thumbnail_url = html_tree.xpath('//meta[@itemprop="thumbnailUrl"]')[0].attrib['content']
        print(thumbnail_url)
    except Exception as e:
        print('Thumbnaill not found. {}'.format(e))  
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
    article.short_description = short_description
    
    
    # get category
    try:
        category_id = html_tree.xpath('//meta[@name="tt_category_id"]')[0].attrib['content']
    except Exception as e:
        print('Category not found. {}'.format(e))
    
    try:
        if (category_id is None):
            category_id = html_tree.xpath('//meta[@itemprop="articleSection"]')[0].attrib['content']
    except Exception as e:
        print('Category not found. {}'.format(e))
    if (category_id is not None):
        print('category: ' + category_id)
        article.category_id = vnexpress_category.get(category_id)
    print(article.category_id)
    
    
    
    if (article.published_time is None or article.title is None or article.category_id is None):
        raise Exception("")
    
    
    ''' insert this article to database, maybe send url to another thread to get count, share, .... or maket it asynchronous'''
    # when no exception, we insert to database
    try:
        print(db_connect.insert_article2(normalized_url, article.title, vnexpress_source_id, 
                                     article.category_id, False, is_on_homepage, article.published_time,
                                     article.thumbnail_url, article.short_description, VN))
    except Exception as dbE:
        print("Error when insert article to db. {}".format(dbE))
    # after insert to database, we put this url to get share, comment, like
    url_sharelikecomment_queue.put(normalized_url, True)



print('...................................................\n' +
      '...................................................\n' + 
      '...................................................\n' +
      'start get articles from vnexpress' +
      '...................................................\n' +
      '...................................................\n'
      )
try:
    db_connect = IIIDatbaseConnection()
    db_connect.init_database_cont()
    
    

    
#     ''' we process homepage news'''
#     VNEXPRESS_HOMPAGE_NEWS = 'http://vnexpress.net/tin-tuc/thoi-su/'
#     vnexpress_homepage_news = requests.get(VNEXPRESS_HOMPAGE_NEWS)
#     html_tree = html.fromstring(vnexpress_homepage_news.text)
#     article_urls = html_tree.xpath('//a/@href')
#     for home_url in article_urls:
#         if  home_url is not None and len(home_url) > 16 : 
#             if ('http://' not in home_url and 'https://' not in home_url):
#                 home_url = VNEXPRESS_HOME + home_url
#             try:
#                 article_home = Article(home_url)
#                 extract_vnexpress_article(article_home, True, 'news')
#             except Exception as e:
#                 print('Smt wrong when process homepage news  article:  {}'.format(e) + home_url)
# #       
# 
#     
#     
#     ''' we process homepage opinions'''
#     VNEXPRESS_HOMPAGE_OPINIONS = 'http://vnexpress.net/tin-tuc/goc-nhin'
#     vnexpress_homepage_opinions = requests.get(VNEXPRESS_HOMPAGE_OPINIONS)
#     html_tree = html.fromstring(vnexpress_homepage_opinions.text)
#     article_urls = html_tree.xpath('//a/@href')
#     for home_url in article_urls:
#         if  home_url is not None and len(home_url) > 16 : 
#             if ('http://' not in home_url and 'https://' not in home_url):
#                 home_url = VNEXPRESS_HOME + home_url
#             try:
#                 article_home = Article(home_url)
#                 extract_vnexpress_article(article_home, True, 'opinions')
#             except Exception as e:
#                 print('Smt wrong when process homepage opinions  article:  {}'.format(e) + home_url)
# 
#     
#     
#     
#     
#     
#     ''' we process homepage world'''
#     VNEXPRESS_HOMPAGE_WORLD = 'http://vnexpress.net/tin-tuc/the-gioi'
#     vnexpress_homepage_world = requests.get(VNEXPRESS_HOMPAGE_WORLD)
#     html_tree = html.fromstring(vnexpress_homepage_world.text)
#     article_urls = html_tree.xpath('//a/@href')
#     for home_url in article_urls:
#         if  home_url is not None and len(home_url) > 16 : 
#             if ('http://' not in home_url and 'https://' not in home_url):
#                 home_url = VNEXPRESS_HOME + home_url
#             try:
#                 article_home = Article(home_url)
#                 extract_vnexpress_article(article_home, True, 'world')
#             except Exception as e:
#                 print('Smt wrong when process homepage world  article:  {}'.format(e) + home_url)
# 
# 
#                 
#                 
#                 
#     
#     
#     
#     ''' we process homepage business'''
#     VNEXPRESS_HOMPAGE_BUSINESS = 'http://kinhdoanh.vnexpress.net/'
#     vnexpress_homepage_business = requests.get(VNEXPRESS_HOMPAGE_BUSINESS)
#     html_tree = html.fromstring(vnexpress_homepage_business.text)
#     article_urls = html_tree.xpath('//a/@href')
#     for home_url in article_urls:
#         if  home_url is not None and len(home_url) > 16 : 
#             if ('http://' not in home_url and 'https://' not in home_url):
#                 home_url = VNEXPRESS_HOME + home_url
#             try:
#                 article_home = Article(home_url)
#                 extract_vnexpress_article(article_home, True, 'business')
#             except Exception as e:
#                 print('Smt wrong when process homepage business  article:  {}'.format(e) + home_url)
# 
# 
# 
# 
# 
# 
#     ''' we process homepage entertainment'''
#     VNEXPRESS_HOMPAGE_ENTERTAIN = 'http://giaitri.vnexpress.net/'
#     vnexpress_homepage_entertainment = requests.get(VNEXPRESS_HOMPAGE_ENTERTAIN)
#     html_tree = html.fromstring(vnexpress_homepage_entertainment.text)
#     article_urls = html_tree.xpath('//a/@href')
#     for home_url in article_urls:
#         if  home_url is not None and len(home_url) > 16 : 
#             if ('http://' not in home_url and 'https://' not in home_url):
#                 home_url = VNEXPRESS_HOME + home_url
#             try:
#                 article_home = Article(home_url)
#                 extract_vnexpress_article(article_home, True, 'entertainment')
#             except Exception as e:
#                 print('Smt wrong when process homepage entertainment  article:  {}'.format(e) + home_url)
# 
# 
# 
# 
# 
# 
# 
#     ''' we process homepage sport'''
#     VNEXPRESS_HOMPAGE_SPORT = 'http://thethao.vnexpress.net/'
#     vnexpress_homepage_sport = requests.get(VNEXPRESS_HOMPAGE_SPORT)
#     html_tree = html.fromstring(vnexpress_homepage_sport.text)
#     article_urls = html_tree.xpath('//a/@href')
#     for home_url in article_urls:
#         if  home_url is not None and len(home_url) > 16 : 
#             if ('http://' not in home_url and 'https://' not in home_url):
#                 home_url = VNEXPRESS_HOME + home_url
#             try:
#                 article_home = Article(home_url)
#                 extract_vnexpress_article(article_home, True, 'sport')
#             except Exception as e:
#                 print('Smt wrong when process homepage sport  article:  {}'.format(e) + home_url)
# #                 
#                 
#                 
#                 
#                 
#                 
#                 
#                 
#     
#     ''' we process homepage law'''
#     VNEXPRESS_HOMPAGE_LAW = 'http://vnexpress.net/tin-tuc/phap-luat/'
#     vnexpress_homepage_law = requests.get(VNEXPRESS_HOMPAGE_LAW)
#     html_tree = html.fromstring(vnexpress_homepage_law.text)
#     article_urls = html_tree.xpath('//a/@href')
#     for home_url in article_urls:
#         if  home_url is not None and len(home_url) > 16 : 
#             if ('http://' not in home_url and 'https://' not in home_url):
#                 home_url = VNEXPRESS_HOME + home_url
#             try:
#                 article_home = Article(home_url)
#                 extract_vnexpress_article(article_home, True, 'law')
#             except Exception as e:
#                 print('Smt wrong when process homepage law  article:  {}'.format(e) + home_url)            
#                 
#                 
#                 
# 
# 
# 
# 
# 
#     ''' we process homepage education'''
#     VNEXPRESS_HOMPAGE_EDUCATION= 'http://vnexpress.net/tin-tuc/giao-duc'
#     vnexpress_homepage_education = requests.get(VNEXPRESS_HOMPAGE_EDUCATION)
#     html_tree = html.fromstring(vnexpress_homepage_education.text)
#     article_urls = html_tree.xpath('//a/@href')
#     for home_url in article_urls:
#         if  home_url is not None and len(home_url) > 16 : 
#             if ('http://' not in home_url and 'https://' not in home_url):
#                 home_url = VNEXPRESS_HOME + home_url
#             try:
#                 article_home = Article(home_url)
#                 extract_vnexpress_article(article_home, True, 'education')
#             except Exception as e:
#                 print('Smt wrong when process homepage education  article:  {}'.format(e) + home_url)            
#                 
#                 
# 
#                 
#                 
#                 
#                 
#                 
#     ''' we process homepage life'''
#     VNEXPRESS_HOMPAGE_LIFE= 'http://doisong.vnexpress.net/'
#     vnexpress_homepage_life = requests.get(VNEXPRESS_HOMPAGE_LIFE)
#     html_tree = html.fromstring(vnexpress_homepage_life.text)
#     article_urls = html_tree.xpath('//a/@href')
#     for home_url in article_urls:
#         if  home_url is not None and len(home_url) > 16 : 
#             if ('http://' not in home_url and 'https://' not in home_url):
#                 home_url = VNEXPRESS_HOME + home_url
#             try:
#                 article_home = Article(home_url)
#                 extract_vnexpress_article(article_home, True, 'entertainment')
#             except Exception as e:
#                 print('Smt wrong when process homepage life  article:  {}'.format(e) + home_url)


                

#     ''' we process homepage travel'''
#     VNEXPRESS_HOMPAGE_TRAVEL= 'http://dulich.vnexpress.net/'
#     vnexpress_homepage_travel = requests.get(VNEXPRESS_HOMPAGE_TRAVEL)
#     html_tree = html.fromstring(vnexpress_homepage_travel.text)
#     article_urls = html_tree.xpath('//a/@href')
#     for home_url in article_urls:
#         if  home_url is not None and len(home_url) > 16 : 
#             if ('http://' not in home_url and 'https://' not in home_url):
#                 home_url = VNEXPRESS_HOME + home_url
#             try:
#                 article_home = Article(home_url)
#                 extract_vnexpress_article(article_home, True, 'travel')
#             except Exception as e:
#                 print('Smt wrong when process homepage travel  article:  {}'.format(e) + home_url)




    
    
    
#     ''' we process homepage tech'''
#     VNEXPRESS_HOMPAGE_TECH =  'http://vnexpress.net/tin-tuc/khoa-hoc/'
#     vnexpress_homepage_tech = requests.get(VNEXPRESS_HOMPAGE_TECH)
#     html_tree = html.fromstring(vnexpress_homepage_tech.text)
#     article_urls = html_tree.xpath('//a/@href')
#     for home_url in article_urls:
#         if  home_url is not None and len(home_url) > 16 : 
#             if ('http://' not in home_url and 'https://' not in home_url):
#                 home_url = VNEXPRESS_HOME + home_url
#             try:
#                 article_home = Article(home_url)
#                 extract_vnexpress_article(article_home, True, 'tech')
#             except Exception as e:
#                 print('Smt wrong when process homepage tech  article:  {}'.format(e) + home_url)
#                 
    
    
    
    
    
#     ''' we process homepage comunity'''
#     VNEXPRESS_HOMPAGE_COMMUNITY =  'http://vnexpress.net/tin-tuc/cong-dong'
#     vnexpress_homepage_community = requests.get(VNEXPRESS_HOMPAGE_COMMUNITY)
#     html_tree = html.fromstring(vnexpress_homepage_community.text)
#     article_urls = html_tree.xpath('//a/@href')
#     for home_url in article_urls:
#         if  home_url is not None and len(home_url) > 16 : 
#             if ('http://' not in home_url and 'https://' not in home_url):
#                 home_url = VNEXPRESS_HOME + home_url
#             try:
#                 article_home = Article(home_url)
#                 extract_vnexpress_article(article_home, True, 'community')
#             except Exception as e:
#                 print('Smt wrong when process homepage community  article:  {}'.format(e) + home_url)  
                
                

    
    
#     ''' we process homepage expressing'''
#     VNEXPRESS_HOMPAGE_EXPRESSING =  'http://vnexpress.net/tin-tuc/tam-su'
#     vnexpress_homepage_expressing= requests.get(VNEXPRESS_HOMPAGE_EXPRESSING)
#     html_tree = html.fromstring(vnexpress_homepage_expressing.text)
#     article_urls = html_tree.xpath('//a/@href')
#     for home_url in article_urls:
#         if  home_url is not None and len(home_url) > 16 : 
#             if ('http://' not in home_url and 'https://' not in home_url):
#                 home_url = VNEXPRESS_HOME + home_url
#             try:
#                 article_home = Article(home_url)
#                 extract_vnexpress_article(article_home, True, 'expressing')
#             except Exception as e:
#                 print('Smt wrong when process homepage expressing  article:  {}'.format(e) + home_url)  
                
                
    
    
    
    
    
    
    ''' we process homepage'''
    VNEXPRESS_HOMPAGE =  'http://vnexpress.net/'
    vnexpress_homepage= requests.get(VNEXPRESS_HOMPAGE)
    html_tree = html.fromstring(vnexpress_homepage.text)
    article_urls = html_tree.xpath('//a/@href')
    for home_url in article_urls:
        if  home_url is not None and len(home_url) > 16 : 
            if ('http://' not in home_url and 'https://' not in home_url):
                home_url = VNEXPRESS_HOME + home_url
            try:
                article_home = Article(home_url)
                extract_vnexpress_article(article_home, True)
            except Exception as e:
                print('Smt wrong when process homepage  article:  {}'.format(e) + home_url)  
    
    










    db_connect.close_database_cont()   
except Exception as e:        
    print('Something went wrong with database: {}'.format(e))
    
    
    
    
    '''
    =======================================================================================================================================
    =======================================================================================================================================
    ================================================= VNEpress stop ======================================================================
    =======================================================================================================================================
    =======================================================================================================================================
    '''




















'''============================================================================
we stop thread getting like, share, comment count here by putting poison in to queue
'''
try:
    share_like_comment_thread.stop_running()
    url_sharelikecomment_queue.put(POISON, True)
except Exception as e:
    print("cannot stop other thread: {}".format(e))