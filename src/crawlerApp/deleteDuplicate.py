'''
Created on Mar 16, 2015

@author: hoavu
'''
import json
import os.path
import queue
import re
import requests
import sys
from threading import Thread
import time
import urllib.parse

from crawlerApp import utils
from crawlerApp.utils import get_consine_text, normalize_text
from fbsdk import facebook
from iiidatabase.DatabaseConnectionLib import IIIDatbaseConnection


sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
UPDATE_COUNT_PERIOD = 30*60;
DUPLICATION_TIME_POSISIBLE = 24 * 60 * 60
class DeleteDuplicateThread(Thread):
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
                cur.execute("SELECT id,text, updated_time, title, category_id FROM articles WHERE is_duplicated = 0 AND UNIX_TIMESTAMP() - last_update_statistic < " + str(4 * 60 * 60))
                articles_set = cur.fetchall()
                print(len(articles_set))
                for article1 in articles_set:
                    for article2 in articles_set:
                        try:
                            similarity_content = get_consine_text(article1[1], article2[1])
                            similarity_title = get_consine_text(normalize_text(article1[3]), normalize_text(article2[3]))
                            similarity = (3 * similarity_content + 2 * similarity_title)/5
                            if (article1[0] != article2[0] and similarity > 0.56 
                                        and abs(article1[2] - article2[2]) < DUPLICATION_TIME_POSISIBLE 
                                        and article1[3] == article2[3]):
                                
                                print(similarity)
                                print("gotta delete")
                                print(article1[3] + "   ======================     " + article2[3])
                                duplicated_id = 0
                                if int(article1[2]) < int(article2[2]):
                                    duplicated_id = article1[0]
                                else:
                                    duplicated_id = article2[0]
                                print(db_thread.update_article_duplicated(duplicated_id, True))
                        
                        
                        
                        except Exception as e:
                            print("Error when get cosine and delete: {}".format(e))
                cur.close()
                print("finished: " + str(running_time))
                time.sleep(UPDATE_COUNT_PERIOD)
        except Exception as db_e:
            print("Error database duplicate: {}".format(db_e))
        finally:
            #close connection db before exit
            if (db_thread is not None):
                db_thread.close_database_cont()
'''    
=========================== end of get like, share thread =====================
'''
                
                




remove_duplicate_thread = DeleteDuplicateThread()
remove_duplicate_thread.start()