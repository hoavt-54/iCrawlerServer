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



FB_REST_API = 'http://api.facebook.com/restserver.php'
TWITTER_URL_API = 'http://urls.api.twitter.com/1/urls/count.json'
POISON = "quite_queue"
UPDATE_COUNT_PERIOD = 5*60;
DELETE_PERIOD = 4 * 24 * 60 * 60
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
            ''' get list of existing url from db here'''
            running_time = 0
            while self.is_running:
                try:
                    
                    running_time = running_time + 1
                    print("======================= Running time" + str(running_time) + "   ==============================")
                    all_urls = {}
                    try:
                        load_db_cont = IIIDatbaseConnection()
                        load_db_cont.init_database_cont()
                        cur = load_db_cont.cursor()
                        cur.execute("SELECT id, url, updated_time FROM articles WHERE is_duplicated = 0 AND UNIX_TIMESTAMP() - last_update_statistic > " + str(40 * 60))
                        all_urls = cur.fetchall()
                    except Exception as e:
                        print("Cannot read database {}".format(e))
                    finally:
                        try:
                            cur.close()
                            load_db_cont.close_database_cont()
                        except Exception as e:
                            pass
                        
                    print(len(all_urls))
                    for r in all_urls:
                        if (self.is_running):
                            try:
                                next_url = r[1]
                                if (int(time.time()) - int(r[2]) > DELETE_PERIOD):
                                    try:
                                        delelte_cont = IIIDatbaseConnection()
                                        delelte_cont.init_database_cont()
                                        delelte_cont.delete_article(r[0])
                                    except Exception as e:
                                        print("Error when delete old articles: {}".format(e))   
                                    finally:
                                        try:
                                            delelte_cont.close_database_cont()
                                        except Exception as e:
                                            pass
                                    continue
                                fb_param = dict(method = 'links.getStats',
                                            urls = urllib.parse.quote(next_url, safe=''),
                                            format = 'json')
                                tw_param = dict(url=next_url)
                                fb_resp = requests.get(url=FB_REST_API, params = fb_param)
                                print(fb_resp.text)
                                data = json.loads(fb_resp.text)[0]
                                # from twitter
                                '''tw_resp = None
                                tw_share = 0
                                try:
                                    tw_resp = requests.get(url=TWITTER_URL_API, params = tw_param)
                                except Exception as db_e:
                                    print("Error when get Twitter {}".format(db_e))
                                if(tw_resp is not None):
                                    twi_data = json.loads(tw_resp.text)
                                    tw_share = twi_data['count']
                                print(data)
                                print(twi_data)'''
                                try:
                                    save_cont = IIIDatbaseConnection()
                                    save_cont.init_database_cont()
                                    print(save_cont.update_article_count(next_url, data['comment_count'],
                                                                     data['share_count'], data['like_count'], data['comments_fbid'], 0))
                                except Exception as e:
                                    print("Error when update count for article: {}".format(e))   
                                finally:
                                    try:
                                        save_cont.close_database_cont()
                                    except Exception as e:
                                        pass
                            except Exception as e:
                                print("Error when get FB, TW like comment: {}".format(e))
                    all_urls = None
                except Exception as db_e:
                    print("Error database thread get like_share count: {}".format(db_e))
                print("finsihed one round, now take sleep")
                time.sleep(UPDATE_COUNT_PERIOD)
        except Exception as db_e:
            print("Error database thread get like_share count: {}".format(db_e))
'''    
=========================== end of get like, share thread =====================
'''













IIIN_SERVER_APP_ID="1410650005904021"
IIIN_SERVER_SERCRET = '52c5ce6ee56af4221c6215f3fc1418d4'

# pages_id = ["657808134330750", '1417094931918673', 
#             '329570850574813', '1592315347647071',
#             '1401344456845009', '445841905563902',
#             '778046915618571'
#             ]

sources_page_id = [
                    '5550296508', '18793419640',
                   '7873709245', '219367258105115', 
                   '6651543066', 
                   '86680728811', '163497464933', #abc
                   '13652355666', '18468761129',
                   '155869377766434', '114288853688',
                   '89686424098', '124213184321534', # bloomberg view
                   '5863113009', '123551651184',
                   '100679109890', '184963273336',
                   '123131338119', '113371309369',
                    '6250307292',
                   '33735392231', '374111579728',
                   '315575098522880','123551651184',  # la entertainment 
                   '15225899564', '96028256183',
                   '131459315949', '13539254023',
                   '266790296879', '1481073582140028',
                   '154758931259107', 
                   '10674237167', '146289548765543',
                   '168744703121', '47689998796',
                   '104266592953439', 
                   '328451927331630', '1318800798260799',
                   '491452930867938', '30911162508', 
                   '269299195015', '95926963131',
                   '42933792278', '42933792278',
                   '274832347617', '89033370735',
                   '8062627951', '7331091005',
                   '18807449704', '500945955060', # mashable
                   '20446254070', '516821321748618', # business insider
                   '116548701336', '119737589217', # uproxx
                   '140738092630206', # the blaze
                   '367116489976035', # I freaking love sricen
                   '112638779551','81286652945', # fox sport
                   '5281959998', 
                   '105307012882667', '176999952314969',# newyork time science
                   '5518834980', '314077407675', # newyork times entertain
                   '15704546335',
                   '21898300328', 
                   '114050161948682', '208994395842496', # reuters 
                   '268914272540', #newyork daily news
                   '97212224368', #cnbc
                   ]
pages_toke = {}  
TOKEN_TIMEOUT = 40 * 24 * 60 * 60
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
        self.FB_LONGLIVE_ACTK = None
        self.LAST_TIME_GET_TOKEN = 0
    
    def stop_running (self):
        self.is_running = False
        

    
        
    def run(self):
        print("thread post article to page already started")
        try:
            db_thread = IIIDatbaseConnection()
            #get statistic on FB, TW
            
            while self.is_running:
                try:
                    if (int(time.time()) - self.LAST_TIME_GET_TOKEN > TOKEN_TIMEOUT):
                        with open ("../../fb_token.txt", "r") as myfile:
                            self.FB_LONGLIVE_ACTK =myfile.read().replace('\n', '')
                            self.LAST_TIME_GET_TOKEN = int(time.time())
                            print("refreshed Facebook token")
                    for source_id in sources_page_id:
                        print("=============== sourceid: " + source_id + "   ===============")
                        api = get_api(self.FB_LONGLIVE_ACTK, '657808134330750')
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
                                    #print("post content: " + string_post_content)
                                    urls = re.findall(r'(https?://\S+)', string_post_content)
                            
                                if (urls is None or len(urls) <= 0):
                                    print("not found url")
                                else: # save id to database
                                    for url in urls:
                                        try:
                                            db_thread.init_database_cont()
                                            url = utils.normalize_url(url)
                                            print("postId: " + post['id'] + " : " + url)
                                            print(db_thread.update_article_fbid(url, post['id']))
                                            db_thread.close_database_cont() 
                                        except Exception as e:
                                            print("Error when save facebook post id to db: {}".format(e))
                            except Exception as e:
                                print("Error when get url from facebook post: {}".format(e))   
                except Exception as e:
                    print("Error when get url from facebook post: {}".format(e))
                time.sleep(2* UPDATE_COUNT_PERIOD)
        except Exception as db_e:
            print("Error database thread post to Facebook: {}".format(db_e))
        finally:
            #close connection db before exit
            if (db_thread is not None):
                db_thread.close_database_cont()      
    
    
    
    
    
    
# #     
get_official_posts_thread = GetFacebookPostForUrl()
get_official_posts_thread.start()

    
share_like_comment_thread = StatisticGetterThread()
share_like_comment_thread.start()