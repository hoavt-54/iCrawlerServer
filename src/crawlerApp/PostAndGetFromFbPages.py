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
import sys,os
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
                    fb_param = dict(method = 'links.getStats',
                                urls = urllib.parse.quote(next_url, safe=''),
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
'''    
=========================== end of get like, share thread =====================
'''    
                    
                    
                    
                    
                    
                    
                    
                    




pages_id = ['1401344456845009', '778046915618571', '329570850574813',
            '647633765368739', '1594539410758135', '657808134330750',
            '1417094931918673', '753548271381696', '1592315347647071',
            '445841905563902', '799881623421852', '350678428455274', 
            '1574182962841454', '414583335389044', '1571382756463440',
            '388362948009298', '1588907418029083', '799495940143171', 
            '328827617326389', '353668731505591', '592177567585710', 
            '806091826127482', '680882785351524', '557816184358955', 
            '880828675311080', '1394037944249687', '1617904361758199',
            '1588155624772622', '361880147332574'
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
            db_thread = IIIDatbaseConnection()
            db_thread.init_database_cont()
            next_article = None
            posts_count = 0
            #get statistic on FB, TW
            while self.is_running:
                try:
                    next_article = self.queue.get(True)
                    ''' sometime post bloomberg image causing error: (#100) picture URL is not properly formatted '''
                    if (next_article == None or next_article == POISON):
                        self.stop_running()
                        break
                    if ('bloomberg' in next_article.url or next_article.thumbnail_url is None):
                        next_article.thumbnail_url ='http://www.leoncidesign.com/images/placeholder.png'
                    if (int(time.time()) - self.LAST_TIME_GET_TOKEN > TOKEN_TIMEOUT):
                        with open ("../../fb_token.txt", "r") as myfile:
                            self.FB_LONGLIVE_ACTK =myfile.read().replace('\n', '')
                            self.LAST_TIME_GET_TOKEN = int(time.time())
                            print("refreshed Facebook token")
                    page_id_position = posts_count % len(pages_id) # post to all pages by each one
                    posts_count += 1
                    api = get_api(self.FB_LONGLIVE_ACTK, pages_id[page_id_position])
                    msg = ""
                    attchment = {"name": next_article.title,
                             "link": next_article.url,
                             "caption": "By IIIN",
                             "description": next_article.short_description,
                             "picture": next_article.thumbnail_url}
                    result =  api.put_wall_post(msg, attachment = attchment)
                    
                    if (result is None or result['id'] is None):
                        print("Cannot post " + next_article.url + " to FB page")
                        ''' put to queue to retry later'''
                        try:
                            self.queue.put(next_article, True)
                        except Exception as e1:
                            print ('put to queue to retry later')
                    else: # save id to database
                        print("postId: " + result['id'])
                        print(db_thread.update_article_fbid(next_article.url, result['id']))
                except Exception as e:
                    print("Error when post article to FB pages: {}".format(e))
                time.sleep(3)
        except Exception as db_e:
            print("Error database thread post to Facebook: {}".format(db_e))
        finally:
            #close connection db before exit
            if (db_thread is not None):
                db_thread.close_database_cont()   
    
        
        
        
    
    

    
    
    
    

    
    
    
    