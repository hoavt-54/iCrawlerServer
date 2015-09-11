'''
Created on Feb 25, 2015

@author: hoavu
'''
import json
import queue
import re
import requests
from threading import Thread
import time
import urllib.parse
from random import randint
import sys,os
from urllib.parse import quote
sys.path.append(os.path.realpath('..'))
from crawlerApp import utils
from fbsdk import facebook
from iiidatabase.DatabaseConnectionLib import IIIDatbaseConnection



IIIN_SERVER_APP_ID="1410650005904021"
IIIN_SERVER_SERCRET = '52c5ce6ee56af4221c6215f3fc1418d4'
FB_REST_API = 'http://api.facebook.com/restserver.php'
TWITTER_URL_API = 'http://urls.api.twitter.com/1/urls/count.json'
POISON = "quite_queue"
'''=========================================================================
Thread waiting to get comment like and share for url, then save result in db
==========================================================================='''
class CommentLikeShrareGetterThread(Thread):
    # define a constructor, parameterised a queue
    def __init__(self, queue):
        Thread.__init__(self)
        self.name= "Thread_share_like_comment_count"
        self.queue = queue;
        self.is_running = True
    
    def stop_running (self):
        self.is_running = False
    
    def run(self):
        
        try:
            db_thread = IIIDatbaseConnection()
            db_thread.init_database_cont()
            next_url = None
            while self.is_running:
                #get statistic on FB, TW
                try:
                    next_url = self.queue.get(True)
                    if (next_url == None or next_url == POISON):
                        self.stop_running()
                        break
                    param_url = next_url
                    if ("http://espn.go.com/" in next_url):
                        try:
                            param_url = next_url.split("_/id/")[0] + "_/id/" +  next_url.split("_/id/")[1].split("/")[0];
                        except Exception as e: 
                            print("cannot split espn url")
                            param_url = next_url
                    fb_param = dict(method = 'links.getStats',
                                urls = urllib.parse.quote(param_url, safe=''),
                                format = 'json')
                    tw_param = dict(url=next_url)
                    fb_resp = requests.get(url=FB_REST_API, params = fb_param)
                    data = json.loads(fb_resp.text)[0]
                    tw_resp = requests.get(url=TWITTER_URL_API, params = tw_param)
                    twi_data = json.loads(tw_resp.text)
                    #print(data)
                    #print(twi_data)
                    print(db_thread.update_article_count(next_url, data['comment_count'],
                                                         data['share_count'], data['like_count'], data['comments_fbid'], twi_data['count']))
                except Exception as e:
                    print("Error when get FB, TW like comment: {}".format(e))

        except Exception as db_e:
            print("Error database thread get like_share count: {}".format(db_e))
        finally:
            #close connection db before exit
            if (db_thread is not None):
                db_thread.close_database_cont()
        print("commentlikeshare thread stoppped")
'''    
=========================== end of get like, share thread =====================
'''    
                    
                    
                    
                    
                    
                    
                    
source_fb_photo = ['bleacherreport_us', 'espn_usa',
                   'cbs_news', 'nbc_news', 'business_insider',
                   'bloomberg', 'forbes_usa', 'mashable',
                   'buzzfeed', 'uproxx', 'theblaze', 
                   'washington_post', 'abc_news', 
                   'eonline_us', 'fox_news', 'la_times',
                   'iflscience', 'nydailynews', 'reuters',
                   'cnbc']                    




pages_id = [#'1401344456845009', 5Asrticler5 banned
             '778046915618571', '329570850574813',
            '647633765368739', '1594539410758135', 
            #'657808134330750', Articles banned
            '1417094931918673', #'753548271381696', A1llneuwscnmn banned
            # '1592315347647071', Hot News Articles banned
            '445841905563902', '799881623421852', '479853082171495', 
            #'1574182962841454',Azticles15 banned
             '414583335389044', '1571382756463440',
            '388362948009298', '1588907418029083', '799495940143171', 
            '328827617326389', 
            #'353668731505591', Azticles18 banned
            '592177567585710', 
            '806091826127482', '680882785351524', '557816184358955', 
            '880828675311080', '1394037944249687', '1617904361758199',
            '1588155624772622', '361880147332574', '979799952044570',# Trending news
            '100774583592220', #Trending news1
            '461608584015059', #Trending news2
            '958048410882817', #Trending Albums1'
            '787179224735097', #:'Trending Albums2'
            '980649805292370', #:'Trending Albums3'
            '995820583775929', #:'Trending Albums4'
            '693162337472554', #:'Trending Albums5'
            '912019705485561',#:'Trending Albums6'
            '821048611275830',#:'Trending Albums7'
            '357000477840701',#:'Trending Albums8'
            '845760015502271', #:'Trending Albums9'
            '1429198120723455',#:'Trending Albums10'
            '529885843825598',#:”Trending Albums11”
            '755459311239529', #:”Trending Albums12”
            '102975006707199',#:”Trending Albums13”
            '365466883636495' #2PageArticles2
            ]

TOKEN_TIMEOUT = 40 * 24 * 60 * 60
pages_tokens = {}  
    
def get_api(access_token, page_id):
    graph = facebook.GraphAPI(access_token)
    # Get page token to post as the page. You can skip 
    # the following if you want to post as yourself. 
    resp = graph.get_object('me/accounts')
    page_access_token = None
    for page in resp['data']:
        if page['id'] == page_id:
            page_access_token = page['access_token']
            graph = facebook.GraphAPI(page_access_token)
            return graph
    # You can also skip the above if you get a page token:
    # http://stackoverflow.com/questions/8231877/facebook-access-token-for-pages
    # and make that long-lived token as in Step 3

def get_api_pagetoken (self, page_access_token):
    return facebook.GraphAPI(page_access_token)

                    
class PostToFacebookPage(Thread):
    
    # define a constructor, parameterised a queue
    def __init__(self, queue):
        Thread.__init__(self)
        self.name= "Thread_post_2_facebook_page"
        self.queue = queue;
        self.is_running = True
        self.FB_LONGLIVE_ACTK = None
        self.LAST_TIME_GET_TOKEN = 0
    
    def stop_running (self):
        self.is_running = False
        

    
        
    def run(self):
        print("thread post article to page already started")
        try:
            db_thread = None
            next_article = None
            #get statistic on FB, TW
            while self.is_running:
                try:
                    next_article = self.queue.get(True)
                    ''' sometime post bloomberg image causing error: (#100) picture URL is not properly formatted '''
                    if (POISON == next_article):
                        self.stop_running()
                        break
                    raise Exception("not post anything for now")
                    if ( next_article.thumbnail_url is None or len(next_article.thumbnail_url) < 8):#''''bloomberg' in next_article.url or'''
                        next_article.thumbnail_url ='http://www.leoncidesign.com/images/placeholder.png'
                    if (next_article.thumbnail_url.startswith("//")):
                        next_article.thumbnail_url = "http:" + next_article.thumbnail_url    
                    if (int(time.time()) - self.LAST_TIME_GET_TOKEN > TOKEN_TIMEOUT):
                        with open ("../../fb_token.txt", "r") as myfile:
                            self.FB_LONGLIVE_ACTK =myfile.read().replace('\n', '')
                            self.LAST_TIME_GET_TOKEN = int(time.time())
                            print("refreshed Facebook token")
                    page_id_position = randint(0, len(pages_id) - 1 ) # post to all pages by each one
                    print("page_id_position: " + str(page_id_position))
                    api = get_api(self.FB_LONGLIVE_ACTK, pages_id[page_id_position])
                    msg = ""
                    ''' add app link sometime '''
                    post_url = "http://iiin.today/applink.html?url=" + urllib.parse.quote_plus(next_article.url) + "&article_id=" + str(next_article.id)
                    print("url to post to fb: " + post_url)
                    if (next_article.source_name is None):
                        next_article.source_name = "IIIN - Trending news"
                    if (next_article.id is None):
                        next_article.id = 0
                    attchment = {"name": next_article.title,
                             "link": post_url, 
                             "caption": "By " + next_article.source_name,
                             "description": next_article.short_description,
                             "picture": next_article.thumbnail_url}
                    result = None
                    result_photo = None
                    
                    '''put article to fb'''
                    try:
                        result =  api.put_wall_post(msg, attachment = attchment)
                        print("postId: " + result['id'])
                    except Exception as e:
                        print("Cannot post " + next_article.url + " to FB page {}".format(e))
                    
                    
                    '''put photo to fb'''
                    try:
                        if (next_article.source_id in source_fb_photo):
                            time.sleep(4)
                            result_photo =  api.put_photo_url_2_page(next_article.short_description, next_article.thumbnail_url)
                            print("photo_Id: " + result_photo['id'])
                    except Exception as e:
                        print("Error page_id: " + pages_id[page_id_position])
                        print("Cannot post photo " + next_article.thumbnail_url + " to FB page {}".format(e))
                        
                    if ((result is None or result['id'] is None) and (result_photo is None or result_photo['id'] is None)):
                        print("Cannot post " + next_article.url + " to FB page")
                        ''' put to queue to retry later'''
                        #try:
                        #    self.queue.put(next_article, True)
                        #except Exception as e1:
                        #    print ('put to queue to retry later')
                    else: # save id to database
                        '''save db post id'''
                        try:
                            try:
                                db_thread = IIIDatbaseConnection()
                                db_thread.init_database_cont()
                                print(db_thread.update_article_fbid_photo(next_article.url, result['id'] if result is not None else None, result_photo['id'] if result_photo is not None else None))
                            finally:
                                db_thread.close_database_cont()
                        except Exception as e:
                            print("Error save FB id to database: {}".format(e))
                        
                except Exception as e:
                    print("Error when post article to FB pages: {}".format(e))
                time.sleep(6)
            print("thread post article to FB stopped")
        except Exception as db_e:
            print("Error database thread post to Facebook: {}".format(db_e))
    
        
        
# next_url = "http://espn.go.com/mlb/story/_/id/12849757/david-price-detroit-tigers-leaves-game-right-ankle-injury-stepping-bat"        
# param_url = next_url.split("_/id/")[0] + "_/id/" +  next_url.split("_/id/")[1].split("/")[0];
# print(param_url)
# FB_LONGLIVE_ACTK ="CAACEdEose0cBALkdhaK2P8EKo0KjcZCxrfq7SNonZBqnKojYChGjSogtPAfBRBli9jPZBKrttVlfAdHW1USmhq5XyWf18bZBZC4gxgIgFqWaPNUukHjyPGgraghPEZC0pDZAVEMe4vaB7uwHMpbXbG9E1aFj9mo4BBsqHy75ckoajc40bitiRcLxy0ZCj7VzUM997NsIhs4AKtJ2n7Hs2cPq67sdUrGJoIEZD"
# api = get_api(FB_LONGLIVE_ACTK, "778046915618571")
# result =  api.put_photo_url_2_page("test photo by python", "http://i.huffpost.com/gen/2989928/images/r-143254701929-huge.jpg")
# print(result)
    