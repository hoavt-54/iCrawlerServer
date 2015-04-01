'''
Created on Mar 15, 2015

@author: hoavu
'''
import json
import queue
import re
import requests
from threading import Thread
import time
import urllib.parse
import os.path
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from crawlerApp import utils
from fbsdk import facebook
from iiidatabase.DatabaseConnectionLib import IIIDatbaseConnection


FB_LONGLIVE_ACTK = "CAAUCZBoyBGpUBACo0GuUx75S24R9nzHz8rOPZAXQZBJGzZBKv6dJOjiM2EAbmxKiWZApxQPW0sSlpVAfFu2ZAqzDr5MdbTUxwstdaFWNTbVe4hs68J0NhlPGdN16Fr5BpEZBb9mlxNm7XjQSxARZCos40An5pcVkuUFodWZAQanjJrZCL20xDqyZCmHqaZBdGdgYbHGCBt8c1LqULzjmZA8nL3sNj"
IIIN_SERVER_APP_ID="1410650005904021"
IIIN_SERVER_SERCRET = '52c5ce6ee56af4221c6215f3fc1418d4'
FB_REST_API = 'http://api.facebook.com/restserver.php'
TWITTER_URL_API = 'http://urls.api.twitter.com/1/urls/count.json'
POISON = "quite_queue"
UPDATE_COUNT_PERIOD = 5*60;
DELETE_PERIOD = 14 * 24 * 60 * 60
'''=========================================================================
Thread waiting to get comment like and share for url, then save result in db
==========================================================================='''
class StatisticGetterThread(Thread):
    # define a constructor, parameterised a queue
    def __init__(self):
        Thread.__init__(self)
        self.name= "Thread_share_like_comment_count"
        self.is_running = True
    
    def stop_running (self):
        self.is_running = False
    
    def run(self):
        
        try:
            db_thread = IIIDatbaseConnection()
            db_thread.init_database_cont()
            ''' get list of existing url from db here'''
            running_time = 0
            while self.is_running:
                running_time = running_time + 1
                print("======================= Running time" + str(running_time) + "   ==============================")
                cur = db_thread.cursor()
                cur.execute("SELECT id, url, updated_time FROM articles WHERE is_duplicated = 0 AND UNIX_TIMESTAMP() - last_update_statistic > " + str(40 * 60))
                #print(len(cur.fetchall()))
                for r in cur.fetchall():
                    if (self.is_running):
                        try:
                            next_url = r[1]
                            try:
                                if (int(time.time()) - int(r[2]) > DELETE_PERIOD):
                                    db_thread.delete_article(r[0])
                            except Exception as e:
                                print("Error when delete old articles: {}".format(e))    
                            fb_param = dict(method = 'links.getStats',
                                        urls = urllib.parse.quote(next_url, safe=''),
                                        format = 'json')
                            tw_param = dict(url=next_url)
                            fb_resp = requests.get(url=FB_REST_API, params = fb_param)
                            print(fb_resp.text)
                            data = json.loads(fb_resp.text)[0]
                            # from twitter
                            tw_resp = None
                            tw_share = 0
                            try:
                                tw_resp = requests.get(url=TWITTER_URL_API, params = tw_param)
                            except Exception as db_e:
                                print("Error when get Twitter {}".format(db_e))
                            if(tw_resp is not None):
                                twi_data = json.loads(tw_resp.text)
                                tw_share = twi_data['count']
                            #print(data)
                            #print(twi_data)
                            print(db_thread.update_article_count(next_url, data['comment_count'],
                                                                 data['share_count'], data['like_count'], data['comments_fbid'], tw_share))
                        except Exception as e:
                            print("Error when get FB, TW like comment: {}".format(e))
                cur.close()
                time.sleep(UPDATE_COUNT_PERIOD)
        except Exception as db_e:
            print("Error database thread get like_share count: {}".format(db_e))
        finally:
            #close connection db before exit
            if (db_thread is not None):
                db_thread.close_database_cont()
'''    
=========================== end of get like, share thread =====================
'''













FB_LONGLIVE_ACTK = "CAAUCZBoyBGpUBACo0GuUx75S24R9nzHz8rOPZAXQZBJGzZBKv6dJOjiM2EAbmxKiWZApxQPW0sSlpVAfFu2ZAqzDr5MdbTUxwstdaFWNTbVe4hs68J0NhlPGdN16Fr5BpEZBb9mlxNm7XjQSxARZCos40An5pcVkuUFodWZAQanjJrZCL20xDqyZCmHqaZBdGdgYbHGCBt8c1LqULzjmZA8nL3sNj"
IIIN_SERVER_APP_ID="1410650005904021"
IIIN_SERVER_SERCRET = '52c5ce6ee56af4221c6215f3fc1418d4'

# pages_id = ["657808134330750", '1417094931918673', 
#             '329570850574813', '1592315347647071',
#             '1401344456845009', '445841905563902',
#             '778046915618571'
#             ]

sources_page_id = ['5550296508', '18793419640',
                   '13652355666', '18468761129',
                   '155869377766434', '114288853688',
                   '89686424098', '86680728811',
                   '5863113009', '123551651184',
                   '100679109890', '184963273336',
                   '123131338119', '113371309369',
                   '5281959998', '6250307292',
                   '33735392231', '374111579728',
                   '15225899564', '96028256183',
                   '131459315949', '13539254023',
                   '266790296879', '1481073582140028',
                   '154758931259107', '15704546335',
                   '10674237167', '146289548765543',
                   '168744703121', '47689998796',
                   '104266592953439', '21898300328',
                   '328451927331630', '1318800798260799',
                   '491452930867938', '30911162508', 
                   '269299195015', '95926963131',
                   '42933792278', '42933792278',
                   '274832347617', '89033370735',
                   '8062627951', '7331091005'
                   
                   ]
pages_toke = {}  
    
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










class GetFacebookPostForUrl(Thread):
    
    # define a constructor, parameterised a queue
    def __init__(self):
        Thread.__init__(self)
        self.name= "Thread_post_2_facebook_page"
        self.is_running = True
    
    def stop_running (self):
        self.is_running = False
        

    
        
    def run(self):
        print("thread post article to page already started")
        try:
            db_thread = IIIDatbaseConnection()
            db_thread.init_database_cont()
            #get statistic on FB, TW
            
            while self.is_running:
                try:
                    for source_id in sources_page_id:
                        print("=============== sourceid: " + source_id + "   ===============")
                        api = get_api(FB_LONGLIVE_ACTK, '657808134330750')
                        posts = api.get_object(id=source_id +'/posts')
                        #print(posts['data'])
                        for post in posts['data']:
                            try:
                                string_post_content = ''
                                if ('story' in post):
                                    string_post_content = string_post_content + post['story'] + " "
                                if ('link' in post):
                                    string_post_content = string_post_content + " " + post['link'] + " "
                                    print(post['link'])
                                if ('message' in post):
                                    string_post_content = string_post_content + post['message']
                                    print(post['message'])
                                if (string_post_content is not None):
                                    print("post content: " + string_post_content)
                                    urls = re.findall(r'(https?://\S+)', string_post_content)
                            
                                if (urls is None or len(urls) <= 0):
                                    print("not found url")
                                else: # save id to database
                                    for url in urls:
                                        url = utils.normalize_url(url)
                                        print("postId: " + post['id'] + " : " + url)
                                        print(db_thread.update_article_fbid(url, post['id']))
                            except Exception as e:
                                print("Error when get url from facebook post: {}".format(e))   
                except Exception as e:
                    print("Error when get url from facebook post: {}".format(e))
                time.sleep(10* UPDATE_COUNT_PERIOD)
        except Exception as db_e:
            print("Error database thread post to Facebook: {}".format(db_e))
        finally:
            #close connection db before exit
            if (db_thread is not None):
                db_thread.close_database_cont()      
    
    
    
    
    
    
#     
get_official_posts_thread = GetFacebookPostForUrl()
get_official_posts_thread.start()

    
share_like_comment_thread = StatisticGetterThread()
share_like_comment_thread.start()