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

from crawlerApp import utils
from fbsdk import facebook
from iiidatabase.DatabaseConnectionLib import IIIDatbaseConnection


FB_LONGLIVE_ACTK = "CAAUCZBoyBGpUBACo0GuUx75S24R9nzHz8rOPZAXQZBJGzZBKv6dJOjiM2EAbmxKiWZApxQPW0sSlpVAfFu2ZAqzDr5MdbTUxwstdaFWNTbVe4hs68J0NhlPGdN16Fr5BpEZBb9mlxNm7XjQSxARZCos40An5pcVkuUFodWZAQanjJrZCL20xDqyZCmHqaZBdGdgYbHGCBt8c1LqULzjmZA8nL3sNj"
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
                    
                    
                    
                    
                    
                    
                    
                    




                    
FB_LONGLIVE_ACTK = "CAAUCZBoyBGpUBACo0GuUx75S24R9nzHz8rOPZAXQZBJGzZBKv6dJOjiM2EAbmxKiWZApxQPW0sSlpVAfFu2ZAqzDr5MdbTUxwstdaFWNTbVe4hs68J0NhlPGdN16Fr5BpEZBb9mlxNm7XjQSxARZCos40An5pcVkuUFodWZAQanjJrZCL20xDqyZCmHqaZBdGdgYbHGCBt8c1LqULzjmZA8nL3sNj"
IIIN_SERVER_APP_ID="1410650005904021"
IIIN_SERVER_SERCRET = '52c5ce6ee56af4221c6215f3fc1418d4'

pages_id = ["657808134330750", '1417094931918673', 
            '329570850574813', '1592315347647071',
            '1401344456845009', '445841905563902',
            '778046915618571'
            ]


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
                    if (next_article == None or next_article == POISON):
                        self.stop_running()
                        break
                    page_id_position = posts_count % len(pages_id) # post to all pages by each one
                    posts_count += 1
                    api = get_api(FB_LONGLIVE_ACTK, pages_id[page_id_position])
                    msg = ""
                    attchment = {"name": next_article.title,
                             "link": next_article.url,
                             "caption": "By IIIN",
                             "description": next_article.short_description,
                             "picture": next_article.thumbnail_url}
                    result =  api.put_wall_post(msg, attachment = attchment)
                    
                    if (result is None or result['id'] is None):
                        print("Cannot post " + next_article.url + " to FB page")
                    else: # save id to database
                        print("postId: " + result['id'])
                        print(db_thread.update_article_fbid(next_article.url, result['id']))
                except Exception as e:
                    print("Error when post article to FB pages: {}".format(e))
                time.sleep(5)
        except Exception as db_e:
            print("Error database thread post to Facebook: {}".format(db_e))
        finally:
            #close connection db before exit
            if (db_thread is not None):
                db_thread.close_database_cont()   
    
        
        
        
    
    

    
    
    
    

    
    
    
    